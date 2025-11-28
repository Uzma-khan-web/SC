#Aim: Implementation of Identity Operators (is, is not)
# (is)
x = 5
if type(x) is int:
    print("x is of type int")
else:
    print("x is not of type int")

# (is not)
y = 5.2
if type(y) is not int:
    print("y is not of type int")
else:
    print("y is of type int")
