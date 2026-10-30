import streamlit as st
import pandas as pd
import numpy as np

# Page Configuration
st.set_page_config(page_title="Trade Tracker", layout="wide")

# Professional Trading Terminal CSS (Exact Match to Reference Layout)
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
    /* Force horizontal layout for top bar */
    [data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        align-items: center !important;
    }
    </style>
""", unsafe_allow_html=True)

# Top Bar: Bot Status on Left & 1 lot on Right (Matching Reference Image)
col_top1, col_top2 = st.columns([1, 1])

with col_top1:
    bot_status = st.toggle("Bot Status", value=True, key="bot_toggle")
    if bot_status:
        st.markdown("<span style='color: #3fb950; font-size: 13px; font-weight: bold;'>🟢 ACTIVE</span>", unsafe_allow_html=True)
    else:
        st.markdown("<span style='color: #f85149; font-size: 13px; font-weight: bold;'>🔴 PAUSED</span>", unsafe_allow_html=True)

with col_top2:
    if 'lot_size' not in st.session_state:
        st.session_state.lot_size = 1
    
    # Exact 1 lot display on top right like reference photo
    st.markdown(f"""
        <div style="text-align: right; padding-top: 5px;">
            <span style="background-color: #21262d; border: 1px solid #30363d; padding: 6px 14px; border-radius: 6px; font-size: 13px; font-weight: bold; color: #58a6ff;">
                {st.session_state.lot_size} lot
            </span>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Active Signal Section (Matching Reference Style)
st.markdown("""
    <div class="card-container">
        <span style="background-color: #1f6feb; color: white; padding: 4px 10px; border-radius: 4px; font-weight: bold; font-size: 12px;">ACTIVE SIGNAL</span>
        <h2 style="color: #3fb950; margin-top: 10px;">BUY 23,050 CE</h2>
        <p style="color: #8b949e; margin-bottom: 0;">Nifty 23050 CE: buy @123.00, stop @93.65, target @153.65. Now ₹123.00. 0.00 to target.</p>
    </div>
""", unsafe_allow_html=True)

# Active Trade Monitor Metrics
st.markdown("### Active Trade Monitor")
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
        <div class="metric-box">
            <p style="color: #8b949e; margin: 0; font-size: 12px;">Buying Price</p>
            <h4 style="color: #58a6ff; margin: 5px 0 0 0;">₹123.03</h4>
            <span style="font-size: 11px; color: #8b949e;">LTP: ₹123.03</span>
        </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
        <div class="metric-box">
            <p style="color: #8b949e; margin: 0; font-size: 12px;">Stop Loss</p>
            <h4 style="color: #f85149; margin: 5px 0 0 0;">₹93.65</h4>
            <span style="font-size: 11px; color: #8b949e;">(-30 Points)</span>
        </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
        <div class="metric-box">
            <p style="color: #8b949e; margin: 0; font-size: 12px;">Target</p>
            <h4 style="color: #3fb950; margin: 5px 0 0 0;">₹153.65</h4>
            <span style="font-size: 11px; color: #8b949e;">(+30 Points)</span>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Target Progress Bar & Live Info
st.markdown("<b>Target Progress</b>", unsafe_allow_html=True)
current_price = 123.03
buy_price = 123.03
target_price = 153.65

progress_percent = min(max((current_price - buy_price) / (target_price - buy_price), 0.0), 1.0)
st.progress(progress_percent)

points_diff = target_price - current_price
rupees_diff = points_diff * (st.session_state.lot_size * 25)

st.markdown(f"""
    <div style="background-color: #161b22; border-left: 4px solid #3fb950; padding: 12px; border-radius: 6px; margin-top: 10px;">
        <p style="color: #c9d1d9; margin: 0; font-size: 13px;">
            Live Market LTP: <b>₹{current_price}</b> | Distance to Target: <b>{points_diff:.2f} Points</b> (₹{rupees_diff:,.2f})
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
        "Buy Price": "₹123.03",
        "SL": "₹93.65",
        "Target": "₹153.65",
        "Exit Price": "₹153.65",
        "Exit Time & Points": "11:15 AM (23,120.50)",
        "Result": "TARGET",
        "P&L": "+₹743.75"
    },
    {
        "Date & Time": "2026-10-30 11:30 AM",
        "Signal": "NIFTY 22950 PE",
        "Score": "42 / 5",
        "Entry Points": "22,955.10",
        "Buy Price": "₹115.50",
        "SL": "₹85.50",
        "Target": "₹145.50",
        "Exit Price": "₹85.50",
        "Exit Time & Points": "12:05 PM (22,910.00)",
        "Result": "STOP HIT",
        "P&L": "-₹750.00"
    },
    {
        "Date & Time": "2026-10-30 01:10 PM",
        "Signal": "NIFTY 23000 CE",
        "Score": "48 / 5",
        "Entry Points": "23,010.50",
        "Buy Price": "₹126.40",
        "SL": "₹96.40",
        "Target": "₹156.40",
        "Exit Price": "₹126.40 (Live)",
        "Exit Time & Points": "Running",
        "Result": "ACTIVE",
        "P&L": "₹0.00 (Live)"
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
