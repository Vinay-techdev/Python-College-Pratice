import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(1)

#? WATER FLOW SENSOR – 48 HOURS

start_time = pd.Timestamp("2024-01-01 00:00:00")
seconds = 48 * 60 * 60  # 48 hours
time_index = pd.date_range(start_time, periods=seconds, freq="1s")

df = pd.DataFrame({"timestamp": time_index})
df["flow_lpm"] = 0.0

# Inject usage bursts
def inject_burst(start_hour, duration_sec, min_flow, max_flow):
    start = start_time + pd.Timedelta(hours=start_hour)
    end = start + pd.Timedelta(seconds=duration_sec)
    mask = (df["timestamp"] >= start) & (df["timestamp"] < end)
    df.loc[mask, "flow_lpm"] = np.random.uniform(min_flow, max_flow, mask.sum())

inject_burst(7, 300, 5, 8)     # Tap
inject_burst(8, 600, 10, 15)   # Shower
inject_burst(19, 1200, 8, 12) # Washing machine

# Inject slow leak (6 hours)
leak_start = start_time + pd.Timedelta(hours=30)
leak_end = leak_start + pd.Timedelta(hours=6)
leak_mask = (df["timestamp"] >= leak_start) & (df["timestamp"] < leak_end)
df.loc[leak_mask, "flow_lpm"] = 0.3

# Add noise 
noise_mask = df["flow_lpm"] > 0
df.loc[noise_mask, "flow_lpm"] += np.random.normal(0, 0.1, noise_mask.sum())
df["flow_lpm"] = df["flow_lpm"].clip(lower=0)

#? PANDAS TASKS

# Segment usage events
df["active"] = df["flow_lpm"] > 0.5
df["event_id"] = (df["active"] != df["active"].shift()).cumsum()

events = df[df["active"]].groupby("event_id").agg(
    start=("timestamp", "min"),
    end=("timestamp", "max"),
    duration_sec=("timestamp", "count"),
    avg_flow=("flow_lpm", "mean")
)

# Hourly water usage
df["hour"] = df["timestamp"].dt.floor("h")
hourly_usage = df.groupby("hour")["flow_lpm"].sum() / 60

# Leak detection
leak_hours = df[(df["flow_lpm"] > 0.1) & (df["flow_lpm"] < 0.5)] \
                .groupby("hour").size()

# Classification
def classify(row):
    if row.duration_sec < 300:
        return "Short usage"
    elif row.avg_flow > 10:
        return "High intensity"
    else:
        return "Normal usage"

events["pattern"] = events.apply(classify, axis=1)

# Leakage impact report
leak_volume = df.loc[leak_mask, "flow_lpm"].sum() / 60
print("\nLeakage Impact Report")
print("---------------------")
print("Leak duration: 6 hours")
print("Total leaked water (liters):", round(leak_volume, 2))

#? VISUALIZATION

plt.figure()
df.set_index("timestamp")["flow_lpm"].plot()
plt.title("Water Flow Sensor - 48 Hours")
plt.ylabel("Flow (LPM)")
plt.show()
