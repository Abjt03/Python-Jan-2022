# Print Fibonacci series for N terms where N is input by the User
N = int(input("Enter number of terms : "))

# First 2 terms
a, b = 0, 1

# Check N and Generate Fibo Sequence
if N <= 0:
    print("Please enter a positive integer")
elif N == 1:
    print("Fibonacci sequence upto", N, ":")
    print(a)
else:
    print("Fibonacci sequence:")
    count = 0
    while count < N:
        print(a, end=' ')
        c = a + b
        a = b
        b = c
        count += 1
