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
    .lot-box {
        width: 126px;
        margin-left: auto;
        border: 1px solid #3fb950;
        border-radius: 8px;
        background: #0b0e14;
        padding: 6px 8px 8px 8px;
    }
    .lot-label {
        font-size: 11px;
        font-weight: 600;
        color: #8b949e;
        text-align: center;
        margin-bottom: 6px;
    }
    .lot-controls {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 8px;
    }
    .lot-value {
        width: 44px;
        text-align: center;
        font-size: 13px;
        font-weight: 600;
        color: white;
        border: 1px solid #3fb950;
        border-radius: 5px;
        padding: 3px 0;
        background: #10151b;
    }
    div[data-testid="stButton"] button {
        width: 24px;
        min-width: 24px;
        height: 24px;
        padding: 0;
        border: 1px solid #3fb950;
        border-radius: 5px;
        color: #3fb950;
        background: #0b0e14;
        font-size: 18px;
        line-height: 1;
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

# Top-right compact lot size box with visible + / - controls
if "lot_size" not in st.session_state:
    st.session_state.lot_size = 1

header_left, header_right = st.columns([5, 1.6])
with header_right:
    st.markdown("<div class='lot-box'>", unsafe_allow_html=True)
    col_label, col_minus, col_value, col_plus = st.columns([1.4, 0.7, 1.0, 0.7])
    with col_label:
        st.markdown("<div class='lot-label'>Lot Size</div>", unsafe_allow_html=True)
    with col_minus:
        if st.button("−", key="lot_minus"):
            st.session_state.lot_size = max(1, st.session_state.lot_size - 1)
    with col_value:
        st.markdown(f"<div class='lot-value'>{st.session_state.lot_size}</div>", unsafe_allow_html=True)
    with col_plus:
        if st.button("+", key="lot_plus"):
            st.session_state.lot_size = min(50, st.session_state.lot_size + 1)
    st.markdown("</div>", unsafe_allow_html=True)

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
    {"Time": "09:30:12", "Type": "CE", "Buy Price": 123.03, "SL": 93.65, "Target": 153.65, "Status": "Active", "P&L": "���0.00"},
    {"Time": "10:15:40", "Type": "PE", "Buy Price": 115.50, "SL": 85.50, "Target": 145.50, "Status": "Closed", "P&L": "+₹750.00"}
])
st.dataframe(trade_history, use_container_width=True)
