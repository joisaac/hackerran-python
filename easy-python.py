# Say "Hello, World!" With Python
print("Hello, World!")

# Python If-Else
n = int(input().strip())
    if (n % 2 == 0) and ((n > 20) or n in range(2,6)):
        print("Not Weird")
    else:
        print("Weird")

# Arithmetic Operations
a = int(input())
b = int(input())

print(f"{a + b}\n{a - b}\n{a * b}")

# Python: Division
a = int(input())
b = int(input())

print(f"{a // b}\n{a / b}")

# Loops
n = int(input())
[print(i**2) for i in range(n)]

# Python Print
n = int(input())
print("".join([str(x) for x in range(1,n+1)]))

# List Comprehension
print([[i,k,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if sum([i,j,k]) !=n])
