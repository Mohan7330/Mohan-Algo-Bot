import streamlit as st
import pandas as pd
import numpy as np

# Page Configuration
st.set_page_config(page_title="Trade Tracker", layout="wide")

# Professional Trading Terminal CSS (Dark Theme & Green Border for Lot Size)
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
        border: 2px solid #238636;
        background-color: #161b22;
        padding: 8px 12px;
        border-radius: 8px;
        display: inline-block;
        float: right;
    }
    </style>
""", unsafe_allow_html=True)

# Top Bar: Toggle Switch (Default ON) on Top-Left & Compact Lot Size on Top-Right
col_tl, col_tr = st.columns([1, 1])

with col_tl:
    # Toggle on top left, default ON
    bot_status = st.toggle("Bot Status", value=True, key="bot_toggle")
    if bot_status:
        st.markdown("<span style='color: #3fb950; font-size: 12px; font-weight: bold;'>🟢 ON (Running)</span>", unsafe_allow_html=True)
    else:
        st.markdown("<span style='color: #f85149; font-size: 12px; font-weight: bold;'>🔴 OFF (Paused)</span>", unsafe_allow_html=True)

with col_tr:
    if 'lot_size' not in st.session_state:
        st.session_state.lot_size = 65
    
    # Compact Lot Box with Green Outline on Top-Right
    st.markdown("<div style='text-align: right;'>", unsafe_allow_html=True)
    st.markdown("<span style='font-size: 12px; color: #8b949e; margin-right: 5px;'>Lot Size:</span>", unsafe_allow_html=True)
    
    lc1, lc2, lc3 = st.columns([1, 1, 1])
    # To keep it compact on the right, we align columns
    with st.container():
        sub_c1, sub_c2, sub_c3, sub_c4 = st.columns([2, 1, 1, 1])
        with sub_c1:
            st.markdown("") # spacing
        with sub_c2:
            if st.button("➖", key="m_btn"):
                if st.session_state.lot_size > 1:
                    st.session_state.lot_size -= 1
                    st.rerun()
        with sub_c3:
            st.markdown(f"<div style='background: #21262d; padding: 4px; border-radius: 4px; text-align: center; color: white; font-weight: bold; border: 2px solid #238636; font-size: 13px;'>{st.session_state.lot_size}</div>", unsafe_allow_html=True)
        with sub_c4:
            if st.button("➕", key="p_btn"):
                st.session_state.lot_size += 1
                st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("---")

# Main Header
st.markdown("## 📊 Nifty Options - Live Terminal")

# Active Signal Card
st.markdown("""
    <div class="card-container">
        <span style="background-color: #1f6feb; color: white; padding: 4px 10px; border-radius: 4px; font-weight: bold; font-size: 12px;">ACTIVE SIGNAL</span>
        <h2 style="color: #3fb950; margin-top: 10px;">BUY 23,050 CE</h2>
        <p style="color: #8b949e;">Nifty 23050 CE: buy @123.00, stop @93.65, target @153.65. Now ₹123.00. 0.00 to target.</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# Price Breakdown Cards (Buying Price, Stop Loss, Target)
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

# Target Progress Bar
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
