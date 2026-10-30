import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="MTrade",
    page_icon="⚡",
    layout="centered"
)

# Session state initialization
if "lot_count" not in st.session_state:
    st.session_state.lot_count = 1

if "orders_on" not in st.session_state:
    st.session_state.orders_on = False

# Custom CSS with strict flexbox alignment for mobile/desktop
st.markdown(
    """
    <style>
    .app-shell {
        background: #0b0e14;
        padding: 0 0 24px 0;
        color: #f0f6fc;
    }
    .topbar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        background: linear-gradient(180deg, #151b24 0%, #10161e 100%);
        border: 1px solid #2d3743;
        border-radius: 12px;
        padding: 12px 14px;
        margin-bottom: 12px;
    }
    .brand {
        font-size: 18px;
        font-weight: 800;
        color: #58a6ff;
    }
    .status {
        font-size: 11px;
        color: #8b949e;
    }
    .status-dot {
        color: #3fb950;
        font-weight: bold;
    }
    .news {
        background: #171d27;
        border-left: 3px solid #d29922;
        border-radius: 8px;
        padding: 8px 10px;
        color: #e1dfdd;
        font-size: 11px;
        margin-bottom: 14px;
    }
    .panel-card {
        background: linear-gradient(180deg, #171d26 0%, #121820 100%);
        border: 1px solid #2d3743;
        border-radius: 14px;
        padding: 12px;
        margin-bottom: 16px;
    }
    .panel-head {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 4px;
    }
    .panel-title {
        color: #f0f6fc;
        font-size: 14px;
        font-weight: 700;
    }
    .live-pill {
        background: #238636;
        color: white;
        font-size: 9px;
        font-weight: 700;
        padding: 3px 7px;
        border-radius: 6px;
    }
    .time {
        color: #8b949e;
        font-size: 10px;
        margin-bottom: 10px;
    }
    /* Custom Inline Control Bar matching friend's app perfectly */
    .control-row {
        display: flex;
        align-items: center;
        gap: 6px;
        width: 100%;
        margin-bottom: 8px;
    }
    .signal-card {
        background: #161b22;
        border: 1px solid #30363d;
        padding: 16px 14px;
        border-radius: 12px;
        margin-bottom: 16px;
    }
    .signal-tag {
        display: inline-block;
        background: #6e7681;
        color: white;
        padding: 3px 8px;
        border-radius: 5px;
        font-weight: 700;
        font-size: 11px;
    }
    .signal-title {
        color: white;
        font-size: 22px;
        font-weight: 800;
        margin: 10px 0 8px 0;
    }
    .mini-grid {
        display: flex;
        gap: 18px;
        margin-bottom: 12px;
        font-size: 12px;
    }
    .mini-label {
        color: #8b949e;
        font-size: 10px;
    }
    .mini-value {
        font-size: 15px;
        font-weight: 700;
        color: white;
    }
    .chip-row {
        display: flex;
        gap: 7px;
        flex-wrap: wrap;
        margin-bottom: 12px;
    }
    .chip {
        padding: 3px 7px;
        border-radius: 5px;
        font-size: 10px;
        font-weight: 700;
        color: white;
    }
    .chip-green { background: #238636; }
    .chip-red { background: #da3633; }
    .chip-gray { background: #6e7681; }
    .metric-card {
        background: #21262d;
        padding: 10px;
        border-radius: 8px;
        text-align: center;
        border: 1px solid #30363d;
    }
    .metric-label {
        color: #8b949e;
        font-size: 10px;
    }
    .stat-badge {
        background-color: #21262d;
        padding: 8px 12px;
        border-radius: 6px;
        border: 1px solid #30363d;
        text-align: center;
        font-size: 12px;
        color: #e6edf3;
        font-weight: 600;
    }
    .table-wrap {
        background: #0d1117;
        border: 1px solid #30363d;
        border-radius: 10px;
        padding: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="app-shell">', unsafe_allow_html=True)

# Top Header
st.markdown(
    """
    <div class="topbar">
        <div class="brand">⚡ MTrade</div>
        <div class="status">
            <span class="status-dot">●</span> Live prices &nbsp;|&nbsp;
            <span class="status-dot">●</span> mStock live
        </div>
    </div>
    <div class="news">
        <b>NEWS:</b> RBI monetary policy meeting chaired by Governor...
    </div>
    """,
    unsafe_allow_html=True
)

# Trading control panel card
st.markdown('<div class="panel-card">', unsafe_allow_html=True)
st.markdown(
    """
    <div class="panel-head">
        <div class="panel-title">Nifty option</div>
        <span class="live-pill">LIVE</span>
    </div>
    <div class="time">21:54:25 IST</div>
    """,
    unsafe_allow_html=True
)

# Inline control row matching friend's app layout precisely
col1, col2, col3, col4, col5 = st.columns([0.6, 1.2, 0.6, 1.6, 1.4])

with col1:
    if st.button("-", key="m_lot", use_container_width=True):
        if st.session_state.lot_count > 1:
            st.session_state.lot_count -= 1
            st.rerun()

with col2:
    st.markdown(
        f'<div style="background: #1d2430; border: 1px solid #3a4657; border-radius: 6px; color: #f0f6fc; font-size: 12px; font-weight: 700; text-align: center; padding: 7px 4px;">{st.session_state.lot_count} lot</div>',
        unsafe_allow_html=True
    )

with col3:
    if st.button("+", key="p_lot", use_container_width=True):
        st.session_state.lot_count += 1
        st.rerun()

with col4:
    btn_label = "Orders on" if st.session_state.orders_on else "Orders off"
    if st.button(btn_label, key="ord_toggle", use_container_width=True):
        st.session_state.orders_on = not st.session_state.orders_on
        st.rerun()

with col5:
    if st.button("Refresh", key="ref_btn", use_container_width=True):
        st.rerun()

status_msg = (
    "Orders are ON. An open position is active and the market is live."
    if st.session_state.orders_on
    else "Orders are off. An open position is sold at the market. Signals continue."
)
st.markdown(f'<div style="font-size: 11px; color: #8b949e; margin-top: 8px;">{status_msg}</div>', unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Signal Card
st.markdown(
    """
    <div class="signal-card">
        <span class="signal-tag">SOLD</span>
        <div class="signal-title">SOLD 23,050 CE</div>

        <div class="mini-grid">
            <div>
                <div class="mini-label">Score</div>
                <div class="mini-value">73/100</div>
            </div>
            <div>
                <div class="mini-label">Confidence</div>
                <div class="mini-value">4/5 ⭐⭐⭐⭐⭐</div>
            </div>
            <div>
                <div class="mini-label">Held up</div>
                <div class="mini-value" style="color: #58a6ff;">385:50</div>
            </div>
        </div>

        <div class="chip-row">
            <span class="chip chip-green">technical 100</span>
            <span class="chip chip-red">OI/PCR 35</span>
            <span class="chip chip-gray">news 50</span>
        </div>

        <div style="color: #c9d1d9; font-size: 12px; line-height: 1.4;">
            23050 CE sold at ₹109.55. Buy was ₹123.65. The session is over, so this option is not carried to the next day.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Metric cards
m1, m2, m3 = st.columns(3)
with m1:
    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-label">Buy</div>
            <span style="font-size: 14px; font-weight: 700; color: #58a6ff; display: block; margin-top: 4px;">₹123.65</span>
            <div class="metric-label" style="margin-top: 4px;">now ₹109.55</div>
        </div>
        """,
        unsafe_allow_html=True
    )
with m2:
    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-label">Sell stop</div>
            <span style="font-size: 14px; font-weight: 700; color: #f85149; display: block; margin-top: 4px;">₹93.65</span>
        </div>
        """,
        unsafe_allow_html=True
    )
with m3:
    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-label">Sell target</div>
            <span style="font-size: 14px; font-weight: 700; color: #3fb950; display: block; margin-top: 4px;">₹153.65</span>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("<br>", unsafe_allow_html=True)

# Signal log summary
st.markdown('<div style="color: white; font-size: 16px; font-weight: 700; margin-bottom: 10px;">Signal log</div>', unsafe_allow_html=True)

s1, s2, s3, s4 = st.columns(4)
with s1:
    st.markdown('<div class="stat-badge">TAKEN <b>181</b></div>', unsafe_allow_html=True)
with s2:
    st.markdown('<div class="stat-badge">TARGET <b>56</b></div>', unsafe_allow_html=True)
with s3:
    st.markdown('<div class="stat-badge">STOP <b>103</b></div>', unsafe_allow_html=True)
with s4:
    st.markdown('<div class="stat-badge">WIN RATE <b>35.2%</b></div>', unsafe_allow_html=True)

st.markdown(
    '<div style="font-size: 16px; font-weight: bold; color: #3fb950; margin: 12px 0;">P&L +₹33,880</div>',
    unsafe_allow_html=True
)

# Signal log table
signal_log_data = [
    {"BUY TIME": "30 Oct, 14:40", "CONTRACT": "23050 CE", "SCORE": 70, "BUY": "₹123.65", "STOP": "₹93.65", "TARGET": "₹153.65"},
    {"BUY TIME": "30 Oct, 14:00", "CONTRACT": "23000 PE", "SCORE": 22, "BUY": "₹129.20", "STOP": "₹99.20", "TARGET": "₹159.20"},
    {"BUY TIME": "30 Oct, 11:58", "CONTRACT": "23100 CE", "SCORE": 69, "BUY": "₹127.95", "STOP": "₹97.95", "TARGET": "₹157.95"},
    {"BUY TIME": "30 Oct, 11:57", "CONTRACT": "23100 CE", "SCORE": 69, "BUY": "₹112.95", "STOP": "₹127.95", "TARGET": "₹142.95"},
    {"BUY TIME": "30 Oct, 11:49", "CONTRACT": "23050 CE", "SCORE": 70, "BUY": "₹127.00", "STOP": "₹142.00", "TARGET": "₹157.00"},
    {"BUY TIME": "30 Oct, 11:20", "CONTRACT": "23050 CE", "SCORE": 68, "BUY": "₹111.10", "STOP": "₹127.60", "TARGET": "₹141.10"},
    {"BUY TIME": "30 Oct, 11:15", "CONTRACT": "23000 CE", "SCORE": 71, "BUY": "₹124.65", "STOP": "₹139.65", "TARGET": "₹154.65"},
    {"BUY TIME": "30 Oct, 10:20", "CONTRACT": "22950 PE", "SCORE": 29, "BUY": "₹159.35", "STOP": "₹126.35", "TARGET": "₹190.35"},
]

df_signal = pd.DataFrame(signal_log_data)
st.markdown('<div class="table-wrap">', unsafe_allow_html=True)
st.dataframe(df_signal, use_container_width=True, hide_index=True)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
