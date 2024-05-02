from tkinter import *

root = Tk()

canvas = Canvas(root, width=700, height=400, bg='Floral white')
canvas.grid(columnspan=3, rowspan=4)
root.title('First steps')

r = IntVar()
r.get()

Radiobutton(root, text='option1', variable=r, value=1).grid(row=1, column=0)
Radiobutton(root, text='option1', variable=r, value=1).grid(row=1, column=0)
Radiobutton(root, text='option1', variable=r, value=1).grid(row=1, column=0)

root.mainloop()