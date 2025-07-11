import pandas as pd
import numpy as np

# Load data
df = pd.read_csv('spaceship_data_1000_rows.csv')
np.random.seed(42)
df['system_status'] = np.random.choice(['OK', 'Minor Fault', 'Critical'], len(df), p=[0.85, 0.12, 0.03])
df['cabin_pressure'] = np.random.uniform(95, 105, len(df))
df['signal_strength'] = np.random.uniform(65, 98, len(df))

print("*** EMERGENCY PROTOCOL ACTIVATED ***\n")

# Critical Issues
critical_systems = len(df[df['system_status'] == 'Critical'])
low_fuel = len(df[df['fuel_level'] < 20])
low_pressure = len(df[df['cabin_pressure'] < 100])
low_signal = len(df[df['signal_strength'] < 70])

print("IMMEDIATE ACTIONS REQUIRED:")
print(f"1. FUEL EMERGENCY: {df['fuel_level'].min():.1f}% remaining")
print(f"2. CRITICAL SYSTEMS: {critical_systems} failures detected")
print(f"3. PRESSURE BREACH: {low_pressure} incidents")
print(f"4. COMMUNICATION: {low_signal} signal drops\n")

print("EMERGENCY PROCEDURES:")
print("[X] Switch to emergency fuel reserves")
print("[X] Seal cabin pressure leaks immediately") 
print("[X] Restart critical system components")
print("[X] Boost communication array power")
print("[X] Prepare for emergency landing protocol")
print("[X] Alert ground control - MAYDAY signal")

print(f"\nSYSTEM STATUS: CRITICAL - Health Score: 0/100")
print("MISSION STATUS: ABORT - Return to base immediately")