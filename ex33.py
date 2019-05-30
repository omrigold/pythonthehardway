def addList(i, numbers):
    print(f"At the top i is {i}")
    numbers.append(i)
    print("Numbers now: ", numbers)
    return numbers

i = 0
end = 8
numbers = []

while i < end:
    numbers = addList(i, numbers)
    i += 1

print("The numbers: ")

for num in numbers:
    print(num)