import streamlit as st
import pandas as pd
import numpy as np

# Page Configuration
st.set_page_config(page_title="Trade Tracker", layout="centered")

# Custom CSS for exact sketch layout (Dark Terminal Theme)
st.markdown("""
    <style>
    .main { background-color: #0b0e14; color: #ffffff; }
    .top-card {
        background-color: #161b22;
        border: 1px solid #30363d;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 15px;
    }
    .metric-card {
        background-color: #21262d;
        padding: 12px;
        border-radius: 8px;
        text-align: center;
        border: 1px solid #30363d;
    }
    </style>
""", unsafe_allow_html=True)

# 1. Top Header: Bot Status & Lot Size (Right Side)
col_top1, col_top2 = st.columns([2, 1])

with col_top1:
    bot_status = st.toggle("Bot Status", value=True, key="bot_toggle")
    if bot_status:
        st.markdown("<span style='color: #3fb950; font-size: 12px; font-weight: bold;'>🟢 ON (Running)</span>", unsafe_allow_html=True)
    else:
        st.markdown("<span style='color: #f85149; font-size: 12px; font-weight: bold;'>🔴 OFF (Paused)</span>", unsafe_allow_html=True)

with col_top2:
    if 'lot_size' not in st.session_state:
        st.session_state.lot_size = 65
    
    st.markdown("<p style='font-size: 11px; margin-bottom: 2px; color: #8b949e; text-align: right;'>Lot Size</p>", unsafe_allow_html=True)
    lc1, lc2, lc3 = st.columns([1, 1, 1])
    with lc1:
        if st.button("➖", key="m_btn"):
            if st.session_state.lot_size > 1:
                st.session_state.lot_size -= 1
                st.rerun()
    with lc2:
        st.markdown(f"<div style='background: #21262d; padding: 3px; border-radius: 4px; text-align: center; color: white; font-weight: bold; border: 2px solid #238636; font-size: 12px;'>{st.session_state.lot_size}</div>", unsafe_allow_html=True)
    with lc3:
        if st.button("➕", key="p_btn"):
            st.session_state.lot_size += 1
            st.rerun()

st.markdown("---")

# 2. Present Market Signal Section (As per your sketch text)
st.markdown("""
    <div class="top-card">
        <p style='color: #8b949e; font-size: 13px; margin-bottom: 5px;'>Present market PE లేదా CE ఏది చెప్పాలి</p>
        <h3 style='color: #58a6ff; margin: 0 0 10px 0;'>💡 Signal: BUY NIFTY 23,050 CE</h3>
        <p style='color: #3fb950; font-size: 14px; margin: 0;'>👉 ఇక్కడ ఎంత price కు buy చేయాలో PE న లో CE నో చెప్పాలి (@ ₹123.00)</p>
    </div>
""", unsafe_allow_html=True)

# 3. Buying Price, SL, Target Section
st.markdown("### 🎯 Active Trade Monitor")
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
        <div class="metric-card">
            <p style="color: #8b949e; margin: 0; font-size: 12px;">Buying Price</p>
            <h4 style="color: #58a6ff; margin: 5px 0 0 0;">₹123.00</h4>
        </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
        <div class="metric-card">
            <p style="color: #8b949e; margin: 0; font-size: 12px;">SL</p>
            <h4 style="color: #f85149; margin: 5px 0 0 0;">₹93.00</h4>
        </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
        <div class="metric-card">
            <p style="color: #8b949e; margin: 0; font-size: 12px;">Target</p>
            <h4 style="color: #3fb950; margin: 5px 0 0 0;">₹153.00</h4>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 4. Progress Bar & Live Market Points Info (As written in your sketch)
st.markdown("<b>Target Progress</b>", unsafe_allow_html=True)
current_price = 138.00  # Example live price moving towards target
buy_price = 123.00
target_price = 153.00

progress_percent = min(max((current_price - buy_price) / (target_price - buy_price), 0.0), 1.0)
st.progress(progress_percent)

# Sketch text logic: "ఈ బార్‌లో target కి దగ్గర అవుతుంటే green లో వెళ్తూ ఉండాలి."
# "లైవ్ మార్కెట్ పాయింట్లు, మన Target కి ఎన్ని రూపాయల difference లో ఉంది అని Live లో చూపించాలి"
points_diff = target_price - current_price
rupees_diff = points_diff * (st.session_state.lot_size * 25)

st.markdown(f"""
    <div style="background-color: #161b22; border-left: 4px solid #3fb950; padding: 12px; border-radius: 6px; margin-top: 10px;">
        <p style="color: #c9d1d9; margin: 0; font-size: 13px;">
            🌿 <b>ఈ బార్‌లో target కి దగ్గర అవుతుంటే green లో వెళ్తుంది.</b><br>
            📈 Live Market points: <b>₹{current_price}</b> | Target కి ఇంకా <b>{points_diff:.1f} Points</b> (రూ.<b>{rupees_diff:,.0f}</b> difference) దూరంలో ఉంది.
        </p>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# 5. Bottom Table: Trade History (Buying Time, price, SL, Target, profit or loss)
st.markdown("### 📜 Trade Log")

trade_log_data = pd.DataFrame([
    {
        "Buying Time": "09:30 AM",
        "price": 123.00,
        "SL": 93.00,
        "Target": 153.00,
        "profit or loss": "+₹975.00 (Live)"
    },
    {
        "Buying Time": "10:15 AM",
        "price": 115.00,
        "SL": 85.00,
        "Target": 145.00,
        "profit or loss": "+₹750.00"
    }
])

st.dataframe(trade_log_data, use_container_width=True)
