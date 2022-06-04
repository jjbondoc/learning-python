import tkinter

window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

#* Label

my_label = tkinter.Label(text="I am a Label", font=('Arial', 24, 'bold')) #create
my_label.pack() #use packer to layout the label component








window.mainloop() # keep window on screen