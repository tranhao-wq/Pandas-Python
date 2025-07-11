import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Spaceship Analysis", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv('spaceship_data_1000_rows.csv')
    np.random.seed(42)
    df['crew_onboard'] = np.random.randint(3, 8, len(df))
    df['signal_strength'] = np.random.uniform(65, 98, len(df))
    df['radiation_level'] = np.random.uniform(0.1, 2.5, len(df))
    df['system_status'] = np.random.choice(['OK', 'Minor Fault', 'Critical'], len(df), p=[0.85, 0.12, 0.03])
    df['oxygen_level'] = np.random.uniform(19, 22, len(df))
    df['cabin_pressure'] = np.random.uniform(95, 105, len(df))
    return df

df = load_data()

st.title("🛰️ SPACESHIP MISSION ANALYSIS")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Velocity", f"{df['velocity'].mean():.1f} km/s")
with col2:
    st.metric("Fuel Level", f"{df['fuel_level'].mean():.1f}%", 
              delta=f"{df['fuel_level'].iloc[-1] - df['fuel_level'].iloc[0]:.1f}%")
with col3:
    st.metric("Temperature", f"{df['temperature'].mean():.1f}°C")
with col4:
    st.metric("Signal", f"{df['signal_strength'].mean():.1f}%")

col1, col2 = st.columns(2)

with col1:
    fig, ax = plt.subplots()
    ax.plot(df.head(100)['velocity'], label='Velocity')
    ax.plot(df.head(100)['fuel_level'], label='Fuel Level')
    ax.legend()
    ax.set_title("Velocity & Fuel Trends")
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots()
    scatter = ax.scatter(df.head(100)['velocity'], df.head(100)['fuel_level'], 
                        c=df.head(100)['temperature'], cmap='viridis')
    ax.set_xlabel('Velocity')
    ax.set_ylabel('Fuel Level')
    ax.set_title("Velocity vs Fuel")
    plt.colorbar(scatter)
    st.pyplot(fig)

# Anomaly Detection
st.subheader("🚨 ANOMALY DETECTION")
critical_systems = len(df[df['system_status'] == 'Critical'])
low_signal = len(df[df['signal_strength'] < 70])
low_pressure = len(df[df['cabin_pressure'] < 100])

col1, col2, col3 = st.columns(3)
with col1:
    st.error(f"Critical Systems: {critical_systems}")
with col2:
    st.warning(f"Low Signal: {low_signal}")
with col3:
    st.warning(f"Low Pressure: {low_pressure}")

# System Health
health_score = max(100 - (critical_systems*10 + low_signal*3 + low_pressure*2), 0)
st.subheader("📊 SYSTEM HEALTH")
st.progress(health_score/100)
st.write(f"Health Score: {health_score}/100")

if health_score < 50:
    st.error("CRITICAL: Immediate maintenance required!")
elif health_score < 80:
    st.warning("WARNING: System monitoring needed")
else:
    st.success("GOOD: Systems operating normally")