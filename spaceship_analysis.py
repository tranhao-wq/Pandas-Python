import pandas as pd
import numpy as np

# Doc du lieu
df = pd.read_csv('spaceship_data_1000_rows.csv')

print("=== BAO CAO PHAN TICH HE THONG TAU VU TRU ===\n")

# I. TONG QUAN SO LIEU
print("I. TONG QUAN SO LIEU")
print(f"Toc do trung binh: {df['velocity'].mean():.2f} km/s")
print(f"Nhien lieu trung binh: {df['fuel_level'].mean():.1f}%")
print(f"Nhiet do trung binh: {df['temperature'].mean():.1f} do C")

# Them cac cot con thieu voi gia tri mo phong
np.random.seed(42)
df['crew_onboard'] = np.random.randint(3, 8, len(df))
df['signal_strength'] = np.random.uniform(65, 98, len(df))
df['radiation_level'] = np.random.uniform(0.1, 2.5, len(df))
df['system_status'] = np.random.choice(['OK', 'Minor Fault', 'Critical'], len(df), p=[0.85, 0.12, 0.03])
df['oxygen_level'] = np.random.uniform(19, 22, len(df))
df['cabin_pressure'] = np.random.uniform(95, 105, len(df))
df['power_usage'] = np.random.uniform(45, 85, len(df))

print(f"Tin hieu trung binh: {df['signal_strength'].mean():.1f}%")
print(f"Buc xa trung binh: {df['radiation_level'].mean():.2f} Sv/h")
print(f"Oxy trung binh: {df['oxygen_level'].mean():.1f}%")

# II. PHAN TICH XU HUONG
print("\nII. PHAN TICH XU HUONG")
velocity_trend = df['velocity'].iloc[-50:].mean() - df['velocity'].iloc[:50].mean()
fuel_trend = df['fuel_level'].iloc[-50:].mean() - df['fuel_level'].iloc[:50].mean()
temp_trend = df['temperature'].iloc[-50:].mean() - df['temperature'].iloc[:50].mean()
signal_trend = df['signal_strength'].iloc[-50:].mean() - df['signal_strength'].iloc[:50].mean()

print(f"Xu huong van toc: {velocity_trend:+.2f} km/s")
print(f"Xu huong nhien lieu: {fuel_trend:+.1f}%")
print(f"Xu huong nhiet do: {temp_trend:+.1f} do C")
print(f"Xu huong tin hieu: {signal_trend:+.1f}%")

# III. PHAT HIEN BAT THUONG
print("\nIII. PHAT HIEN BAT THUONG")
critical_systems = len(df[df['system_status'] == 'Critical'])
high_velocity = len(df[df['velocity'] > 12])
low_signal = len(df[df['signal_strength'] < 70])
low_pressure = len(df[df['cabin_pressure'] < 100])

print(f"He thong Critical: {critical_systems} lan")
print(f"Van toc >12 km/s: {high_velocity} lan")
print(f"Tin hieu <70%: {low_signal} lan")
print(f"Ap suat <100 kPa: {low_pressure} lan")

# IV. CHAN DOAN TONG THE
print("\nIV. CHAN DOAN TONG THE")
health_score = 100 - (critical_systems*10 + high_velocity*5 + low_signal*3 + low_pressure*2)
fuel_status = "Tot" if df['fuel_level'].mean() > 85 else "Canh bao" if df['fuel_level'].mean() > 70 else "Nguy hiem"

print(f"Diem suc khoe he thong: {max(health_score, 0)}/100")
print(f"Trang thai nhien lieu: {fuel_status}")
print(f"Nguy co buc xa: {'Thap' if df['radiation_level'].mean() < 1.5 else 'Cao'}")

# V. DE XUAT KY THUAT
print("\nV. DE XUAT KY THUAT")
if df['fuel_level'].mean() < 80:
    print("- Kich hoat che do tiet kiem nhien lieu")
if df['temperature'].mean() > 23:
    print("- Tang cuong lam mat he thong")
if low_signal > 50:
    print("- Kiem tra va hieu chinh anten lien lac")
if critical_systems > 0:
    print("- Thuc hien bao tri khan cap he thong")
print("- Duy tri giam sat lien tuc cac thong so quan trong")