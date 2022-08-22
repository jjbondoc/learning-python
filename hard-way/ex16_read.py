print("Type the filename: ")
filename = input("> ")

txt = open(filename)
print(txt.read())