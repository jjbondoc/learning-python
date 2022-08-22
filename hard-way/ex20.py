from sys import argv

script, input_file = argv
# read a stream and output contents
def print_all(f):
    print(f.read())
# move back to initial location
def rewind(f):
    f.seek(0)
# read a single line from a stream
def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file) # curent_line = 1

current_line += 1
print_a_line(current_line, current_file) # 2

current_line += 1
print_a_line(current_line, current_file) # 3