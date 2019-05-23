from sys import argv

scirpt, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("if you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# this doesn't work:
# target.write("{}\n{}\n{}\n", line1, line2, line3)

# but this does:
formatter = "{}\n{}\n{}\n"
target.write(formatter.format(line1, line2, line3))

print("And finally, we close it.")
target.close()