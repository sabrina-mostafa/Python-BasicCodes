import math


num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))

x = math.gcd(num1, num2)
y = math.lcm(num1, num2)

print("\nThe GCD is :", x, "\n")
print("The LCM is :", y, "\n")
