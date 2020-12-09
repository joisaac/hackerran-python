# Write a function
def is_leap(year):
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)

# Minion game
def minion_game(string):
    s = 0
    k = 0

    for i in range(len(string)):
        if string[i] in "AEIOU":
            k += len(string) - i
        else:
            s += len(string) - i

    if s > k:
        print(f"Stuart {s}")
    elif k > s:
        print(f"Kevin {k}")
    else:
        print("Draw")

# Merge the Tools
def merge_the_tools(string, k):
    l = [string[i:i+k] for i in range(0,len(string),k)]
    for w in l:
        print("".join(dict.fromkeys(w)))
