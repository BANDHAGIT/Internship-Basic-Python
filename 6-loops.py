# For Loop
print("=== For Loop ===")
for i in range(5):
    print("Iteration:", i)

# For Loop with List
print("\n=== For Loop with List ===")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit:", fruit)

# While Loop
print("\n=== While Loop ===")
count = 0
while count < 5:
    print("Count:", count)
    count += 1

# Break Statement
print("\n=== Break Statement ===")
for i in range(10):
    if i == 5:
        print("Loop stopped at", i)
        break
    print(i)

# Continue Statement
print("\n=== Continue Statement ===")
for i in range(6):
    if i == 3:
        continue
    print(i)

# Nested Loop
print("\n=== Nested Loop ===")
for i in range(3):
    for j in range(2):
        print("i:", i, "| j:", j)
