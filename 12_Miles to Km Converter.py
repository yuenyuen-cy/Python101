from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=120, pady=100, bg="white")

#text

text_miles = Label(text="Miles", font=("Arial", 12, "normal"), bg="white")
text_miles.grid(row=0, column=2)

text_km = Label(text="Km", font=("Arial", 12, "normal"), bg="white")
text_km.grid(row=1, column=2)

text_equal = Label(text="is equals to", font=("Arial", 12, "normal"), bg="white")
text_equal.grid(row=1, column=0)

calculation = Label(text="0", font=("Arial", 12, "normal"), bg="white")
calculation.grid(row=1, column=1)

def click():
    miles_convertion = round(float(miles_input.get()) * 1.6,2)
    calculation.config(text=miles_convertion)

#entry
miles_input = Entry(width=10)
miles_input.grid(row=0, column=1)


#button
button = Button(text="Calculate", font=("Arial", 12, "normal"), command=click, bg="white")
button.grid(row=2, column=1, padx=10, pady=10)



window.mainloop()