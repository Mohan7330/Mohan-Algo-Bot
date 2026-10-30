import streamlit as st
import pandas as pd
import numpy as np

# Page Configuration
st.set_page_config(page_title="Trade Tracker", layout="wide")

# Professional Trading Terminal CSS (Dark Theme)
st.markdown("""
    <style>
    .main { background-color: #0b0e14; color: #ffffff; }
    .card-container {
        background-color: #161b22;
        border: 1px solid #30363d;
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 20px;
    }
    .metric-box {
        background-color: #21262d;
        padding: 15px;
        border-radius: 8px;
        text-align: center;
        border: 1px solid #30363d;
    }
    div[data-testid="stNumberInput"] {
        max-width: 120px;
        margin-left: auto;
        margin-top: 0px;
        margin-bottom: 0px;
    }
    div[data-testid="stNumberInput"] label {
        display: block;
        font-size: 11px;
        font-weight: 600;
        color: #8b949e;
        margin-bottom: 4px;
    }
    div[data-testid="stNumberInput"] > div {
        width: 100%;
        min-width: 0;
    }
    div[data-testid="stNumberInput"] input {
        font-size: 12px;
        padding: 3px 5px;
        height: 28px;
        border: 1px solid #3fb950;
        border-radius: 6px;
        background-color: #0b0e14;
        color: white;
    }
    div[data-testid="stNumberInput"] button {
        width: 22px;
        min-width: 22px;
        height: 22px;
        padding: 0;
        border: 1px solid #3fb950;
        color: #3fb950;
        background-color: #0b0e14;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Menu (Simple & Clean)
with st.sidebar:
    st.markdown("### ⚡ TrustedTrade")
    st.markdown("---")
    st.markdown("📊 **Dashboard**")
    st.markdown("📋 **Orders**")
    st.markdown("📈 **Positions**")
    st.markdown("⚙️ **Analytics & Logs**")
    st.markdown("---")
    bot_status = st.toggle("Bot Status (ON/OFF)", value=False)
    if bot_status:
        st.success("🟢 Bot is Running")
    else:
        st.error("🔴 Bot is Paused")

# Main Dashboard Header
st.markdown("## 📊 Nifty Options - Live Terminal")

# Top-right compact lot size box
header_left, header_right = st.columns([5, 1])
with header_right:
    lot_size = st.number_input("Lot Size", min_value=1, max_value=50, value=1, step=1)

st.markdown("---")

# Signal Card
st.markdown("""
    <div class="card-container">
        <span style="background-color: #1f6feb; color: white; padding: 4px 10px; border-radius: 4px; font-weight: bold; font-size: 12px;">ACTIVE SIGNAL</span>
        <h2 style="color: #3fb950; margin-top: 10px;">BUY 23,050 CE</h2>
        <p style="color: #8b949e;">Nifty 23050 CE: buy @123.00, stop @93.65, target @153.65. Now ₹123.00. 0.00 to target.</p>
    </div>
""", unsafe_allow_html=True)

# Market Status Row only below signal
st.info("💡 **Market Status:** Live feed connected successfully. Ready for execution.", icon="💡")

# Price Breakdown Cards
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
        <div class="metric-box">
            <p style="color: #8b949e; margin: 0;">Buying Price</p>
            <h3 style="color: #58a6ff; margin: 5px 0 0 0;">₹123.03</h3>
            <span style="font-size: 12px; color: #8b949e;">LTP: ₹123.03</span>
        </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
        <div class="metric-box">
            <p style="color: #8b949e; margin: 0;">Stop Loss (SL)</p>
            <h3 style="color: #f85149; margin: 5px 0 0 0;">₹93.65</h3>
            <span style="font-size: 12px; color: #8b949e;">(-30 Points)</span>
        </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
        <div class="metric-box">
            <p style="color: #8b949e; margin: 0;">Target</p>
            <h3 style="color: #3fb950; margin: 5px 0 0 0;">₹153.65</h3>
            <span style="font-size: 12px; color: #8b949e;">(+30 Points)</span>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Progress Bar toward Target
st.markdown("#### 🎯 Target Progress Bar")
current_price = 123.03
buy_price = 123.03
target_price = 153.65
progress = min(max((current_price - buy_price) / (target_price - buy_price), 0.0), 1.0)
st.progress(progress)

st.markdown("---")

# Trade History / Log Table
st.markdown("### 📜 Trade History")
trade_history = pd.DataFrame([
    {"Time": "09:30:12", "Type": "CE", "Buy Price": 123.03, "SL": 93.65, "Target": 153.65, "Status": "Active", "P&L": "₹0.00"},
    {"Time": "10:15:40", "Type": "PE", "Buy Price": 115.50, "SL": 85.50, "Target": 145.50, "Status": "Closed", "P&L": "+₹750.00"}
])
st.dataframe(trade_history, use_container_width=True)
