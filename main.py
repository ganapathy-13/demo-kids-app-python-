from tkinter import *
import mysql.connector as mysql
from PIL import Image, ImageTk
import pandas as pd
from tkinter import messagebox as mb
from matplotlib.backends._backend_tk import NavigationToolbar2Tk #NavigationToolbar2Tk is a built-in toolbar for the figure on the graph
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg # you can use matplotlib from an arbitrary non-gui python shell.
from matplotlib.figure import Figure

db = mysql.connect(host='localhost', user='root', password='12345', database='kglearn')
cur = db.cursor()


def home_page():
    root3 = Tk()
    canvas1 = Canvas(root3, width=700, height=400, bg='light yellow')
    canvas1.grid(columnspan=3, rowspan=3)
    root3.title('First steps')

    l_sub = Label(text='SUBJECTS', justify=CENTER, font=('Comic Sans MS', 25), fg='purple', bg='light yellow')

    def bevs():
        root3.destroy()
        evs()

    def beng(): 
        root3.destroy()
        eng()

    def bmat():
        root3.destroy()
        mat()

    b_evs = Button(root3, text='EVS', command=bevs, padx=20, pady=15, fg='white', bg='green', font=('Comic Sans MS', 15, 'bold'))
    b_eng = Button(root3, text='ENG', command=beng, padx=20, pady=15, fg='white', bg='red', font=('Comic Sans MS', 15, 'bold'))
    b_mat = Button(root3, text='MAT', command=bmat, padx=20, pady=15, fg='white', bg='blue', font=('Comic Sans MS', 15, 'bold'))

    l_sub.grid(row=0, column=1)
    b_evs.grid(row=1, column=0)
    b_mat.grid(row=1, column=2)
    b_eng.grid(row=1, column=1)

    root3.mainloop()


def result_p():
    i = str(i3)
    root8.destroy()
    root4 = Tk()
    canvas = Canvas(root4, width=700, height=400, bg='Floral white')
    canvas.grid(columnspan=4, rowspan=3)
    root4.title('First steps')

    la_title = Label(root4, text="RESULT", justify=CENTER, font=('Comic Sans MS', 25), fg='purple', bg='Floral white')
    la_score = Label(root4, text="Your score is "+i, justify=CENTER, font=('Comic Sans MS', 30), fg='green', bg='Floral white')

    def b_mark():
        root4.destroy()
        mark_sheet()

    def quit_main():
        root4.destroy()

    def b_home():
        root4.destroy()
        home_page()

    def b_log():
        root4.destroy()
        log_page()

    but1 = Button(root4, text="QUIT", command=quit_main, padx=20, pady=15, fg='purple', bg='light blue', font=('Comic Sans MS', 15, 'bold'))
    but2 = Button(root4, text="SUBJECTS", command=b_home, padx=20, pady=15, fg='purple', bg='light blue', font=('Comic Sans MS', 15, 'bold'))
    but3 = Button(root4, text="MARK ENTRY", command=b_mark, padx=20, pady=15, fg='purple', bg='light blue', font=('Comic Sans MS', 15, 'bold'))
    but4 = Button(root4, text='log', command=b_log, padx=20, pady=15, fg='purple', bg='light blue', font=('Comic Sans MS', 15, 'bold'))

    la_title.grid(row=0, columnspan=4)
    la_score.grid(row=1, columnspan=4)

    but1.grid(row=2, column=0)
    but2.grid(row=2, column=1)
    but3.grid(row=2, column=2)
    but4.grid(row=2, column=3)

    root4.mainloop()


def result_p_m():
    i = str(i4)
    root20.destroy()
    root4 = Tk()
    canvas = Canvas(root4, width=700, height=400, bg='Floral white')
    canvas.grid(columnspan=4, rowspan=3)
    root4.title('First steps')

    la_title = Label(root4, text="RESULT", justify=CENTER, font=('Comic Sans MS', 25), fg='purple', bg='Floral white')
    la_score = Label(root4, text="Your score is "+i, justify=CENTER, font=('Comic Sans MS', 30), fg='green', bg='Floral white')

    def b_mark():
        root4.destroy()
        mark_sheet()

    def quit_main():
        root4.destroy()

    def b_home():
        root4.destroy()
        home_page()

    def b_log():
        root4.destroy()
        log_page()

    but1 = Button(root4, text="QUIT", command=quit_main, padx=20, pady=15, fg='purple', bg='cyan', font=('Comic Sans MS', 15, 'bold'))
    but2 = Button(root4, text="SUBJECTS", command=b_home, padx=20, pady=15, fg='purple', bg='Cyan', font=('Comic Sans MS', 15, 'bold'))
    but3 = Button(root4, text="MARK ENTRY", command=b_mark, padx=20, pady=15, fg='purple', bg='Cyan', font=('Comic Sans MS', 15, 'bold'))
    but4 = Button(root4, text='log', command=b_log, padx=20, pady=15, fg='purple', bg='Cyan', font=('Comic Sans MS', 15, 'bold'))

    la_title.grid(row=0, columnspan=4)
    la_score.grid(row=1, columnspan=4)

    but1.grid(row=2, column=0)
    but2.grid(row=2, column=1)
    but3.grid(row=2, column=2)
    but4.grid(row=2, column=3)

    root4.mainloop()


def result_p_e():
    i = str(i3)
    root21.destroy()
    root4 = Tk()
    canvas = Canvas(root4, width=700, height=400, bg='Floral white')
    canvas.grid(columnspan=4, rowspan=3)
    root4.title('First steps')

    la_title = Label(root4, text="RESULT", justify=CENTER, font=('Comic Sans MS', 25), fg='purple', bg='Floral white')
    la_score = Label(root4, text="Your score is "+i, justify=CENTER, font=('Comic Sans MS', 30), fg='green', bg='Floral white')

    def b_mark():
        root4.destroy()
        mark_sheet()

    def quit_main():
        root4.destroy()

    def b_home():
        root4.destroy()
        home_page()

    def b_log():
        root4.destroy()
        log_page()

    but1 = Button(root4, text="QUIT", command=quit_main, padx=20, pady=15, fg='purple', bg='light blue', font=('Comic Sans MS', 15, 'bold'))
    but2 = Button(root4, text="SUBJECTS", command=b_home, padx=20, pady=15, fg='purple', bg='light blue', font=('Comic Sans MS', 15, 'bold'))
    but3 = Button(root4, text="MARK ENTRY", command=b_mark, padx=20, pady=15, fg='purple', bg='light blue', font=('Comic Sans MS', 15, 'bold'))
    but4 = Button(root4, text='log', command=b_log, padx=20, pady=15, fg='purple', bg='light blue', font=('Comic Sans MS', 15, 'bold'))

    la_title.grid(row=0, columnspan=4)
    la_score.grid(row=1, columnspan=4)

    but1.grid(row=2, column=0)
    but2.grid(row=2, column=1)
    but3.grid(row=2, column=2)
    but4.grid(row=2, column=3)

    root4.mainloop()


def log_page():
    root10 = Tk()

    fig = Figure(figsize=(10, 10), dpi=100)  # creating figure for placing graph in tkinter

    plot1 = fig.add_subplot(111)  # creating subplot for the graph to be ploted

    query_log = "Select * from log"
    log = pd.read_sql(query_log, db)
    df_log = pd.DataFrame(log)

    plot1.bar(df_log.date, df_log.name)

    canvas = FigureCanvasTkAgg(fig, master=root10)
    canvas.draw()
    canvas.get_tk_widget().pack()

    toolbar = NavigationToolbar2Tk(canvas, root10)
    toolbar.update()

    canvas.get_tk_widget().pack()

    root10.mainloop()


def evs():
    global result
    result = 0
    q1()


def q1():
    global root5
    root5 = Tk()
    canvas = Canvas(root5, width=700, height=400, bg='light blue')
    canvas.grid(columnspan=4, rowspan=3)
    root5.title('First steps')

    qus1 = Label(root5, text='Which of the following is hand?', justify=CENTER, font=('Comic Sans MS', 25), fg='purple', bg='light blue')
    qus1.grid(row=0, columnspan=5)

    img_but1 = ImageTk.PhotoImage(Image.open('img/1.jpg'))
    img_but2 = ImageTk.PhotoImage(Image.open('img/2.jpg'))
    img_but3 = ImageTk.PhotoImage(Image.open('img/3.jpg'))
    img_but4 = ImageTk.PhotoImage(Image.open('img/4.jpg'))

    def ans1():
        global i
        i = result
        q2()

    def ans():
        global i
        i = result + 1
        q2()

    button1 = Button(root5, command=ans, image=img_but1)
    button2 = Button(root5, command=ans1, image=img_but2)
    button3 = Button(root5, command=ans1, image=img_but3)
    button4 = Button(root5, command=ans1, image=img_but4)

    button1.grid(row=1, column=0)
    button2.grid(row=1, column=1)
    button3.grid(row=1, column=2)
    button4.grid(row=1, column=3)

    root5.mainloop()


def q2():
    root5.destroy()
    global root6
    root6 = Tk()
    canvas = Canvas(root6, width=700, height=400, bg='light blue')
    canvas.grid(columnspan=4, rowspan=3)
    root6.title('First steps')

    qus1 = Label(root6, text='Which of the following is lips?', justify=CENTER, font=('Comic Sans MS', 25), fg='purple', bg='light blue')
    qus1.grid(row=0, columnspan=5)

    img_but1 = ImageTk.PhotoImage(Image.open('img/1.jpg'))
    img_but2 = ImageTk.PhotoImage(Image.open('img/2.jpg'))
    img_but3 = ImageTk.PhotoImage(Image.open('img/3.jpg'))
    img_but4 = ImageTk.PhotoImage(Image.open('img/4.jpg'))

    def ans1():
        global i1
        i1 = i
        q3()

    def ans():
        global i1
        i1 = i + 1
        q3()

    button1 = Button(root6, command=ans1, image=img_but1)
    button2 = Button(root6, command=ans, image=img_but2)
    button3 = Button(root6, command=ans1, image=img_but3)
    button4 = Button(root6, command=ans1, image=img_but4)

    button1.grid(row=1, column=0)
    button2.grid(row=1, column=1)
    button3.grid(row=1, column=2)
    button4.grid(row=1, column=3)

    root6.mainloop()


def q3():
    root6.destroy()
    global root7
    root7 = Tk()

    canvas = Canvas(root7, width=700, height=400, bg='light blue')
    canvas.grid(columnspan=3, rowspan=4)
    root7.title('First steps')

    la = Label(root7, text='Who gives injection to you?', font=('Comic Sans MS', 25), fg='purple', bg='light blue')
    la.grid(row=0, columnspan=3)

    r1 = IntVar()
    r1.get()
    r2 = IntVar()
    r2.get()
    r3 = IntVar()
    r3.get()
    r4 = IntVar()
    r4.get()
    r5 = IntVar()
    r5.get()
    r6 = IntVar()
    r6.get()

    def ans1():
        global i2
        i2 = i1
        q4()

    def ans():
        global i2
        i2 = i1 + 1
        q4()

    Radiobutton(root7, text='cook', variable=r1, value=1, command=ans1, font=('Comic Sans MS', 25), fg='green', bg='light blue').grid(row=1, column=0)
    Radiobutton(root7, text='doctor', variable=r2, value=1, command=ans, font=('Comic Sans MS', 25), fg='green', bg='light blue').grid(row=1, column=2)
    Radiobutton(root7, text='teacher', variable=r3, value=1, command=ans1, font=('Comic Sans MS', 25), fg='green', bg='light blue').grid(row=1, column=1)
    Radiobutton(root7, text='student', variable=r4, value=1, command=ans1, font=('Comic Sans MS', 25), fg='green', bg='light blue').grid(row=2, column=0)
    Radiobutton(root7, text='gardner', variable=r5, value=1, command=ans1, font=('Comic Sans MS', 25), fg='green', bg='light blue').grid(row=2, column=1)
    Radiobutton(root7, text='pilot', variable=r6, value=1, command=ans1, font=('Comic Sans MS', 25), fg='green', bg='light blue').grid(row=2, column=2)

    root7.mainloop()


def q4():
    root7.destroy()
    global root8
    root8 = Tk()
    canvas = Canvas(root8, width=700, height=400, bg='light blue')
    canvas.grid(columnspan=4, rowspan=3)
    root8.title('First steps')

    qus4 = Label(root8, text='which of the following eat only plants?', justify=CENTER, font=('Comic Sans MS', 25), fg='purple', bg='light blue')

    img_but1 = ImageTk.PhotoImage(Image.open('img/giraf.jpeg'))
    img_but2 = ImageTk.PhotoImage(Image.open('img/tiger.jpeg'))
    img_but3 = ImageTk.PhotoImage(Image.open('img/snake.jpeg'))
    img_but4 = ImageTk.PhotoImage(Image.open('img/lion.jpeg'))

    def ans1():
        global i3
        i3 = i2
        result_p()

    def ans():
        global i3
        i3 = i2 + 1
        result_p()

    button1 = Button(root8, command=ans, image=img_but1)
    button2 = Button(root8, command=ans1, image=img_but2)
    button3 = Button(root8, command=ans1, image=img_but3)
    button4 = Button(root8, command=ans1, image=img_but4)

    qus4.grid(row=0, columnspan=5)

    button1.grid(row=1, column=0)
    button2.grid(row=1, column=1)
    button3.grid(row=1, column=2)
    button4.grid(row=1, column=3)

    root8.mainloop()


def eng():
    global result
    result = 0
    eq1()


def eq1():
    global root13
    root13 = Tk()
    canvas = Canvas(root13, width=700, height=400, bg='light green')
    canvas.grid(columnspan=4, rowspan=3)
    root13.title('First steps')

    lable = Label(root13, text='Click the first letters.', justify=CENTER, font=('Comic Sans MS', 25), fg='purple', bg='light green')

    img_flower = ImageTk.PhotoImage(Image.open('img/f.jpg'))
    img_orange = ImageTk.PhotoImage(Image.open('img/o.jpg'))

    def ans1():
        global i
        i = result
        eq2()

    def ans():
        global i
        i = result + 1
        eq2()

    but_ans = Button(root13, text='F, O', command=ans, padx=10, pady=10, fg='white', bg='green',font=('Comic Sans MS', 10, 'bold'))
    but_wans1 = Button(root13, text='S, O', command=ans1, padx=10, pady=10, fg='white', bg='green',font=('Comic Sans MS', 10, 'bold'))
    but_wans2 = Button(root13, text='F, S', command=ans1, padx=10, pady=10, fg='white', bg='green',font=('Comic Sans MS', 10, 'bold'))
    but_wans3 = Button(root13, text='A, D', command=ans1, padx=10, pady=10, fg='white', bg='green',font=('Comic Sans MS', 10, 'bold'))

    but_ans.grid(row=1, column=2)
    but_wans3.grid(row=2, column=2)
    but_wans2.grid(row=2, column=1)
    but_wans1.grid(row=1, column=1)

    lab_flower = Label(root13, image=img_flower)
    lab_orange = Label(root13, image=img_orange)

    lab_flower.grid(row=1, column=0)
    lab_orange.grid(row=1, column=3)

    lable.grid(row=0, columnspan=4)
    root13.mainloop()


def eq2():
    root13.destroy()
    global root14
    root14 = Tk()
    canvas = Canvas(root14, width=700, height=400, bg='light green')
    canvas.grid(columnspan=4, rowspan=3)
    root14.title('First steps')

    lable = Label(root14, text='Click the missing letters.', justify=CENTER, font=('Comic Sans MS', 25), fg='purple', bg='light green')

    lab_1 = Label(root14, text='APP_E', font=('Comic Sans MS', 25), fg='red', bg='light green')
    lab_2 = Label(root14, text='CHI_DREN', font=('Comic Sans MS', 25), fg='blue', bg='light green')

    def ans1():
        global i1
        i1 = i
        eq3()

    def ans():
        global i1
        i1 = i + 1
        eq3()

    but_ans = Button(root14, text='L, L', command=ans, padx=10, pady=10, fg='white', bg='green', font=('Comic Sans MS', 10, 'bold'))
    but_wans1 = Button(root14, text='N, L', command=ans1, padx=10, pady=10, fg='white', bg='green',font=('Comic Sans MS', 10, 'bold'))
    but_wans2 = Button(root14, text='D, S', command=ans1, padx=10, pady=10, fg='white', bg='green',font=('Comic Sans MS', 10, 'bold'))
    but_wans3 = Button(root14, text='O, V', command=ans1, padx=10, pady=10, fg='white', bg='green',font=('Comic Sans MS', 10, 'bold'))

    but_ans.grid(row=1, column=2)
    but_wans3.grid(row=2, column=2)
    but_wans2.grid(row=2, column=1)
    but_wans1.grid(row=1, column=1)

    lab_1.grid(row=1, column=0)
    lab_2.grid(row=1, column=3)

    lable.grid(row=0, columnspan=4)
    root14.mainloop()


def eq3():
    root14.destroy()
    global root15
    root15 = Tk()
    canvas = Canvas(root15, width=700, height=400, bg='light green')
    canvas.grid(columnspan=3, rowspan=3)
    root15.title('First steps')

    la_title = Label(root15, text='Select the rhyming word for the following.', justify=CENTER,font=('Comic Sans MS', 25), fg='purple', bg='light green')
    la_word = Label(root15, text='BOX', justify=CENTER, font=('Comic Sans MS', 30), fg='brown', bg='light green')

    r1 = IntVar()
    r1.get()
    r2 = IntVar()
    r2.get()
    r3 = IntVar()
    r3.get()

    def ans1():
        global i2
        i2 = i1
        eq4()

    def ans():
        global i2
        i2 = i1 + 1
        eq4()

    b1 = Radiobutton(root15, text='pin', command=ans1, variable=r1, value=1, font=('Comic Sans MS', 25), fg='green', bg='light green')
    b2 = Radiobutton(root15, text='fox', command=ans, variable=r2, value=1, font=('Comic Sans MS', 25), fg='green', bg='light green')
    b3 = Radiobutton(root15, text='rat', command=ans1, variable=r3, value=1, font=('Comic Sans MS', 25), fg='green', bg='light green')

    b1.grid(row=2, column=0)
    b2.grid(row=2, column=1)
    b3.grid(row=2, column=2)

    la_word.grid(row=1, columnspan=3)
    la_title.grid(row=0, columnspan=3)
    root15.mainloop()


def eq4():
    root15.destroy()
    global root21
    root21 = Tk()
    canvas = Canvas(root21, width=700, height=400, bg='light green')
    canvas.grid(columnspan=8, rowspan=4)
    root21.title('First steps')

    la_title = Label(root21, text='Complete the given puzzle.', justify=CENTER, font=('Comic Sans MS', 25), fg='purple', bg='light green')

    la = Label(root21, text='E', justify=CENTER, font=('Comic Sans MS', 25), fg='red', bg='light green')
    la1 = Label(root21, text='_', justify=CENTER, font=('Comic Sans MS', 25), fg='red', bg='light green')
    la2 = Label(root21, text='R', justify=CENTER, font=('Comic Sans MS', 25), fg='red', bg='light green')

    la3 = Label(root21, text='H', justify=RIGHT, font=('Comic Sans MS', 25), fg='blue', bg='light green')
    la4 = Label(root21, text='N', justify=LEFT, font=('Comic Sans MS', 25), fg='blue', bg='light green')
    la5 = Label(root21, text='D', justify=LEFT, font=('Comic Sans MS', 25), fg='blue', bg='light green')

    img_hand = ImageTk.PhotoImage(Image.open('img/1.jpg'))
    img_ear = ImageTk.PhotoImage(Image.open('img/3.jpg'))
    lab_i1 = Label(root21, image=img_hand)
    lab_i2 = Label(root21, image=img_ear)

    def ans1():
        global i3
        i3 = i2
        result_p_e()

    def ans():
        global i3
        i3 = i2 + 1
        result_p_e()

    but_e = Button(root21, command=ans1, text='E', justify=CENTER, font=('Comic Sans MS', 15), fg='whitesmoke', bg='brown')
    but_o = Button(root21, command=ans1, text='O', justify=CENTER, font=('Comic Sans MS', 15), fg='whitesmoke', bg='brown')
    but_a = Button(root21, command=ans, text='A', justify=CENTER, font=('Comic Sans MS', 15), fg='whitesmoke', bg='brown')

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


def mat():
    global result
    result = 0
    mq1()


def mq1():
    global root16
    root16 = Tk()
    canvas = Canvas(root16, width=700, height=400, bg='#FFCBCB')
    canvas.grid(columnspan=4, rowspan=3)
    root16.title('First steps')

    label = Label(root16, text='Choose the preceeding number of 8.', justify=CENTER, font=('Comic Sans MS', 25),fg='purple', bg='#FFCBCB')

    def ans1():
        global i
        i = result
        mq2()

    def ans():
        global i
        i = result + 1
        mq2()

    but_1 = Button(root16, text='4', command=ans1, padx=15, pady=15, fg='white', bg='green', font=('Comic Sans MS', 18, 'bold'))
    but_2 = Button(root16, text='9', command=ans1, padx=15, pady=15, fg='white', bg='green', font=('Comic Sans MS', 18, 'bold'))
    but_3 = Button(root16, text='7', command=ans, padx=15, pady=15, fg='white', bg='green', font=('Comic Sans MS', 18, 'bold'))
    but_4 = Button(root16, text='6', command=ans1, padx=15, pady=15, fg='white', bg='green', font=('Comic Sans MS', 18, 'bold'))

    but_1.grid(row=1, column=0)
    but_2.grid(row=1, column=1)
    but_3.grid(row=1, column=2)
    but_4.grid(row=1, column=3)

    label.grid(row=0, columnspan=4)
    root16.mainloop()


def mq2():
    root16.destroy()
    global root17
    root17 = Tk()
    canvas = Canvas(root17, width=700, height=400, bg='#FFCBCB')
    canvas.grid(columnspan=4, rowspan=3)
    root17.title('First steps')

    label = Label(root17, text='Choose the succeeding number of 4.', justify=CENTER, font=('Comic Sans MS', 25),fg='purple', bg='#FFCBCB')

    def ans1():
        global i1
        i1 = i
        mq3()

    def ans():
        global i1
        i1 = i + 1
        mq3()

    but_1 = Button(root17, text='5', command=ans, padx=15, pady=15, fg='white', bg='green', font=('Comic Sans MS', 18, 'bold'))
    but_2 = Button(root17, text='3', command=ans1, padx=15, pady=15, fg='white', bg='green', font=('Comic Sans MS', 18, 'bold'))
    but_3 = Button(root17, text='2', command=ans1, padx=15, pady=15, fg='white', bg='green', font=('Comic Sans MS', 18, 'bold'))
    but_4 = Button(root17, text='6', command=ans1, padx=15, pady=15, fg='white', bg='green', font=('Comic Sans MS', 18, 'bold'))

    but_1.grid(row=1, column=0)
    but_2.grid(row=1, column=1)
    but_3.grid(row=1, column=2)
    but_4.grid(row=1, column=3)

    label.grid(row=0, columnspan=4)
    root17.mainloop()


def mq3():
    root17.destroy()
    global root18
    root18 = Tk()
    canvas = Canvas(root18, width=700, height=400, bg='#FFCBCB')
    canvas.grid(columnspan=4, rowspan=3)
    root18.title('First steps')

    label = Label(root18, text='Choose the correct option.', justify=CENTER, font=('Comic Sans MS', 25), fg='purple',bg='#FFCBCB')
    label1 = Label(root18, text='4 + _ = 9', justify=CENTER, font=('Comic Sans MS', 35), fg='purple', bg='#FFCBCB')

    def ans1():
        global i2
        i2 = i1
        mq4()

    def ans():
        global i2
        i2 = i1 + 1
        mq4()

    but_1 = Button(root18, text='4', command=ans1, padx=15, pady=15, fg='white', bg='green', font=('Comic Sans MS', 18, 'bold'))
    but_2 = Button(root18, text='7', command=ans1, padx=15, pady=15, fg='white', bg='green', font=('Comic Sans MS', 18, 'bold'))
    but_3 = Button(root18, text='5', command=ans, padx=15, pady=15, fg='white', bg='green', font=('Comic Sans MS', 18, 'bold'))
    but_4 = Button(root18, text='3', command=ans1, padx=15, pady=15, fg='white', bg='green', font=('Comic Sans MS', 18, 'bold'))

    but_1.grid(row=2, column=0)
    but_2.grid(row=2, column=1)
    but_3.grid(row=2, column=2)
    but_4.grid(row=2, column=3)

    label1.grid(row=1, columnspan=4)
    label.grid(row=0, columnspan=4)
    root18.mainloop()


def mq4():
    root18.destroy()
    global root19
    root19 = Tk()
    canvas = Canvas(root19, width=700, height=400, bg='#FFCBCB')
    canvas.grid(columnspan=4, rowspan=3)
    root19.title('First steps')

    label = Label(root19, text='Choose the correct option.', justify=CENTER, font=('Comic Sans MS', 25), fg='purple',bg='#FFCBCB')
    label1 = Label(root19, text='3 _ 2 = 1', justify=CENTER, font=('Comic Sans MS', 35), fg='purple', bg='#FFCBCB')

    def ans1():
        global i3
        i3 = i2
        mq5()

    def ans():
        global i3
        i3 = i2 + 1
        mq5()

    but_1 = Button(root19, text='-', command=ans, padx=15, pady=15, fg='white', bg='green', font=('Comic Sans MS', 18, 'bold'))
    but_2 = Button(root19, text='+', command=ans1, padx=15, pady=15, fg='white', bg='green', font=('Comic Sans MS', 18, 'bold'))
    but_3 = Button(root19, text='x', command=ans1, padx=15, pady=15, fg='white', bg='green', font=('Comic Sans MS', 18, 'bold'))
    but_4 = Button(root19, text='%', command=ans1, padx=15, pady=15, fg='white', bg='green', font=('Comic Sans MS', 18, 'bold'))

    but_1.grid(row=2, column=0)
    but_2.grid(row=2, column=1)
    but_3.grid(row=2, column=2)
    but_4.grid(row=2, column=3)

    label1.grid(row=1, columnspan=4)
    label.grid(row=0, columnspan=4)
    root19.mainloop()

def mq5():
    root19.destroy()
    global root20
    root20 = Tk()
    canvas = Canvas(root20, width=700, height=400, bg='#FFCBCB')
    canvas.grid(columnspan=4, rowspan=3)
    root20.title('First steps')

    label = Label(root20, text='Choose the correct number name.', justify=CENTER, font=('Comic Sans MS', 25),fg='purple', bg='#FFCBCB')
    label1 = Label(root20, text='7', justify=CENTER, font=('Comic Sans MS', 35), fg='purple', bg='#FFCBCB')

    def ans1():
        global i4
        i4 = i3
        result_p_m()

    def ans():
        global i4
        i4 = i3 + 1
        result_p_m()

    but_1 = Button(root20, text='TWO', command=ans1, padx=15, pady=15, fg='white', bg='green', font=('Comic Sans MS', 18, 'bold'))
    but_2 = Button(root20, text='ELEVEN', command=ans1, padx=15, pady=15, fg='white', bg='green', font=('Comic Sans MS', 18, 'bold'))
    but_3 = Button(root20, text='TWENTY', command=ans1, padx=15, pady=15, fg='white', bg='green', font=('Comic Sans MS', 18, 'bold'))
    but_4 = Button(root20, text='SEVEN', command=ans, padx=15, pady=15, fg='white', bg='green', font=('Comic Sans MS', 18, 'bold'))

    but_1.grid(row=2, column=0)
    but_2.grid(row=2, column=1)
    but_3.grid(row=2, column=2)
    but_4.grid(row=2, column=3)

    label1.grid(row=1, columnspan=4)
    label.grid(row=0, columnspan=4)
    root20.mainloop()


def mark_sheet():
    root9 = Tk()
    canvas = Canvas(root9, width=900, height=400, bg='light yellow')
    canvas.grid(columnspan=4, rowspan=4)
    root9.title('First steps')

    la_sno = Label(root9, text='roll number', justify=CENTER, font=('Comic Sans MS', 25), fg='purple', bg='light yellow')
    la_name = Label(root9, text='Student name', justify=CENTER, font=('Comic Sans MS', 25), fg='purple', bg='light yellow')
    la_mark = Label(root9, text='Mark', justify=CENTER, font=('Comic Sans MS', 25), fg='purple', bg='light yellow')
    la_year = Label(root9, text='Academic year', justify=CENTER, font=('Comic Sans MS', 25), fg='purple', bg='light yellow')

    text = StringVar()
    text1 = StringVar()
    text2 = StringVar()
    text3 = StringVar()

    e_roll = Entry(root9, width=20, textvariable=text, justify=CENTER, font=('Comic Sans MS', 13))
    e_name = Entry(root9, width=20, textvariable=text1, justify=CENTER, font=('Comic Sans MS', 13))
    e_mark = Entry(root9, width=20, textvariable=text2, justify=CENTER, font=('Comic Sans MS', 13))
    e_year = Entry(root9, width=20, textvariable=text3, justify=CENTER, font=('Comic Sans MS', 13))

    def add():
        r = e_roll.get()
        n = e_name.get()
        m = e_mark.get()
        y = e_year.get()
        qur = "insert into mark_sheet values('%s', '%s', '%s', '%s')" % (r, n, m, y)
        cur.execute(qur)
        db.commit()
        mb.showinfo("Message", "Added successfully")

    def delete():
        r = e_roll.get()
        qur1 = "delete from mark_sheet where roll_no = '%s'" % r
        cur.execute(qur1)
        db.commit()
        mb.showinfo("Message", "Deleted successfully")

    def update():
        r = e_roll.get()
        n = e_name.get()
        m = e_mark.get()
        y = e_year.get()
        qur2 = "update mark_sheet set name = '%s' where roll_no = '%s'" % (n, r)
        qur3 = "update mark_sheet set mark = '%s' where roll_no = '%s'" % (m, r)
        cur.execute(qur2, qur3)
        db.commit()
        mb.showinfo("Message", "Updated successfully")

    def close():
        root9.destroy()

    b_add = Button(root9, text='ADD', command=add, padx=15, pady=10, fg='green', font=('Comic Sans MS', 10, 'bold'))
    b_update = Button(root9, text='UPDATE', command=update, padx=15, pady=10, fg='green', font=('Comic Sans MS', 10, 'bold'))
    b_delete = Button(root9, text='DELETE', command=delete, padx=15, pady=10, fg='green', font=('Comic Sans MS', 10, 'bold'))
    b_close = Button(root9, text='CLOSE', command=close, padx=15, pady=10, fg='green', font=('Comic Sans MS', 10, 'bold'))

    la_sno.grid(row=0, column=0)
    la_name.grid(row=0, column=1)
    la_mark.grid(row=0, column=2)
    la_year.grid(row=0, column=3)

    e_roll.grid(row=1, column=0)
    e_name.grid(row=1, column=1)
    e_mark.grid(row=1, column=2)
    e_year.grid(row=1, column=3)

    b_add.grid(row=2, column=0)
    b_update.grid(row=2, column=1)
    b_delete.grid(row=2, column=2)
    b_close.grid(row=2, column=3)

    root9.mainloop()


def login_page():
    global e
    global e1
    global e2
    root.destroy()
    root2 = Tk()

    canvas2 = Canvas(root2, width=700, height=400, bg='light yellow')
    canvas2.grid(columnspan=3, rowspan=9)
    root2.title('login')

    la_heading = Label(root2, text='Create Your account', justify=CENTER, font=('Comic Sans MS', 20), fg='violet', bg='light yellow')
    la_name = Label(root2, text='Name:', justify=CENTER, font=('Comic Sans MS', 15), fg='red', bg='light yellow')
    la_username = Label(root2, text='Username:', justify=CENTER,font=('Comic Sans MS', 15), fg='red', bg='light yellow')
    la_password = Label(root2, text='Password:', justify=CENTER, font=('Comic Sans MS', 15), fg='red', bg='light yellow')

    text = StringVar()
    text1 = StringVar()
    text2 = StringVar()

    e = Entry(root2, width=20, textvariable=text, justify=CENTER, font=('Comic Sans MS', 13))
    e1 = Entry(root2, width=20, textvariable=text1, justify=CENTER, font=('Comic Sans MS', 13))
    e2 = Entry(root2, width=20, textvariable=text2, justify=CENTER, font=('Comic Sans MS', 13))

    def back():
        root2.destroy()
        main()

    def log():
        n = e.get()
        u = e1.get()
        p = e2.get()
        l = len(p)
        qur = "select user_id from login"
        df = pd.read_sql(qur, db)
        check = df.isin([u]).any().any()
        if check:
            mb.showwarning("Warning!!!", "The username already exist")
        elif n == "":
            mb.showwarning("Warning!!!", "Name is required!")
        elif u == "":
            mb.showwarning("Warning!!!", "Username is required!")
        elif p == "":
            mb.showwarning("Warning!!!", "Enter the password!")
        elif l > 8:
            mb.showwarning("Warning!!!", "password should contain only 8 characters")
        elif l < 8:
            mb.showwarning("Warning!!!", "password should contain 8 characters")
        else:
            qur1 = "insert into login values('%s', '%s', '%s')" % (n, u, p)
            cur.execute(qur1)
            db.commit()
            root2.destroy()
            home_page()

    but_sub = Button(root2, text='SUBMIT', command=lambda: log(), padx=15, pady=10, fg='green', bg='light pink', font=('Comic Sans MS', 10, 'bold'))
    but_back = Button(root2, text='BACK', command=back, padx=15, pady=10, fg='green', bg='light pink', font=('Comic Sans MS', 10, 'bold'))

    la_heading.grid(row=0, column=1)
    la_name.grid(row=1, column=1)
    e.grid(row=2, column=1, pady=10)

    la_username.grid(row=3, column=1)
    e1.grid(row=4, column=1, pady=10)

    la_password.grid(row=5, column=1)
    e2.grid(row=6, column=1, pady=10)

    but_sub.grid(row=7, column=2)
    but_back.grid(row=7, column=0)

    root2.mainloop()


def sign_in():
    root.destroy()
    root1 = Tk()

    canvas1 = Canvas(root1, width=700, height=400, bg='light green')
    canvas1.grid(columnspan=3, rowspan=9)
    root1.title('sign in')

    la_heading = Label(root1, text='Sign in', justify=CENTER, font=('Comic Sans MS', 20), fg='red', bg='light green')
    la_username = Label(root1, text='Username:', justify=CENTER, font=('Comic Sans MS', 15), fg='red', bg='light green')
    la_password = Label(root1, text='Password:', justify=CENTER, font=('Comic Sans MS', 15), fg='red', bg='light green')

    text1 = StringVar()
    text2 = StringVar()

    e1 = Entry(root1, width=20, textvariable=text1, justify=CENTER, font=('Comic Sans MS', 13))
    e2 = Entry(root1, width=20, textvariable=text2, justify=CENTER, font=('Comic Sans MS', 13))

    def back():
        root1.destroy()
        main()

    def log1():
        u = e1.get()
        p = e2.get()
        qur = "select user_id from login"
        df = pd.read_sql(qur, db)
        check = df.isin([u]).any().any()
        qur1 = "select password from login"
        df1 = pd.read_sql(qur1, db)
        check1 = df1.isin([p]).any().any()
        if check and check1:
            qur1 = "insert into log values('%s', now())" % u
            cur.execute(qur1)
            db.commit()
            root1.destroy()
            home_page()
        else:
            mb.showwarning("Warning!!!", "Account details are not correct!")

    but = Button(root1, text='SUBMIT', command=lambda: log1(), padx=15, pady=10, fg='green', bg='light pink', font=('Comic Sans MS', 10, 'bold'))
    but_back = Button(root1, text='BACK', command=back, padx=15, pady=10, fg='green', bg='light pink', font=('Comic Sans MS', 10, 'bold'))

    la_heading.grid(row=0, column=1)

    la_username.grid(row=3, column=1)
    e1.grid(row=4, column=1, pady=10)

    la_password.grid(row=5, column=1)
    e2.grid(row=6, column=1, pady=10)

    but.grid(row=7, column=2)
    but_back.grid(row=7, column=0)

    root1.mainloop()


def main():
    global root
    root = Tk()
    canvas = Canvas(root, width=700, height=400, bg='Whitesmoke')
    canvas.grid(columnspan=3, rowspan=3)
    root.title('First steps')

    logo = Image.open('logo.jpeg')
    resized_image = logo.resize((250, 205))
    logo_img = ImageTk.PhotoImage(resized_image)
    logo_label = Label(image=logo_img)
    logo_label.grid(row=0, column=1)

    but = Button(text='Create new account', command=login_page, width=15, pady=15, padx=15, fg='blue', bg='light pink', font=('Comic Sans MS', 15, 'bold'))
    but1 = Button(text='Sign in', command=sign_in, width=15, pady=15, padx=15, fg='blue', bg='light pink', font=('Comic Sans MS', 15, 'bold'))

    but.grid(row=1, column=0)
    but1.grid(row=1, column=2)

    root.mainloop()
main()