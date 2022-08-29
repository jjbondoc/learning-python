# from the sys package, import argv module
#from sys import argv
# unpacking argv, use two variables to hold the variables
#script, filename = argv
# open a file and return a stream, storing it in 'txt'
print(f"Type the file name:")
filename = input('> ')
txt = open(filename)

print(f"Here's your file {filename}:")
# using the .read() function to read the contents of the stream
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
txt.close()
txt_again.close()