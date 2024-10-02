'''Accept n and Print the following
a. If n is odd, print Odd
b. If n is even and in the inclusive range of 2 to 5, print Accepted
c. If n is even and in the inclusive range of 6 to 20, print Not Accepted
d. If n is even and greater than 20, print Good '''

n = int(input("Enter a number: "))

if n % 2 != 0:
    print("Odd")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Accepted")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Not Accepted")
elif n % 2 == 0 and n > 20:
    print("Good")
