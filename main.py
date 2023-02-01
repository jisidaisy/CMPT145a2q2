import sys
if len(sys.argv) != 2:
    # Checking if filename is given as argument
    print("Must include filename as an argument")
    sys.exit(1)

# Opening example file
with open('example.txt', 'r') as f:
    # Going through the file line by line
    for line in f.readlines():
