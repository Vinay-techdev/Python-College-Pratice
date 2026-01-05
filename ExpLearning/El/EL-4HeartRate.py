import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(2)

#? HEART RATE SENSOR – 24 HOURS

start_time = pd.Timestamp("2024-01-02 00:00:00")
records = int((24 * 60 * 60) / 5)
time_index = pd.date_range(start_time, periods=records, freq="5s")

df = pd.DataFrame({"timestamp": time_index})

# Baseline heart rate
def baseline(ts):
    if 0 <= ts.hour < 6:
        return np.random.normal(58, 3)   # Sleep
    elif 6 <= ts.hour < 22:
        return np.random.normal(72, 5)   # Active
    else:
        return np.random.normal(62, 4)

df["heart_rate"] = df["timestamp"].apply(baseline)

# Exercise sessions
exercises = [
    (7, 1800),
    (18, 2400)
]

for hour, duration in exercises:
    start = start_time + pd.Timedelta(hours=hour)
    end = start + pd.Timedelta(seconds=duration)
    mask = (df["timestamp"] >= start) & (df["timestamp"] < end)
    df.loc[mask, "heart_rate"] += np.linspace(40, 70, mask.sum())

# Recovery
for hour, duration in exercises:
    end = start_time + pd.Timedelta(hours=hour, seconds=duration)
    rec_mask = (df["timestamp"] >= end) & \
               (df["timestamp"] < end + pd.Timedelta(minutes=10))
    df.loc[rec_mask, "heart_rate"] -= np.linspace(30, 0, rec_mask.sum())

# Dropouts
drop_idx = np.random.choice(df.index, 50, replace=False)
df.loc[drop_idx, "heart_rate"] = np.nan

#? PANDAS TASKS

# Sleep / Active detection
df["state"] = np.where(df["heart_rate"] < 65, "Sleep", "Active")

# Exercise detection
df["exercise"] = df["heart_rate"] > 110

# Abnormal heart rate
abnormal = df[(df["heart_rate"] > 160) | (df["heart_rate"] < 45)]

# Daily summary
summary = pd.DataFrame({
    "Average HR": [round(df["heart_rate"].mean(), 2)],
    "Max HR": [df["heart_rate"].max()],
    "Exercise Records": [df["exercise"].sum()],
    "Abnormal Episodes": [len(abnormal)]
})

print("\nDaily Fitness Summary")
print("---------------------")
print(summary)

#? VISUALIZATION

plt.figure()
df.set_index("timestamp")["heart_rate"].plot()
plt.title("Heart Rate Sensor – 24 Hours")
plt.ylabel("BPM")
plt.show()
