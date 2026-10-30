import streamlit as st
import pandas as pd
import numpy as np

# Page Configuration
st.set_page_config(page_title="Trade Tracker", layout="wide")

# Professional Trading Terminal CSS (Force Horizontal Layout for Lot Size on Mobile)
st.markdown("""
    <style>
    .main { background-color: #0b0e14; color: #ffffff; }
    .card-container {
        background-color: #161b22;
        border: 1px solid #30363d;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 15px;
    }
    .metric-box {
        background-color: #21262d;
        padding: 15px;
        border-radius: 8px;
        text-align: center;
        border: 1px solid #30363d;
    }
    /* Force columns to strictly stay horizontal on mobile */
    [data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
    }
    [data-testid="column"] {
        width: auto !important;
        flex: 1 !important;
        min-width: unset !important;
    }
    .stButton > button {
        background-color: #21262d;
        color: white;
        border: 1px solid #30363d;
        border-radius: 4px;
        padding: 2px 6px;
        font-weight: bold;
        min-height: 32px;
    }
    .stButton > button:hover {
        background-color: #30363d;
        border-color: #58a6ff;
    }
    </style>
""", unsafe_allow_html=True)

# Top Bar: Bot Status (ON/OFF) on Top-Left & Lot Size on Top-Right
col_top1, col_top2 = st.columns([1, 1])

with col_top1:
    bot_status = st.toggle("Bot Status", value=True, key="bot_toggle")
    if bot_status:
        st.markdown("<span style='color: #3fb950; font-size: 14px; font-weight: bold;'>🟢 ACTIVE</span>", unsafe_allow_html=True)
    else:
        st.markdown("<span style='color: #f85149; font-size: 14px; font-weight: bold;'>🔴 PAUSED</span>", unsafe_allow_html=True)

with col_top2:
    if 'lot_size' not in st.session_state:
        st.session_state.lot_size = 65
    
    # Lot Size label matching Bot Status font size, positioned on top-right
    st.markdown("<div style='text-align: right;'><span style='font-size: 14px; font-weight: bold; color: #ffffff;'>Lot Size</span></div>", unsafe_allow_html=True)
    
    # Compact inline horizontal controls: [-] [ 65 ] [+]
    c_minus, c_num, c_plus = st.columns([1, 1.2, 1])
    with c_minus:
        if st.button("-", key="m_btn", use_container_width=True):
            if st.session_state.lot_size > 1:
                st.session_state.lot_size -= 1
                st.rerun()
    with c_num:
        st.markdown(f"<div style='background: #21262d; padding: 4px 2px; border-radius: 4px; text-align: center; color: white; font-weight: bold; border: 2px solid #238636; font-size: 13px; margin-top: 2px;'>{st.session_state.lot_size}</div>", unsafe_allow_html=True)
    with c_plus:
        if st.button("+", key="p_btn", use_container_width=True):
            st.session_state.lot_size += 1
            st.rerun()

st.markdown("---")

# Active Signal Section
st.markdown("""
    <div class="card-container">
        <span style="background-color: #1f6feb; color: white; padding: 4px 10px; border-radius: 4px; font-weight: bold; font-size: 12px;">ACTIVE SIGNAL</span>
        <h2 style="color: #3fb950; margin-top: 10px;">BUY NIFTY 23,050 CE</h2>
        <p style="color: #8b949e; margin-bottom: 0;">Execution Price: <b>₹123.00</b> | Score: <b>45 / 5</b></p>
    </div>
""", unsafe_allow_html=True)

# Active Trade Monitor Metrics
st.markdown("### Active Trade Monitor")
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
        <div class="metric-box">
            <p style="color: #8b949e; margin: 0; font-size: 12px;">Buying Price</p>
            <h4 style="color: #58a6ff; margin: 5px 0 0 0;">₹123.00</h4>
        </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
        <div class="metric-box">
            <p style="color: #8b949e; margin: 0; font-size: 12px;">Stop Loss</p>
            <h4 style="color: #f85149; margin: 5px 0 0 0;">₹93.00</h4>
        </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
        <div class="metric-box">
            <p style="color: #8b949e; margin: 0; font-size: 12px;">Target</p>
            <h4 style="color: #3fb950; margin: 5px 0 0 0;">₹153.00</h4>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Target Progress Bar & Live Info
st.markdown("<b>Target Progress</b>", unsafe_allow_html=True)
current_price = 138.00
buy_price = 123.00
target_price = 153.00

progress_percent = min(max((current_price - buy_price) / (target_price - buy_price), 0.0), 1.0)
st.progress(progress_percent)

points_diff = target_price - current_price
rupees_diff = points_diff * (st.session_state.lot_size * 25)

st.markdown(f"""
    <div style="background-color: #161b22; border-left: 4px solid #3fb950; padding: 12px; border-radius: 6px; margin-top: 10px;">
        <p style="color: #c9d1d9; margin: 0; font-size: 13px;">
            Live Market LTP: <b>₹{current_price}</b> | Distance to Target: <b>{points_diff:.1f} Points</b> (₹{rupees_diff:,.0f})
        </p>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# Full-Fledged Trade Log Table with Colored Status and P&L
st.markdown("### Trade Log & History")

trade_data = [
    {
        "Date & Time": "2026-10-30 09:30 AM",
        "Signal": "NIFTY 23050 CE",
        "Score": "45 / 5",
        "Entry Points": "23,045.20",
        "Buy Price": "₹123.00",
        "SL": "₹93.00",
        "Target": "₹153.00",
        "Exit Price": "₹153.00",
        "Exit Time & Points": "11:15 AM (23,120.50)",
        "Result": "TARGET",
        "P&L": "+₹975.00"
    },
    {
        "Date & Time": "2026-10-30 11:30 AM",
        "Signal": "NIFTY 22950 PE",
        "Score": "42 / 5",
        "Entry Points": "22,955.10",
        "Buy Price": "₹115.00",
        "SL": "₹85.00",
        "Target": "₹145.00",
        "Exit Price": "₹85.00",
        "Exit Time & Points": "12:05 PM (22,910.00)",
        "Result": "STOP HIT",
        "P&L": "-₹750.00"
    },
    {
        "Date & Time": "2026-10-30 01:10 PM",
        "Signal": "NIFTY 23000 CE",
        "Score": "48 / 5",
        "Entry Points": "23,010.50",
        "Buy Price": "₹128.00",
        "SL": "₹98.00",
        "Target": "₹158.00",
        "Exit Price": "₹138.00 (Live)",
        "Exit Time & Points": "Running",
        "Result": "ACTIVE",
        "P&L": "+₹650.00 (Live)"
    }
]

df_trades = pd.DataFrame(trade_data)

def highlight_results(row):
    color = [''] * len(row)
    if row['Result'] == 'TARGET':
        return ['background-color: rgba(35, 134, 54, 0.2); color: #3fb950; font-weight: bold;' if col == 'Result' else '' for col in row.index]
    elif row['Result'] == 'STOP HIT':
        return ['background-color: rgba(248, 81, 73, 0.2); color: #f85149; font-weight: bold;' if col == 'Result' else '' for col in row.index]
    elif row['Result'] == 'ACTIVE':
        return ['background-color: rgba(31, 111, 235, 0.2); color: #58a6ff; font-weight: bold;' if col == 'Result' else '' for col in row.index]
    return color

st.dataframe(df_trades.style.apply(highlight_results, axis=1), use_container_width=True)
