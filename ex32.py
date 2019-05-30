the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'guava']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this kind of for loop goes through a list
for number in the_count:
    print(f"This is count number {number}")

# same as before
for fruit in fruits:
    print(f"This fruit is: {fruit}")

# we can iterate through mixed lists too
# notice the use of {} since we don't know what we'll get
for i in change:
    print(f"I got {i}")

# we can also build lists starting with an empty one
elements = []

# then use the range function to count from 0 to 5
for i in range(0, 6):
    print(f"Adding {i} to the list")
    elements.append(i)

# now we can print them out as before
for e in elements:
    print(f"Element is: {e}")