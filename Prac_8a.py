#Aim: Implementation of Membership and Identity operators (in, not in).

# Part 1 : Membership Operator (in)

def check_overlapping(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False

print("------ PART 1 : (in) OPERATOR ------")
list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5, 6, 7]

if check_overlapping(list1, list2):
    print("Result : Lists are Overlapping (using 'in')")
else:
    print("Result : Lists are NOT Overlapping")

# Part 2 : Membership Operator (not in)

print("\n------ PART 2 : (not in) OPERATOR ------")
x = 14
my_list = [1,2,3,4,5,6,7,8,9]

if x not in my_list:
    print("Result :", x, "is NOT in the list (using 'not in')")
else:
    print("Result :", x, "is in the list")
