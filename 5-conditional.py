# If statement
print("=== If Statement ===")
a = 10
b = 20
if a < b:
    print("A is less than B")

# If-Else statement
print("\n=== If-Else Statement ===")
c = 30
d = 20
if c < d:
    print("C is less than D")
else:
    print("C is greater than or equal to D")

# If-Elif-Else statement
print("\n=== If-Elif-Else Statement ===")
e = 20
f = 20
if e < f:
    print("E is less than F")
elif e == f:
    print("E is equal to F")
else:
    print("E is greater than F")

# Nested If statement
print("\n=== Nested If Statement ===")
g = 10
h = 20
i = 30
if g < h:
    if h < i:
        print("G is less than H and H is less than I")
    else:
        print("G is less than H but H is not less than I")
else:
    print("G is not less than H")
