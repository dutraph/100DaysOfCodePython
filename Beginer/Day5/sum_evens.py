total_evens = 0
for even in range(0, 101, 2):
    total_evens += even
print(total_evens)

# Or 

total_evens2 = 0
for i in range(1, 101):
    if (i % 2 == 0):
        total_evens2 += i
print(total_evens2)