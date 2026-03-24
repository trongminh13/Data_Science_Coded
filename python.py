a = {"day": "Monday", "temperature": 32}
print(a.keys())
print(a.values())
print(a.items())

# total = 0
# for i in range(101):
#     total += i

total = sum([i for i in range(101) if i % 2 == 1])
print(total)