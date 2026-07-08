# coding=utf-8
import urllib.parse
import urllib.request
import urllib.error
import json
import smtplib

# Slack post data needs to be encoded in UTF-8
def encoded_dict(in_dict):
    out_dict = {}
    for k, v in in_dict.items():
        if isinstance(v, str):
            v = v.encode('utf8')
        out_dict[k] = v
    return out_dict


class NotificationException(Exception):
    pass


def check_urlib_response(response, platform):
    response_str = response.read()
    response_obj = json.loads(response_str)
    if not response_obj['ok']:
        msg = "Error connecting to {0}, got response: {1}".format(platform, response_obj)
        raise NotificationException(msg)


def post_to_slack(msg, channels, token):
    for channel in channels:
        post_data = {'text': msg, 'channel': channel, 'token': token}
        enc_post_data = urllib.parse.urlencode(encoded_dict(post_data)).encode('utf-8')
        url = 'https://{}/api/{}'.format('slack.com', 'chat.postMessage')
        response = urllib.request.urlopen(url, enc_post_data)
        check_urlib_response(response, 'slack')


def post_to_telegram(msg, chat_ids, bot_id):
    for chat_id in chat_ids:
        post_data = {"chat_id": chat_id, "text": msg}
        url = "https://api.telegram.org/bot" + bot_id + "/sendMessage"
        try:
            response = urllib.request.urlopen(url, urllib.parse.urlencode(post_data).encode('utf-8'))
            check_urlib_response(response, 'telegram')
        except urllib.error.HTTPError as e:
            msg = "Your bot id is probably configured incorrectly"
            raise NotificationException("{0}\n{1}".format(e, msg))


def send_email(msg, email_login_address, email_login_password, email_smtp_server, email_smtp_port,
               email_to_addresses, email_smtp_starttls):
    subject = 'Lending bot'

    email_text = "\r\n".join(["From: {0}".format(email_login_address),
                              "To: {0}".format(", ".join(email_to_addresses)),
                              "Subject: {0}".format(subject),
                              "",
                              "{0}".format(msg)
                              ])

    try:
        if email_smtp_starttls:
            server = smtplib.SMTP(email_smtp_server, email_smtp_port)
            server.ehlo()
            server.starttls()
        else:
            server = smtplib.SMTP_SSL(email_smtp_server, email_smtp_port)
        server.ehlo()
        server.login(email_login_address, email_login_password)
        server.sendmail(email_login_address, email_to_addresses, email_text)
        server.close()
    except Exception as e:
        print("Could not send email, got error {0}".format(e))
        raise NotificationException(e)

def post_to_pushbullet(msg, token, deviceid):
    post_data = {'body': msg, 'device_iden': deviceid, 'title': 'Poloniex Bot', 'type': 'note'}
    opener = urllib.request.build_opener()
    req = urllib.request.Request('https://api.pushbullet.com/v2/pushes', data=json.dumps(post_data).encode('utf-8'),
                          headers={'Content-Type': 'application/json', 'Access-Token': token})
    try:
        response = opener.open(req)
    except Exception as e:
        print("Could not send pushbullet, got error {0}".format(e))
        raise NotificationException(e)

def send_notification(msg, notify_conf):
    nc = notify_conf
    if nc['email']:
        send_email(msg, nc['email_login_address'], nc['email_login_password'], nc['email_smtp_server'],
                   nc['email_smtp_port'], nc['email_to_addresses'], nc['email_smtp_starttls'])
    if nc['slack']:
        post_to_slack(msg, nc['slack_channels'], nc['slack_token'])
    if nc['telegram']:
        post_to_telegram(msg, nc['telegram_chat_ids'], nc['telegram_bot_id'])
    if nc['pushbullet']:
        post_to_pushbullet(msg, nc['pushbullet_token'], nc['pushbullet_deviceid'])
