import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import time

st.set_page_config(page_title="EcoOptimize AI Dashboard", page_icon="🏢", layout="wide")

st.markdown("<h1 style='text-align: center; color: #1BC17E;'>EcoOptimize AI</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Intelligent Edge-AI Energy Management for Smart Buildings</h4>", unsafe_allow_html=True)

st.divider()

# Sidebar for controls
st.sidebar.header("⚙️ System Controls")
operation_mode = st.sidebar.radio("HVAC Operation Mode", ["Standard (Rule-based)", "EcoOptimize AI (Smart)"])
st.sidebar.markdown("---")
st.sidebar.subheader("Live Sensor Feeds")
building_occupancy = st.sidebar.slider("Current Building Occupancy (%)", 0, 100, 45)
outside_temp = st.sidebar.slider("Outside Temperature (°C)", 10, 40, 24)

# Simulated Data Generation
np.random.seed(42)
hours = [f"{i:02d}:00" for i in range(24)]
standard_energy = np.random.normal(loc=500, scale=30, size=24)
standard_energy[8:18] += 200  # High usage during work hours, even if nobody is there
standard_energy[18:24] += 50  # Wasted energy at night

if operation_mode == "EcoOptimize AI (Smart)":
    # AI optimizes based on occupancy curve instead of block hours
    occupancy_curve = np.array([5,5,5,5,10,20,50,80,95,90,85,90,80,90,85,75,40,20,10,5,5,5,5,5]) / 100.0
    ai_energy = 300 + (occupancy_curve * 350) + np.random.normal(0, 10, 24)
    if outside_temp > 28 or outside_temp < 15:
        ai_energy += 50
    current_power = ai_energy[14]
    daily_total = np.sum(ai_energy)
else:
    current_power = standard_energy[14]
    daily_total = np.sum(standard_energy)

# Top Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Current Power Draw (kW)", f"{current_power:.1f}")
col2.metric("Projected Daily Usage (kWh)", f"{daily_total:.0f}", delta=f"{int(daily_total - np.sum(standard_energy))} kWh" if operation_mode == "EcoOptimize AI (Smart)" else "0 kWh", delta_color="inverse")
col3.metric("Edge NPU Status", "Active (Low Latency)" if operation_mode == "EcoOptimize AI (Smart)" else "Idle")

# Main Graph
df = pd.DataFrame({
    "Time": hours,
    "Power Draw (kW)": ai_energy if operation_mode == "EcoOptimize AI (Smart)" else standard_energy,
})

st.subheader(f"⚡ Energy Consumption 24h Forecast: {operation_mode}")
fig = px.area(df, x="Time", y="Power Draw (kW)", 
              color_discrete_sequence=["#1BC17E"] if operation_mode == "EcoOptimize AI (Smart)" else ["#FF5E5E"])
fig.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
st.plotly_chart(fig, use_container_width=True)

# Edge AI Insights
st.subheader("🧠 Edge-AI Real-Time Insights")
if operation_mode == "EcoOptimize AI (Smart)":
    st.success(f"**Optimization Active:** Occupancy detected at {building_occupancy}%. Target cooling optimized to {22 if outside_temp < 25 else 24}°C. Lights dimmed in empty zones.")
    st.info("**Privacy Check:** Feature extraction ran locally on Snapdragon NPU. 0 bytes of sensitive data sent to the cloud.")
else:
    st.warning("Running on inefficient static schedule. Cooling active in all zones regardless of occupancy.")
