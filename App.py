import streamlit as st
import pandas as pd
import numpy as np

# Page Configuration for MTrade Mobile Trading App
st.set_page_config(page_title="MTrade", layout="centered")

# Custom CSS matching your mobile application layout
st.markdown("""
    <style>
    .main { background-color: #0b0e14; color: #ffffff; font-family: sans-serif; }
    .top-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: #12161c;
        padding: 10px 15px;
        border-radius: 8px;
        border: 1px solid #30363d;
        margin-bottom: 10px;
    }
    .card-box {
        background-color: #161b22;
        border: 1px solid #30363d;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 15px;
    }
    .metric-card {
        background-color: #21262d;
        padding: 10px;
        border-radius: 6px;
        text-align: center;
        border: 1px solid #30363d;
    }
    .stat-badge {
        background-color: #21262d;
        padding: 8px 12px;
        border-radius: 6px;
        border: 1px solid #30363d;
        text-align: center;
        font-size: 13px;
    }
    </style>
""", unsafe_allow_html=True)

# 1. Top Header Bar (MTrade branding & live status)
st.markdown("""
    <div class="top-header">
        <div style="font-weight: bold; font-size: 18px; color: #58a6ff;">⚡ MTrade</div>
        <div style="font-size: 11px; color: #8b949e;">
            <span style="color: #3fb950;">●</span> Live prices &nbsp;|&nbsp; <span style="color: #3fb950;">●</span> mStock live
        </div>
    </div>
""", unsafe_allow_html=True)

# News ticker simulation
st.markdown("""
    <div style="background-color: #1a1f29; padding: 6px 10px; border-radius: 4px; font-size: 11px; color: #e1dfdd; margin-bottom: 15px; border-left: 3px solid #d29922;">
        <b>NEWS:</b> RBI monetary policy meeting chaired by Governor...
    </div>
""", unsafe_allow_html=True)

# 2. Nifty Option Live & Controls Row
st.markdown("<b>Nifty option &nbsp;<span style='background-color: #238636; color: white; padding: 2px 6px; border-radius: 4px; font-size: 10px;'>LIVE</span></b>", unsafe_allow_html=True)
st.markdown("<p style='font-size: 11px; color: #8b949e; margin-bottom: 5px;'>21:54:25 IST</p>", unsafe_allow_html=True)

c1, c2, c3, c4, c5 = st.columns([1, 1.5, 1, 1.8, 1.5])

if 'lot_count' not in st.session_state:
    st.session_state.lot_count = 1

with c1:
    if st.button("-", key="m_lot"):
        if st.session_state.lot_count > 1:
            st.session_state.lot_count -= 1
            st.rerun()
with c2:
    st.markdown(f"<div style='background: #21262d; padding: 6px; text-align: center; border-radius: 4px; border: 1px solid #30363d; font-size: 12px; font-weight: bold;'>{st.session_state.lot_count} lot</div>", unsafe_allow_html=True)
with c3:
    if st.button("+", key="p_lot"):
        st.session_state.lot_count += 1
        st.rerun()
with c4:
    if st.button("Orders off", use_container_width=True):
        st.toast("Orders status toggled!")
with c5:
    if st.button("Refresh", use_container_width=True):
        st.rerun()

st.markdown("<p style='font-size: 11px; color: #8b949e; margin-top: 5px;'>Orders are off. An open position is sold at the market. Signals continue.</p>", unsafe_allow_html=True)
st.markdown("---")

# 3. Active Signal Card (SOLD 23,050 CE view)
st.markdown("""
    <div class="card-box">
        <span style="background-color: #6e7681; color: white; padding: 3px 8px; border-radius: 4px; font-weight: bold; font-size: 11px;">SOLD</span>
        <h2 style="color: #ffffff; margin-top: 8px; margin-bottom: 5px;">SOLD 23,050 CE</h2>
        
        <div style="display: flex; gap: 20px; margin-bottom: 12px; font-size: 12px;">
            <div>Score<br><b style="font-size: 15px;">73/100</b></div>
            <div>Confidence<br><b style="font-size: 15px;">4/5 ⭐⭐⭐⭐⭐</b></div>
            <div>Held up<br><b style="font-size: 15px; color: #58a6ff;">385:50</b></div>
        </div>

        <div style="margin-bottom: 12px;">
            <span style="background-color: #238636; color: white; padding: 2px 6px; border-radius: 4px; font-size: 10px;">technical 100</span>
            <span style="background-color: #da3633; color: white; padding: 2px 6px; border-radius: 4px; font-size: 10px;">OI/PCR 35</span>
            <span style="background-color: #6e7681; color: white; padding: 2px 6px; border-radius: 4px; font-size: 10px;">news 50</span>
        </div>

        <p style="font-size: 12px; color: #c9d1d9; line-height: 1.4;">
            23050 CE sold at ₹109.55. Buy was ₹123.65. The session is over, so this option is not carried to the next day.
        </p>
    </div>
""", unsafe_allow_html=True)

# Three metrics at bottom of card (Buy, Sell stop, Sell target)
col_m1, col_m2, col_m3 = st.columns(3)
with col_m1:
    st.markdown("""
        <div class="metric-card">
            <span style="font-size: 10px; color: #8b949e;">Buy</span><br>
            <b style="font-size: 14px; color: #58a6ff;">₹123.65</b><br>
            <span style="font-size: 9px; color: #8b949e;">now ₹109.55</span>
        </div>
    """, unsafe_allow_html=True)
with col_m2:
    st.markdown("""
        <div class="metric-card">
            <span style="font-size: 10px; color: #8b949e;">Sell stop</span><br>
            <b style="font-size: 14px; color: #f85149;">₹93.65</b>
        </div>
    """, unsafe_allow_html=True)
with col_m3:
    st.markdown("""
        <div class="metric-card">
            <span style="font-size: 10px; color: #8b949e;">Sell target</span><br>
            <b style="font-size: 14px; color: #3fb950;">₹153.65</b>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 4. Signal Log Summary Section
st.markdown("### Signal log")
st.markdown("""
    <div style="display: flex; gap: 10px; flex-wrap: wrap; margin-bottom: 12px; font-size: 12px;">
        <div class="stat-badge">TAKEN <b>181</b></div>
        <div class="stat-badge">TARGET <b>56</b></div>
        <div class="stat-badge">STOP <b>103</b></div>
        <div class="stat-badge">WIN RATE <b>35.2%</b></div>
    </div>
    <div style="font-size: 16px; font-weight: bold; color: #3fb950; margin-bottom: 15px;">
        P&L +₹33,880
    </div>
""", unsafe_allow_html=True)

# 5. Full Signal Log Table
signal_log_data = [
    {"BUY TIME": "30 Oct, 14:40", "CONTRACT": "23050 CE", "SCORE": 70, "BUY": "₹123.65", "STOP": "₹93.65", "TARGET": "₹153.65"},
    {"BUY TIME": "30 Oct, 14:00", "CONTRACT": "23000 PE", "SCORE": 22, "BUY": "₹129.20", "STOP": "₹99.20", "TARGET": "₹159.20"},
    {"BUY TIME": "30 Oct, 11:58", "CONTRACT": "23100 CE", "SCORE": 69, "BUY": "₹127.95", "STOP": "₹97.95", "TARGET": "₹157.95"},
    {"BUY TIME": "30 Oct, 11:57", "CONTRACT": "23100 CE", "SCORE": 69, "BUY": "₹112.95", "STOP": "₹127.95", "TARGET": "₹142.95"},
    {"BUY TIME": "30 Oct, 11:49", "CONTRACT": "23050 CE", "SCORE": 70, "BUY": "₹127.00", "STOP": "₹142.00", "TARGET": "₹157.00"},
    {"BUY TIME": "30 Oct, 11:20", "CONTRACT": "23050 CE", "SCORE": 68, "BUY": "₹111.10", "STOP": "₹127.60", "TARGET": "₹141.10"},
    {"BUY TIME": "30 Oct, 11:15", "CONTRACT": "23000 CE", "SCORE": 71, "BUY": "₹124.65", "STOP": "₹139.65", "TARGET": "₹154.65"},
    {"BUY TIME": "30 Oct, 10:20", "CONTRACT": "22950 PE", "SCORE": 29, "BUY": "₹159.35", "STOP": "₹126.35", "TARGET": "₹190.35"}
]

df_signal = pd.DataFrame(signal_log_data)
st.dataframe(df_signal, use_container_width=True)
