threes = list(range(1, 31, 3))
for i in range(0, 3):
    print(threes[i])

slice = threes[0:3]
print(slice)

middle = int(len(threes) / 2)
print(threes[middle - 1])
print(threes[middle])
print(threes[middle + 1])

slice = threes[middle - 1 : middle + 2]
print(slice)

for i in range(-3, 0):
    print(threes[i])
slice = threes[-3:]
print(slice)
