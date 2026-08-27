import streamlit as st
import pandas as pd
from pathlib import Path


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Predictive Maintenance Decision Support",
    page_icon="⚙️",
    layout="wide"
)


# ============================================================
# DATA PATH
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "dashboard_data"

# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():

    kpis = pd.read_csv(DATA_DIR / "dashboard_kpis.csv")
    pumps = pd.read_csv(DATA_DIR / "dashboard_pumps.csv")
    portfolio = pd.read_csv(DATA_DIR / "dashboard_portfolio.csv")
    strategy = pd.read_csv(DATA_DIR / "dashboard_strategy.csv")

    return kpis, pumps, portfolio, strategy


kpis, pumps, portfolio, strategy = load_data()


# ============================================================
# TITLE
# ============================================================

st.title("⚙️ Predictive Maintenance Decision Support System")

st.markdown(
    """
    **ML-based pump failure prediction + risk assessment + economic optimization + MILP portfolio selection**
    """
)

st.divider()


# ============================================================
# KPI EXTRACTION
# ============================================================

def get_kpi(name):

    row = kpis[kpis["KPI"] == name]

    if len(row) == 0:
        return None

    return row.iloc[0]["Value"]


total_pumps = get_kpi("Total Pumps")
pumps_selected = get_kpi("Pumps Selected")
maintenance_hours = get_kpi("Maintenance Hours Used")
capacity_utilization = get_kpi("Capacity Utilization (%)")
expected_failure_loss = get_kpi("Expected Failure Loss (₹)")
maintenance_cost = get_kpi("Maintenance Cost (₹)")
net_benefit = get_kpi("Expected Net Benefit (₹)")
net_benefit_per_hour = get_kpi("Net Benefit per Hour (₹)")


# ============================================================
# EXECUTIVE KPI CARDS
# ============================================================

st.subheader("Executive Summary")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Pumps Available",
        f"{int(total_pumps):,}"
    )

with col2:
    st.metric(
        "Pumps Selected",
        f"{int(pumps_selected):,}"
    )

with col3:
    st.metric(
        "Maintenance Hours",
        f"{maintenance_hours:.0f}"
    )

with col4:
    st.metric(
        "Capacity Utilization",
        f"{capacity_utilization:.1f}%"
    )


col5, col6, col7, col8 = st.columns(4)

with col5:
    st.metric(
        "Expected Failure Loss",
        f"₹{expected_failure_loss:,.0f}"
    )

with col6:
    st.metric(
        "Maintenance Cost",
        f"₹{maintenance_cost:,.0f}"
    )

with col7:
    st.metric(
        "Expected Net Benefit",
        f"₹{net_benefit:,.0f}"
    )

with col8:
    st.metric(
        "Net Benefit / Hour",
        f"₹{net_benefit_per_hour:,.0f}"
    )


st.divider()


# ============================================================
# RECOMMENDED STRATEGY
# ============================================================

st.subheader("Recommended Maintenance Strategy")

st.success(
    "Risk-Constrained MILP — Recommended"
)

st.markdown(
    """
    The optimization model selects a maintenance portfolio subject to
    pump and maintenance-hour capacity constraints while prioritizing
    economically valuable high-risk assets.
    """
)


# ============================================================
# STRATEGY COMPARISON
# ============================================================

st.subheader("Maintenance Strategy Comparison")

strategy_display = strategy.copy()

st.dataframe(
    strategy_display,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# STRATEGY CHARTS
# ============================================================

col1, col2 = st.columns(2)

with col1:

    st.markdown("### Expected Net Benefit")

    if "Expected Net Benefit (₹)" in strategy.columns:

        chart_data = strategy.set_index("Strategy")[
            ["Expected Net Benefit (₹)"]
        ]

        st.bar_chart(chart_data)


with col2:

    st.markdown("### Actual Failure Coverage")

    if "Failure Coverage (%)" in strategy.columns:

        chart_data = strategy.set_index("Strategy")[
            ["Failure Coverage (%)"]
        ]

        st.bar_chart(chart_data)


st.divider()


# ============================================================
# MILP PORTFOLIO
# ============================================================

st.subheader("MILP Selected Maintenance Portfolio")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Selected Pumps",
        f"{len(portfolio)}"
    )

with col2:
    st.metric(
        "Average Failure Probability",
        f"{portfolio['Failure_Probability'].mean():.3f}"
    )

with col3:
    st.metric(
        "Average Condition Severity",
        f"{portfolio['Condition_Severity'].mean():.2f}"
    )


# ============================================================
# PORTFOLIO RISK PROFILE
# ============================================================

st.subheader("Failure Probability — Selected Portfolio")

risk_distribution = (
    portfolio["Failure_Probability"]
    .value_counts(bins=10)
    .sort_index()
)

st.bar_chart(risk_distribution)


# ============================================================
# PORTFOLIO TABLE
# ============================================================

st.subheader("Selected Pumps")

display_columns = [
    "Pump_ID",
    "Failure_Probability",
    "Risk_Level",
    "Actual_Failure",
    "Maintenance_Hours",
    "Failure_Cost",
    "Maintenance_Cost",
    "Expected_Failure_Loss",
    "Expected_Net_Benefit",
    "Benefit_Per_Hour",
    "Condition_Severity"
]

available_columns = [
    col for col in display_columns
    if col in portfolio.columns
]

st.dataframe(
    portfolio[available_columns],
    use_container_width=True,
    hide_index=True
)


# ============================================================
# DOWNLOAD
# ============================================================

st.divider()

st.subheader("Export")

csv = portfolio.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Selected Portfolio",
    data=csv,
    file_name="milp_selected_portfolio.csv",
    mime="text/csv"
)


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Industrial Pump Predictive Maintenance | "
    "Machine Learning + Economic Decision Modeling + MILP Optimization"
)