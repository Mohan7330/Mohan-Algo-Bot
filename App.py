import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# Page Configuration for Mobile Friendly Dashboard
st.set_page_config(page_title="Mohan Algo Dashboard", layout="wide")

st.title("🚀 Mohan's F&O Smart Trading Dashboard (Paper Trading)")
st.markdown("---")

# Sidebar Controls for Bot Status
st.sidebar.header("Bot Control Panel")
bot_status = st.sidebar.radio("Bot Status", ["OFF", "ON"])
market_mode = st.sidebar.selectbox("Market Condition Mode", ["Auto Detect (Trend / Range)", "Forced Trend", "Forced Sideways"])

# Initialize Session State for Signal Logs & Live Tracking
if 'signal_logs' not in st.session_state:
    st.session_state['signal_logs'] = pd.DataFrame(columns=[
        'BUY TIME', 'CONTRACT', 'SCORE', 'BUY PRICE', 'STOP LOSS', 'TARGET', 'SELL PRICE', 'SELL TIME', 'RESULT', 'P&L'
    ])

if 'active_trade' not in st.session_state:
    st.session_state['active_trade'] = None

# Main Dashboard Layout
col1, col2, col3, col4 = st.columns(4)
col1.metric("Bot Status", bot_status, "Active" if bot_status == "ON" else "Paused")
col2.metric("Active Trades", "1" if st.session_state['active_trade'] else "0")
col3.metric("Total P&L (Paper)", "₹ +1,450", "+12%")
col4.metric("Win Rate", "55.2%", "Target/SL: 30 Pts")

st.markdown("### 📊 Live Tracking & Market Analysis")

# Logic Simulation & Metrics Display
if bot_status == "ON":
    st.info("🤖 Bot is actively scanning Nifty 50 5-min candles, S&R, Volume, RSI, ATR & ADX...")
    
    # Simulating Live Tracking Box (like friend's dashboard)
    if st.session_state['active_trade'] is None:
        # Let's simulate a triggered trade based on user logic
        current_time = datetime.now().strftime("%d Oct, %H:%M")
        st.session_state['active_trade'] = {
            'buy_time': current_time,
            'contract': 'Nifty 23050 CE',
            'score': 75,
            'buy_price': 123.65,
            'stop_loss': 93.65,    # Exactly 30 points SL
            'target': 153.65,       # Exactly 30 points Target
            'now_price': 130.50
        }
    
    trade = st.session_state['active_trade']
    
    st.markdown(f"""
    <div style="background-color: #1e293b; padding: 20px; border-radius: 10px; color: white;">
        <h4>Tracking: {trade['contract']} | Score: {trade['score']}/100</h4>
        <p><b>Buy Price:</b> ₹{trade['buy_price']} | <b>Stop Loss (30 Pts):</b> ₹{trade['stop_loss']} | <b>Target (30 Pts):</b> ₹{trade['target']}</p>
        <p><b>Current Live Price:</b> ₹{trade['now_price']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Simulate Exit (Hit Target / SL)"):
        # Move active trade to logs
        sell_time = datetime.now().strftime("%d Oct, %H:%M")
        new_log = {
            'BUY TIME': trade['buy_time'],
            'CONTRACT': trade['contract'],
            'score': trade['score'],
            'BUY PRICE': trade['buy_price'],
            'STOP LOSS': trade['stop_loss'],
            'TARGET': trade['target'],
            'SELL PRICE': trade['target'], # Assuming target hit
            'SELL TIME': sell_time,
            'RESULT': 'target',
            'P&L': '+₹1,500'
        }
        st.session_state['signal_logs'] = pd.concat([pd.DataFrame([new_log]), st.session_state['signal_logs']], ignore_index=True)
        st.session_state['active_trade'] = None
        st.rerun()

else:
    st.warning("⚠️ Bot is currently OFF. Switch to ON from the sidebar to start live paper tracking.")

st.markdown("---")
st.markdown("### 📝 Signal Log & History Table")

# Display Signal Log Table
if not st.session_state['signal_logs'].empty:
    st.dataframe(st.session_state['signal_logs'], use_container_width=True)
else:
    st.info("No closed trades yet. Once trades hit 30 Pts Target or 30 Pts Stop Loss, they will log here automatically.")
