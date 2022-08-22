from tkinter import * # imports every class

def button_clicked():
    my_label.config(text=input.get())
    print("Clicked")

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

#* Label

my_label = Label(text="I am a Label", font=('Arial', 24, 'bold')) #create
my_label.config(text="New Text")
my_label.grid(column=0, row=0)

#* Button

button = Button(text="Button 1", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="Button 2")
new_button.grid(column=2, row=0)

#* Entry

input = Entry(width=10)
input.grid(column=4, row=2)

window.mainloop() # keep window on screen