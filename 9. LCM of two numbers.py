def compute_lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y

    value = greater
    while(True):
        if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
        else:
            greater += value
    return lcm

num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))

print("\nThe L.C.M. is :", compute_lcm(num1, num2), "\n")
