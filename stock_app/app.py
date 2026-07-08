#!/usr/bin/env python3
"""
Stock Trading App - Find Big Movers with 21 EMA Entry Points
"""
import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from flask import Flask, render_template, jsonify
import plotly.graph_objs as go
import plotly.utils
import json

app = Flask(__name__)

# List of popular stocks to scan (you can expand this)
STOCK_UNIVERSE = [
    'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META', 'TSLA', 'NVDA', 'AMD', 
    'NFLX', 'DIS', 'PYPL', 'INTC', 'CSCO', 'ADBE', 'CRM', 'ORCL',
    'BABA', 'TSM', 'V', 'MA', 'JPM', 'BAC', 'WMT', 'HD', 'PFE',
    'JNJ', 'UNH', 'CVX', 'XOM', 'KO', 'PEP', 'NKE', 'MCD', 'SBUX',
    'BA', 'CAT', 'GE', 'GM', 'F', 'COIN', 'SQ', 'SHOP', 'ROKU',
    'SNAP', 'TWTR', 'UBER', 'LYFT', 'ZM', 'DOCU', 'PLTR', 'SNOW'
]


def calculate_ema(data, period=21):
    """Calculate Exponential Moving Average"""
    return data.ewm(span=period, adjust=False).mean()


def find_big_movers(min_move_percent=15, days_back=7):
    """
    Find stocks that moved 15% or more in a single day over the last week
    Returns: List of (ticker, move_percent, date) tuples
    """
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days_back + 30)  # Extra days for EMA calculation
    
    big_movers = []
    
    print(f"Scanning {len(STOCK_UNIVERSE)} stocks for {min_move_percent}%+ moves...")
    
    for ticker in STOCK_UNIVERSE:
        try:
            stock = yf.Ticker(ticker)
            hist = stock.history(start=start_date, end=end_date)
            
            if hist.empty or len(hist) < 2:
                continue
            
            # Calculate daily percentage change
            hist['Daily_Change'] = ((hist['Close'] - hist['Open']) / hist['Open'] * 100).abs()
            
            # Check for big moves in the last week
            recent_week = hist.tail(days_back)
            max_move = recent_week['Daily_Change'].max()
            
            if max_move >= min_move_percent:
                max_move_date = recent_week['Daily_Change'].idxmax()
                big_movers.append({
                    'ticker': ticker,
                    'move_percent': round(max_move, 2),
                    'date': max_move_date.strftime('%Y-%m-%d'),
                    'current_price': round(hist['Close'].iloc[-1], 2),
                    'data': hist
                })
                print(f"  ✓ {ticker}: {max_move:.2f}% move on {max_move_date.strftime('%Y-%m-%d')}")
        
        except Exception as e:
            print(f"  ✗ Error fetching {ticker}: {str(e)}")
            continue
    
    # Sort by move percentage (highest first) and return top 15
    big_movers.sort(key=lambda x: x['move_percent'], reverse=True)
    return big_movers[:15]


def create_chart(ticker_data):
    """Create interactive chart with 21 EMA"""
    hist = ticker_data['data']
    
    # Calculate 21 EMA
    hist['EMA_21'] = calculate_ema(hist['Close'], 21)
    
    # Create candlestick chart
    fig = go.Figure()
    
    # Add candlestick
    fig.add_trace(go.Candlestick(
        x=hist.index,
        open=hist['Open'],
        high=hist['High'],
        low=hist['Low'],
        close=hist['Close'],
        name='Price',
        increasing_line_color='#26a69a',
        decreasing_line_color='#ef5350'
    ))
    
    # Add 21 EMA
    fig.add_trace(go.Scatter(
        x=hist.index,
        y=hist['EMA_21'],
        mode='lines',
        name='21 EMA (Entry)',
        line=dict(color='#2196F3', width=2)
    ))
    
    # Update layout
    fig.update_layout(
        title=f"{ticker_data['ticker']} - {ticker_data['move_percent']}% Move on {ticker_data['date']}",
        yaxis_title='Price ($)',
        xaxis_title='Date',
        template='plotly_dark',
        height=400,
        xaxis_rangeslider_visible=False,
        hovermode='x unified'
    )
    
    return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)


@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')


@app.route('/api/scan')
def scan_stocks():
    """API endpoint to scan for big movers"""
    try:
        big_movers = find_big_movers(min_move_percent=15, days_back=7)
        
        # Create charts for each stock
        results = []
        for mover in big_movers:
            results.append({
                'ticker': mover['ticker'],
                'move_percent': mover['move_percent'],
                'date': mover['date'],
                'current_price': mover['current_price'],
                'ema_21': round(mover['data']['EMA_21'].iloc[-1], 2) if 'EMA_21' in mover['data'].columns else None,
                'chart': create_chart(mover)
            })
        
        return jsonify({
            'success': True,
            'count': len(results),
            'stocks': results
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
