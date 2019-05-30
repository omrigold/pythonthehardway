ten_things = "Apples Oranges Crows Lighthouses Mix-Tapes Sugar"

print("Wait we're missing some things...")

stuff = ten_things.split(' ')

more_stuff = ["Day", "Night", "Day-Man", "Night-Man", "Boy", "Frisbee", "Club"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding ", next_one)
    stuff.append(next_one)
    print(f"There are now {len(stuff)} items.")

print("There we go: ", stuff)
print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))