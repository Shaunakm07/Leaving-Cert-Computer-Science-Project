import pandas as pd
import matplotlib.pyplot as plt

CSV_FILE = "serial_parsed_only.csv"  # change if your filename is different

# Load
df = pd.read_csv(CSV_FILE)

# Ensure numeric
df["timestamp"] = pd.to_numeric(df["timestamp"], errors="coerce")
for col in ["moisture", "temperature", "humidity"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Drop bad rows
df = df.dropna(subset=["timestamp", "moisture", "temperature", "humidity"])

# Make time axis (seconds since start)
df["time_sec"] = df["timestamp"] - df["timestamp"].iloc[0]

# Plot (all on one chart)
plt.figure()
plt.plot(df["time_sec"], df["temperature"], label="Temperature (°C)")
plt.plot(df["time_sec"], df["humidity"], label="Humidity (%)")
plt.plot(df["time_sec"], df["moisture"], label="Moisture")

plt.xlabel("Time (s)")
plt.ylabel("Value")
plt.title("Sensor Data Over Time")
plt.legend()
plt.grid(True)
plt.show()
