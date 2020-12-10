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
print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if sum([i,j,k]) !=n])

# Find the Runner-Up Score!
n = int(input())
a = list(set([int(n) for n in input().split()]))
a.sort()
print(a[-2])

# Nested List
index = int(input())
students_list = [[input(), float(input())] for _ in range(index)]
second = sorted(list(set([grade for student,grade in students_list])))[1]
print("\n".join([name for name,grade in sorted(students_list) if grade == second]))

# Finding the percentage
index = int(input())
students = {name: [float(m) for m in marks] for name, *marks in [input().split() for n in range(index)]}
print(f"{sum(students[input()]) / 3:0.2f}")

# Lists
n = int(input())
l = []
for i in range(n):
    s = input().split()
    mthd = s[0]
    vals = s[1:]
    if mthd != "print":
        eval(f"l.{mthd}({','.join(vals)})")
    else:
        print(l)

# Tuples
n = int(input())
print(hash(tuple([int(n) for n in input().split()])))

# Swap case
def swap_case(s):
    return s.swapcase()

# String Split and Join
def split_and_join(line):
    return "-".join(line.split())

# What's Your Name
def print_full_name(first_name, last_name):
    return print(f"Hello {first_name} {last_name}! You just delved into python.")

# Mutations
def mutate_string(string, position, character):
    l = list(s)
    l[position] = character
    return "".join(list(l))

# Find a string
def count_substring(string, sub_string):
    return [string[i:i+len(sub_string)] for i in range(len(string))].count(sub_string)

# String Validators
s = input()
print(len([c for c in s if c.isalnum()]) > 0)
print(len([c for c in s if c.isalpha()]) > 0)
print(len([c for c in s if c.isdigit()]) > 0)
print(len([c for c in s if c.islower()]) > 0)
print(len([c for c in s if c.isupper()]) > 0)

s = input()
print any([c.isalnnum() for c in s])
print any([c.isalpha() for c in s])
print any([c.isdigit() for c in s])
print any([c.islower() for c in s])
print any([c.isupper() for c in s])

# Text Wrap
import textwrap
def wrap(string, max_width):
    return textwrap.fill(string, max_width)

def print_formatted(number):
    w = len(bin(number)[2:])
    for n in range(1,number+1):
        print(f"{n:{w}d} {n:{w}o} {n:{w}X} {n:{w}b}")

# Capitalize!
def solve(s):
    return " ".join([c.capitalize() for c in s.split(" ")])
