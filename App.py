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
        padding: 18px 12px;
        border-radius: 10px;
        text-align: center;
        border: 1px solid #30363d;
        min-height: 120px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        box-shadow: inset 0 1px 0 rgba(255,255,255,0.03);
    }
    .price-frame {
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 14px;
        padding: 18px;
        margin: 10px 0 18px 0;
        box-shadow: 0 6px 18px rgba(0, 0, 0, 0.18);
    }
    .price-row {
        display: flex;
        gap: 16px;
        width: 100%;
    }
    .price-card {
        flex: 1 1 0;
        min-width: 0;
        background-color: #21262d;
        border: 1px solid #30363d;
        border-radius: 10px;
        padding: 18px 14px;
        text-align: center;
        min-height: 120px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    .price-label {
        color: #8b949e;
        margin: 0 0 8px 0;
        font-size: 14px;
        letter-spacing: 0.3px;
    }
    .price-value {
        margin: 0;
        font-size: clamp(1.4rem, 2vw, 2.1rem);
        font-weight: 700;
        line-height: 1.2;
    }
    .price-subtext {
        font-size: 12px;
        color: #8b949e;
        margin-top: 8px;
    }
    @media (max-width: 768px) {
        .price-row {
            flex-direction: column;
        }
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
st.markdown("---")

# Signal Card
st.markdown("""
    <div class="card-container">
        <span style="background-color: #1f6feb; color: white; padding: 4px 10px; border-radius: 4px; font-weight: bold; font-size: 12px;">ACTIVE SIGNAL</span>
        <h2 style="color: #3fb950; margin-top: 10px;">BUY 23,050 CE</h2>
        <p style="color: #8b949e;">Nifty 23050 CE: buy @123.00, stop @93.65, target @153.65. Now ₹123.00. 0.00 to target.</p>
    </div>
""", unsafe_allow_html=True)

# Lot Size & Live Market Row
col_lot, col_info = st.columns([1, 3])
with col_lot:
    lot_size = st.number_input("Lot Size", min_value=1, max_value=50, value=1, step=1)
with col_info:
    st.info("💡 **Market Status:** Live feed connected successfully. Ready for execution.")

# Price Breakdown Cards
st.markdown("""
<div class="price-frame">
    <div class="price-row">
        <div class="price-card">
            <p class="price-label">Buying Price</p>
            <h3 class="price-value" style="color: #58a6ff;">₹123.03</h3>
            <span class="price-subtext">LTP: ₹123.03</span>
        </div>
        <div class="price-card">
            <p class="price-label">Stop Loss (SL)</p>
            <h3 class="price-value" style="color: #f85149;">₹93.65</h3>
            <span class="price-subtext">(-30 Points)</span>
        </div>
        <div class="price-card">
            <p class="price-label">Target</p>
            <h3 class="price-value" style="color: #3fb950;">₹153.65</h3>
            <span class="price-subtext">(+30 Points)</span>
        </div>
    </div>
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
