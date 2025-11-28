import math

# Step 1: Number of inputs
n = int(input("Enter number of elements: "))

# Step 2: Enter input values
print("Enter the inputs:")
inputs = []
for i in range(n):
    ele = float(input())
    inputs.append(ele)

# Step 3: Enter weight values
print("Enter the weights:")
weights = []
for i in range(n):
    ele = float(input())
    weights.append(ele)

# Store the final net input value
Yin_value = sum(Yin)

# Binary Sigmoid Function
binary_sigmoid = 1 / (1 + (2.71828 ** (-Yin_value)))

# Bipolar Sigmoid Function
bipolar_sigmoid = (2 / (1 + (2.71828 ** (-Yin_value)))) - 1

print("Binary Sigmoid Output =", round(binary_sigmoid, 4))
print("Bipolar Sigmoid Output =", round(bipolar_sigmoid, 4))
