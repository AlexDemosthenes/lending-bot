# Deploy Stock Trading App to Cloud

Choose one of these platforms to deploy your app. All have free tiers!

## 🚀 Option 1: Railway (EASIEST - Recommended)

**Why Railway?** Fastest deployment, great free tier, automatic SSL.

### Steps:
1. Go to [railway.app](https://railway.app)
2. Sign up/login with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select this repository
5. Select the `cursor/stock-trading-app-e049` branch
6. Set root directory to `stock_app`
7. Railway auto-detects everything and deploys!
8. Click "Generate Domain" to get your URL
9. Open on iPhone: `https://your-app.railway.app`

**Deploy Time:** ~3 minutes  
**Free Tier:** 500 hours/month

---

## 🎨 Option 2: Render (Also Easy)

**Why Render?** Reliable, free tier, simple setup.

### Steps:
1. Go to [render.com](https://render.com)
2. Sign up/login with GitHub
3. Click "New" → "Web Service"
4. Connect your GitHub repo
5. Select `cursor/stock-trading-app-e049` branch
6. Configure:
   - **Name:** stock-movers
   - **Root Directory:** stock_app
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
7. Click "Create Web Service"
8. Wait for deployment (~5 min)
9. Open on iPhone: `https://stock-movers.onrender.com`

**Deploy Time:** ~5 minutes  
**Free Tier:** Yes, sleeps after 15 min inactivity

---

## 🐍 Option 3: PythonAnywhere

**Why PythonAnywhere?** Always on, no sleep, Python-focused.

### Steps:
1. Go to [pythonanywhere.com](https://www.pythonanywhere.com)
2. Sign up for free account
3. Go to "Files" → Upload stock_app folder
4. Open a Bash console:
   ```bash
   cd ~/stock_app
   pip install --user -r requirements.txt
   ```
5. Go to "Web" tab → "Add a new web app"
6. Choose "Flask"
7. Set:
   - **Source code:** `/home/YOUR_USERNAME/stock_app`
   - **Working directory:** `/home/YOUR_USERNAME/stock_app`
   - **WSGI file:** Edit to point to `app.py`
8. Click "Reload" your web app
9. Open on iPhone: `https://YOUR_USERNAME.pythonanywhere.com`

**Deploy Time:** ~10 minutes  
**Free Tier:** Always on (with pythonanywhere.com subdomain)

---

## ⚡ Option 4: Vercel (Serverless)

**Why Vercel?** Very fast, edge network, free SSL.

### Steps:
1. Go to [vercel.com](https://vercel.com)
2. Sign up/login with GitHub
3. Click "Add New" → "Project"
4. Import your GitHub repo
5. Configure:
   - **Root Directory:** stock_app
   - **Framework Preset:** Other
   - **Build Command:** `pip install -r requirements.txt`
   - **Output Directory:** (leave empty)
6. Add file `vercel.json` (already created if using our repo)
7. Deploy!
8. Open on iPhone: `https://your-app.vercel.app`

**Deploy Time:** ~2 minutes  
**Free Tier:** Generous limits

---

## 📱 After Deployment

### Add to iPhone Home Screen:
1. Open the app URL in Safari
2. Tap the Share button
3. Scroll down and tap "Add to Home Screen"
4. Name it "Stock Movers"
5. Now it looks like a native app! 🎉

### Bookmark It:
- Save the URL in your Safari bookmarks
- Access anytime, anywhere!

---

## 🔧 Troubleshooting

**App is slow on first load?**
- Free tiers "sleep" after inactivity
- First request wakes it up (~30 sec)
- Subsequent requests are fast!

**Data not loading?**
- Yahoo Finance API may have rate limits
- Try refreshing after a minute
- Reduce number of stocks in STOCK_UNIVERSE if needed

**Need help?**
- All platforms have excellent documentation
- Railway and Render have great support channels

---

## 💡 Pro Tips

1. **Custom Domain:** Most platforms let you add custom domains
2. **Environment Variables:** Keep API keys secure (if you add any)
3. **Monitoring:** Enable uptime monitoring (free with many services)
4. **Scaling:** All platforms offer paid tiers for more power

---

## 🎯 Recommended Choice

**For beginners:** Railway (easiest, fastest)  
**For reliability:** Render (very stable)  
**For Python devs:** PythonAnywhere (Python-specific features)  
**For speed:** Vercel (edge network)

Choose Railway if you want to deploy in under 5 minutes! 🚀
