import numpy as np

# Dataset: 5 seconds of driving data
# Columns: [Speed (km/h), Distance (m), Fog_Level (0-100)]
driving_data = np.array([
    [50.0,  25.5, 10.0],  # Second 1
    [80.0,  12.0, 45.0],  # Second 2
    [120.0, 80.0, 85.0],  # Second 3
    [0.0,    1.2, 90.0],  # Second 4
    [65.0,  34.0, 20.0]   # Second 5
])

# 1. Isolate the distance column and find the minimum distance
distances = driving_data[:, 1]
min_distance = np.min(distances)
print("Minimum distance recorded:", min_distance, "meters")

# 2. Find the maximum speed reached
max_speed = np.max(driving_data[:, 0])
print("Maximum speed recorded:", max_speed, "km/h")

# 3. Normalize the Fog Level column (bring values between 0 and 1)
# Note: your np.divide approach was correct, but you can also just do / 100
driving_data[:, 2] = driving_data[:, 2] / 100.0

# 4. Emergency Filter (Boolean Masking)
# Danger is when distance is LESS than 15 meters
danger_mask = distances < 15
print("\nDanger Mask (True means dangerous second):", danger_mask)

# Vectorized Filtering: No loops needed! 
# This extracts only the rows from driving_data where danger_mask is True
print("\n--- EMERGENCY LOGS (Dangerous Seconds) ---")
print(driving_data[danger_mask])