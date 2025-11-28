#Aim: Generate XOR function using McCulloch-Pitts neural net.
import numpy as np

# Getting weights and threshold value
print('Enter weights')
w11 = int(input('Weight w11= '))
w12 = int(input('Weight w12= '))
w21 = int(input('Weight w21= '))
w22 = int(input('Weight w22= '))
v1 = int(input('Weight v1= '))
v2 = int(input('Weight v2= '))

print('Enter Threshold Value')
theta = int(input('theta= '))

x1 = np.array([0, 0, 1, 1])
x2 = np.array([0, 1, 0, 1])
z = np.array([0, 1, 1, 0])  # Target XOR output

con = 1
y1 = np.zeros((4,))
y2 = np.zeros((4,))
y = np.zeros((4,))

if con == 1:
    zin1 = x1 * w11 + x2 * w21
    zin2 = x1 * w12 + x2 * w22

    print("zin1:", zin1)
    print("zin2:", zin2)

    for i in range(4):
        y1[i] = 1 if zin1[i] >= theta else 0
        y2[i] = 1 if zin2[i] >= theta else 0

    print("y1:", y1)
    print("y2:", y2)

    zin = y1 * v1 + y2 * v2

    for i in range(4):
        y[i] = 1 if zin[i] >= theta else 0

    print("Final OUTPUT y:", y)
    print("Target z:", z)

print("z2", zin2)

for i in range(0, 4):
    if zin1[i] >= theta:
        y1[i] = 1
    else:
        y1[i] = 0

    if zin2[i] >= theta:
        y2[i] = 1
    else:
        y2[i] = 0

yin = np.array([])
yin = y1 * v1 + y2 * v2

for i in range(0, 4):
    if yin[i] >= theta:
        y[i] = 1
    else:
        y[i] = 0

print("yin", yin)
print('OUTPUT of Net')
y = y.astype(int)
print("y", y)
print("z", z)

if not np.array_equal(y, z):
    print("Net is not learning. Enter another set of weights and threshold value.")
    w11 = input("Weight w11 = ")
    w12 = input("Weight w12 = ")
    w21 = input("Weight w21 = ")
    w22 = input("Weight w22 = ")
    v1 = input("Weight v1 = ")
    v2 = input("Weight v2 = ")
    theta = input("theta = ")

print("McCulloch-Pitts Net for XOR function")
print("Weights of Neuron Z1")
print(w11)
print(w21)
print("Weights of Neuron Z2")
print(w12)
print(w22)
print("Weights of Neuron Y")
print(v1)
print(v2)
print("Threshold value")
print(theta)
