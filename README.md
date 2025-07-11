# 🛰️ SPACESHIP MISSION ANALYSIS SYSTEM
## Pics
<img width="944" height="534" alt="image" src="https://github.com/user-attachments/assets/bac58437-dc7a-4635-8af3-2a27439f4e42" />
<img width="944" height="433" alt="image" src="https://github.com/user-attachments/assets/f44e7509-7e9d-4d5d-b85e-2c8fbcaafc33" />
<img width="944" height="431" alt="image" src="https://github.com/user-attachments/assets/2a37d85c-b783-4016-af21-8fd4db8cf7f1" />
![Uploading image.png…]()

## Project Description
Real-time spaceship mission data analysis system with 1000 data points, including critical technical parameters and emergency protocols.

## Project Structure
```
├── spaceship_data_1000_rows.csv    # Raw spaceship data
├── spaceship_analysis.py           # Console analysis script
├── spaceship_app.py                # Streamlit web application
├── emergency_protocol.py           # Emergency protocol handler
└── README.md                       # This documentation
```

## Monitored Parameters
- **timestamp**: Data recording time
- **x, y, z**: 3D space coordinates
- **velocity**: Speed (km/s)
- **direction**: Flight direction (0-360°)
- **fuel_level**: Fuel percentage (%)
- **temperature**: Cabin temperature (°C)
- **crew_onboard**: Number of crew members
- **signal_strength**: Communication signal strength (%)
- **radiation_level**: Space radiation level (Sv/h)
- **system_status**: System condition
- **oxygen_level**: Oxygen concentration (%)
- **cabin_pressure**: Cabin pressure (kPa)

## How to Run

### 1. Console Analysis
```bash
python spaceship_analysis.py
```

### 2. Web Application
```bash
streamlit run spaceship_app.py
```

### 3. Emergency Protocol
```bash
python emergency_protocol.py
```

## Analysis Results

### I. Data Overview
- Average velocity: **7.49 km/s**
- Average fuel level: **52.4%** (DANGER)
- Average temperature: **22.0°C**
- Average signal strength: **81.5%**
- Average radiation level: **1.30 Sv/h**

### II. Trend Analysis
- Velocity: **+0.17 km/s** (slight increase)
- Fuel: **-89.7%** (critical depletion)
- Temperature: **+0.2°C** (stable)
- Signal: **-1.0%** (slight decrease)

### III. Anomaly Detection
- Critical systems: **25 times**
- Signal <70%: **162 times**
- Pressure <100 kPa: **507 times**
- Velocity >12 km/s: **0 times**

### IV. Overall Diagnosis
- **Health score: 0/100** (CRITICAL)
- **Fuel status: DANGER**
- **Radiation risk: LOW**

### V. Technical Recommendations
1. Activate fuel conservation mode
2. Check cabin pressure systems
3. Emergency maintenance for critical systems
4. Calibrate communication antenna
5. Continuous monitoring of all parameters

## 🚨 EMERGENCY STATUS

### Critical risks detected:
- **Fuel depletion: 2.7%**
- **22 critical system failures**
- **484 cabin pressure incidents**
- **157 signal loss events**

### MAYDAY protocol activated:
- [X] Switch to emergency fuel reserves
- [X] Seal cabin leaks
- [X] Restart critical systems
- [X] Boost antenna power
- [X] Prepare emergency landing
- [X] Transmit MAYDAY signal

### Mission decision:
**STATUS: ABORT MISSION - RETURN TO BASE IMMEDIATELY**

## System Requirements
- Python 3.7+
- pandas
- numpy
- streamlit
- matplotlib

## Installation
```bash
pip install pandas numpy streamlit matplotlib
```

## Author
AI Systems Engineer - National Space Mission
