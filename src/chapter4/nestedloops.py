##
# Nested loop examples
#

# Example 1
for i in range(4):
    for j in range(i + 1):
        print("*", end="")
    print()
print()

# Example 2
for i in range(3):
    for j in range(5):
        if j % 2 == 1:
            print("*", end="")
        else:
            print("−", end="")
    print()
print()

# Example 3
for i in range(3):
    for j in range(5):
        if i % 2 == j % 2:
            print("* ", end="")
        else:
            print(" ", end="")
    print()
