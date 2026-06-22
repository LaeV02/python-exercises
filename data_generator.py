import numpy as np

# 1. Generate synthetic server temperature data using a normal distribution
# loc=25.0 (mean), scale=2.0 (standard deviation), size=24 (hours)
temperature_array = np.random.normal(loc=25.0, scale=2.0, size=24)
print("--- 1D Raw Temperature Vector ---")
print(temperature_array.round(2))

# 2. Reshape the 1D vector into a 2D matrix (3 shifts of 8 hours each)
temperature_matrix = temperature_array.reshape(3, 8)
print("\n--- 2D Shift Matrix (3x8) ---")
print(temperature_matrix.round(2))

# 3. 2D Slicing (Cropping)
# Extract shift 2 (index 1) and central hours (columns 1 to 5)
# We use 1:2 instead of just 1 to keep the 2D matrix structure
central_hours_shift2 = temperature_matrix[1:2, 1:6]
print("\n--- Extracted 2D Sub-matrix (Shift 2, Central Hours) ---")
print(central_hours_shift2.round(2))