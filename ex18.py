# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok, *args is actually pointless, so we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this takes no arguments
def print_none():
    print("I got nothin'.")

print_two("Omri","Goldshtrom")
print_two_again("Omri","Goldshtrom")
print_none()