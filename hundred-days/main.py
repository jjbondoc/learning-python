from tkinter import * # imports every class

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

#* Label

my_label = Label(text="I am a Label", font=('Arial', 24, 'bold')) #create
my_label.pack() #use packer to layout the label component

my_label['text'] = "New Text"
my_label.config(text="New Text")

#* Button

def button_clicked():
    my_label.config(text=input.get())
    print("Clicked")

button = Button(text="Click Me", command=button_clicked)
button.pack()

#* Entry

input = Entry(width=10)
input.pack()

window.mainloop() # keep window on screen
