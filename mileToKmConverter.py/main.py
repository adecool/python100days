from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20,pady=20)

def button_clicked():
    miles = float(miles_input_label.get())
    km = round(miles * 1.609)
    km_result_label.config(text=f'{km}')


equal_to_label = Label(text="is equal to")
equal_to_label.grid(column=0, row=1)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

km_label = Label(text='Km')
km_label.grid(column=2, row=1)

km_result_label = Label(text='')
km_result_label.grid(column=1, row=1)

button = Button(text='Calculate', command=button_clicked)
button.grid(column=1, row=2)

miles_input_label = Entry(width=10)
miles_input_label.grid(column=1, row=0)








window.mainloop()
