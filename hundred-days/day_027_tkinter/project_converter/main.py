from tkinter import *

FONT = ('Arial', 12, 'normal')

def convert():
    miles = int(miles_value.get())
    km = round(miles * 1.60934)
    # km = "{:.0f}".format(round(miles * 1.60934, 0))
    km_value.config(text=km)

window = Tk()
window.title("Converter Program")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

#label - equal
label_equal = Label(text="is equal to", font=FONT)
label_equal.grid(column=0, row=1)
label_equal.config(padx=5, pady=5)

#label - miles
label_miles = Label(text="Miles", font=FONT)
label_miles.grid(column=2, row=0)
label_miles.config(padx=5, pady=5)

#label - km
label_km = Label(text="Km", font=FONT)
label_km.grid(column=2, row=1)
label_km.config(padx=5, pady=5)

#entry - miles value
miles_value = Entry(width=10)
miles_value.grid(column=1, row=0)
miles_value.focus()

#label - km value
km_value = Label(font=FONT)
km_value.grid(column=1, row=1)
km_value.config(padx=5, pady=5)

#button - calculate
button_calculate = Button(text="Calculate", command=convert)
button_calculate.grid(column=1, row=2)

window.mainloop()