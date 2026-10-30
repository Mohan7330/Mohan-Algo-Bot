import streamlit as st
import pandas as pd
import numpy as np
import time

# Page Setup
st.set_page_config(page_title="Trade Tracker", layout="centered")

# Custom CSS for Mobile Styling
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #1e222d; padding: 10px; border-radius: 8px; }
    .card { background-color: #1e222d; padding: 15px; border-radius: 10px; margin-bottom: 10px; }
    .buy-card { border-left: 5px solid #26a69a; }
    .status-text { font-size: 18px; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

st.title("⚡ Trade Tracker")

# Top Header: Market Signal & Lot Size
with st.container():
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("### 📊 Present Market Signal")
        st.info("💡 **Signal:** Buy **NIFTY 24200 CE** @ **₹145.00**")
    with col2:
        lot_size = st.number_input("Lot Size", min_value=1, max_value=50, value=1, step=1)

st.markdown("---")

# Active Trade Details
st.markdown("### 🎯 Active Trade Monitor")

buy_price = 145.0
sl_price = 115.0  # 30 pts SL
target_price = 175.0  # 30 pts Target
current_price = 162.0  # Simulated Live Price

# Calculate progress towards target
total_range = target_price - buy_price
current_gain = current_price - buy_price
progress_percent = min(max(current_gain / total_range, 0.0), 1.0)
points_to_target = target_price - current_price
rupees_to_target = points_to_target * (lot_size * 25)

col_a, col_b, col_c = st.columns(3)
col_a.metric("Buying Price", f"₹{buy_price}")
col_b.metric("Stop Loss (SL)", f"₹{sl_price}")
col_c.metric("Target", f"₹{target_price}")

# Target Progress Bar
st.markdown(f"**Target Progress:** ({int(progress_percent * 100)}% Reached)")
st.progress(progress_percent)

# Live Status Banner
st.success(f"📈 **Live Market:** Current Price **₹{current_price}** | Target కి ఇంకా **{points_to_target:.1f} Points (₹{rupees_to_target:,.0f})** దూరంలో ఉంది!")

st.markdown("---")

# Trade History Table
st.markdown("### 📜 Trade Log")

trade_data = pd.DataFrame([
    {
        "Buying Time": "09:30 AM",
        "Type": "CE",
        "Buying Price": 145.0,
        "SL": 115.0,
        "Target": 175.0,
        "Profit / Loss": "+₹425.00 (Live)"
    },
    {
        "Buying Time": "10:15 AM",
        "Type": "PE",
        "Buying Price": 120.0,
        "SL": 90.0,
        "Target": 150.0,
        "Profit / Loss": "+₹750.00"
    }
])

st.dataframe(trade_data, use_container_width=True)
