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

# Step 4: Calculate Yin using sum(xi * wi)
Yin_terms = []
for i in range(n):
    Yin_terms.append(inputs[i] * weights[i])

Yin = sum(Yin_terms)

print("\n-------------------------------")
print("Net Input (Yin) =", round(Yin, 4))
print("-------------------------------")

# Step 5: Binary Sigmoid Activation
binary_sigmoid = 1 / (1 + math.exp(-Yin))

# Step 6: Bipolar Sigmoid Activation
bipolar_sigmoid = (2 / (1 + math.exp(-Yin))) - 1

print("Binary Sigmoid Output     =", round(binary_sigmoid, 4))
print("Bipolar Sigmoid Output    =", round(bipolar_sigmoid, 4))
