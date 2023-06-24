def compute_gcd(a, b):
    while(b!=0):
        r = a % b
        a = b
        b = r
    return a

num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))

print("\nThe GCD is :", compute_gcd(num1, num2), "\n")
