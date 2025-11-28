#Aim: Calculate the output of a Neural Net using both binary and bipolar sigmoidal function.
# number of elements as input
n = int(input("Enter number of elements : "))

# Entering the inputs
print("Enter the inputs")
inputs = []

for i in range(0, n):
    ele = float(input())
    inputs.append(ele)

print(inputs)

print("Enter the weights")
weights = []

for i in range(0, n):
    ele = float(input())
    weights.append(ele)

print(weights)

print("The net input can be calculated as Yin = x1w1 + x2w2 + x3w3")

Yin = []
for i in range(0, n):
    Yin.append(inputs[i] * weights[i])

print(round(sum(Yin), 3))
