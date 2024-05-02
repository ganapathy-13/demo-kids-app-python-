import datetime
from tkinter import *
import matplotlib.dates as dates
import matplotlib.pyplot as plt
import mysql.connector as mysql
import pandas as pd
from PIL import ImageTk, Image

db = mysql.connect(host='localhost', user='root', password='12345', database='kglearn')
cur = db.cursor()

'''
root11 = Tk()
canvas = Canvas(root11, width=900, height=400, bg='light yellow')
canvas.grid(columnspan=4, rowspan=4)
root11.title('First steps')

la_sno = Label(root11, text='S.No', justify=CENTER, font=('Comic Sans MS', 25), fg='purple', bg='light yellow')
la_name = Label(root11, text='Student name', justify=CENTER, font=('Comic Sans MS', 25), fg='purple', bg='light yellow')
la_mark = Label(root11, text='Mark', justify=CENTER, font=('Comic Sans MS', 25), fg='purple', bg='light yellow')
la_year = Label(root11, text='Academic year', justify=CENTER, font=('Comic Sans MS', 25), fg='purple', bg='light yellow')

text = StringVar()
text1 = StringVar()
text2 = IntVar
text3 = StringVar()


e_sno = Entry(root11, width=20, textvariable=text, justify=CENTER, font=('Comic Sans MS', 13))
e_name = Entry(root11, width=20, textvariable=text1, justify=CENTER, font=('Comic Sans MS', 13))
e_mark = Entry(root11, width=20, textvariable=text2, justify=CENTER, font=('Comic Sans MS', 13))
e_year = Entry(root11, width=20, textvariable=text3, justify=CENTER, font=('Comic Sans MS', 13))

b_add = Button(root11, text='ADD', padx=15, pady=10, fg='green', font=('Comic Sans MS', 10, 'bold'))
b_update = Button(root11, text='UPDATE', padx=15, pady=10, fg='green', font=('Comic Sans MS', 10, 'bold'))
b_delete = Button(root11, text='DELETE', padx=15, pady=10, fg='green', font=('Comic Sans MS', 10, 'bold'))

la_sno.grid(row=0, column=0)
la_name.grid(row=0, column=1)
la_mark.grid(row=0, column=2)
la_year.grid(row=0, column=3)

e_sno.grid(row=1, column=0)
e_name.grid(row=1, column=1)
e_mark.grid(row=1, column=2)
e_year.grid(row=1, column=3)

b_add.grid(row=2, column=0)
b_update.grid(row=2, column=1)
b_delete.grid(row=2, column=2)

root11.mainloop()

'''
'''
from PIL import Image, ImageTk
from gtts import gTTS #to convert text to audio
from playsound import playsound # to play the audio


root21 = Tk()
canvas = Canvas(root21, width=700, height=400, bg='light yellow')
canvas.grid(columnspan=3, rowspan=3)
root21.title('First steps')

label = Label(root21, text='Repeat after the voice.', justify=CENTER, font=('Comic Sans MS', 25), fg='purple', bg='light yellow')

label1 = Label(root21, text='Flower', justify=CENTER, font=('Comic Sans MS', 35), fg='green', bg='light yellow')
label2 = Label(root21, text='Orange', justify=CENTER, font=('Comic Sans MS', 35), fg='orange', bg='light yellow')
label3 = Label(root21, text='Apple', justify=CENTER, font=('Comic Sans MS', 35), fg='red', bg='light yellow')
label4 = Label(root21, text='Children', justify=CENTER, font=('Comic Sans MS', 35), fg='blue', bg='light yellow')

button = Button(root21, text='Next', justify=CENTER, font=('Comic Sans MS', 20), fg='whitesmoke', bg='purple')

text = "Flower"
lan = 'en'
obj = gTTS(text=text, lang=lan, slow=True)
obj.save("flower.mp3")
playsound("flower.mp3")

text1 = "Orange"
obj1 = gTTS(text=text, lang=lan, slow=True)
obj1.save("orange.mp3")
playsound("orange.mp3")

text2 = "Apple"
obj2 = gTTS(text=text, lang=lan, slow=True)
obj2.save("apple.mp3")
playsound("apple.mp3")

text3 = "Children"
obj3 = gTTS(text=text, lang=lan, slow=True)
obj3.save("children.mp3")
playsound("children.mp3")

label1.grid(row=1, column=0)
label2.grid(row=1, column=2)
label3.grid(row=2, column=0)
label4.grid(row=2, column=2)

button.grid(row=2, column=1)

label.grid(row=0, columnspan=3)
root21.mainloop()

# for english root21, 16,

from gtts import gTTS #to convert text to audio
from playsound import playsound # to play the audio
text = "Hi how are you"
lan = 'en'
obj = gTTS(text=text, lang=lan, slow=False)
obj.save("sound.mp3")
playsound("sound.mp3")
'''

root21 = Tk()
canvas = Canvas(root21, width=700, height=400, bg='light yellow')
canvas.grid(columnspan=8, rowspan=4)
root21.title('First steps')

la_title = Label(root21, text='Complete the given puzzle.', justify=CENTER, font=('Comic Sans MS', 25), fg='purple', bg='light yellow')

la = Label(root21, text='E', justify=CENTER, font=('Comic Sans MS', 25), fg='red', bg='light yellow', pady=25)
la1 = Label(root21, text='_', justify=CENTER, font=('Comic Sans MS', 25), fg='red', bg='light yellow')
la2 = Label(root21, text='R', justify=CENTER, font=('Comic Sans MS', 25), fg='red', bg='light yellow')

la3 = Label(root21, text='H',  justify=RIGHT, font=('Comic Sans MS', 25), fg='blue', bg='light yellow')
la4 = Label(root21, text='N', justify=LEFT, font=('Comic Sans MS', 25), fg='blue', bg='light yellow')
la5 = Label(root21, text='D', justify=LEFT, font=('Comic Sans MS', 25), fg='blue', bg='light yellow')

img_hand = ImageTk.PhotoImage(Image.open('img/1.jpg'))
lab_i1 = Label(root21, image=img_hand)
img_ear = ImageTk.PhotoImage(Image.open('img/3.jpg'))
lab_i1 = Label(root21, image=img_hand)
lab_i2 = Label(root21, image=img_ear)

but_e = Button(root21, text='E', justify=CENTER, font=('Comic Sans MS', 15), fg='whitesmoke', bg='brown')
but_o = Button(root21, text='O', justify=CENTER, font=('Comic Sans MS', 15), fg='whitesmoke', bg='brown')
but_a = Button(root21, text='A', justify=CENTER, font=('Comic Sans MS', 15), fg='whitesmoke', bg='brown')

but_e.grid(row=1, column=5)
but_o.grid(row=2, column=5)
but_a.grid(row=3, column=5)

lab_i1.grid(row=1, column=0)
lab_i2.grid(row=1, column=2)

la.grid(row=1, column=1)
la1.grid(row=2, column=1)
la2.grid(row=3, column=1)

la3.grid(row=2, column=0)
la4.grid(row=2, column=2)
la5.grid(row=2, column=3)

la_title.grid(row=0, columnspan=8)
root21.mainloop()

