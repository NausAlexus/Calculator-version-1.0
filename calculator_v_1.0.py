from tkinter import *

window = Tk()
window.title('Калькулятор Орлов А.В. version 1.0')
window.geometry('500x580+700+100')
window.resizable(False, False)


def input_into_entry(symbol):
    entry.insert(END, symbol)


def clear():
    entry.delete(0, END)


def erase():
    entry.delete(entry.index(END) - 1)


def count_result():
    text = entry.get()
    result = 0

    if '+' in text:
        try:
            splitted_text = text.split('+')
            first = float(splitted_text[0])
            second = float(splitted_text[1])
            result = first+second
        except ValueError:
            result = 0

    if '-' in text:
        try:
            splitted_text = text.split('-')
            first = float(splitted_text[0])
            second = float(splitted_text[1])
            result = first-second
        except ValueError:
            result

    if '/' in text:
        try:
            splitted_text = text.split('/')
            first = float(splitted_text[0])
            second = float(splitted_text[1])
            result = first/second
        except ZeroDivisionError:
            result = ('Eror')
        except ValueError:
            result = 0

    if 'x' in text:
        try:
            splitted_text = text.split('x')
            first = float(splitted_text[0])
            second = float(splitted_text[1])
            result = first*second
        except ValueError:
            result = 0
    clear()
    entry.insert(0, result)


entry = Entry(window, width=20, font=('', 20))
entry.place(x=152, y=28, height=101)

btn1 = Button(window, bg='black', fg='white', text='1', font='Arial 20', command=lambda: input_into_entry('1'))
btn1.place(x=50, y=130, width=102, height=102)

btn2 = Button(window, bg='black', fg='white', text='2', font='Arial 20', command=lambda: input_into_entry('2'))
btn2.place(x=152, y=130, width=102, height=102)

btn3 = Button(window, bg='black', fg='white', text='3', font='Arial 20', command=lambda: input_into_entry('3'))
btn3.place(x=254, y=130, width=102, height=102)

btn4 = Button(window, bg='black', fg='white', text='4', font='Arial 20', command=lambda: input_into_entry('4'))
btn4.place(x=50, y=232, width=102, height=102)

btn5 = Button(window, bg='black', fg='white', text='5', font='Arial 20', command=lambda: input_into_entry('5'))
btn5.place(x=152, y=232, width=102, height=102)

btn6 = Button(window, bg='black', fg='white', text='6', font='Arial 20', command=lambda: input_into_entry('6'))
btn6.place(x=254, y=232, width=102, height=102)

btn7 = Button(window, bg='black', fg='white', text='7', font='Arial 20', command=lambda: input_into_entry('7'))
btn7.place(x=50, y=334, width=102, height=102)

btn8 = Button(window, bg='black', fg='white', text='8', font='Arial 20', command=lambda: input_into_entry('8'))
btn8.place(x=152, y=334, width=102, height=102)

btn9 = Button(window, bg='black', fg='white', text='9', font='Arial 20', command=lambda: input_into_entry('9'))
btn9.place(x=254, y=334, width=102, height=102)

btn0 = Button(window, bg='black', fg='white', text='0', font='Arial 20', command=lambda: input_into_entry('0'))
btn0.place(x=152, y=436, width=102, height=102)

btn_plus = Button(window, bg='black', fg='white', text='+', font='Arial 20', command=lambda: input_into_entry('+'))
btn_plus.place(x=356, y=130, width=102, height=102)

btn_minus = Button(window, bg='black', fg='white', text='-', font='Arial 20', command=lambda: input_into_entry('-'))
btn_minus.place(x=356, y=232, width=102, height=102)

btn_divide = Button(window, bg='black', fg='white', text='/', font='Arial 20', command=lambda: input_into_entry('/'))
btn_divide.place(x=356, y=334, width=102, height=102)

btn_multiply = Button(window, bg='black', fg='white', text='x', font='Arial 20', command=lambda: input_into_entry('x'))
btn_multiply.place(x=356, y=436, width=102, height=102)

btn_result = Button(window, bg='black', fg='white', text='=', font='Arial 20', command=count_result)
btn_result.place(x=254, y=436, width=102, height=102)

btn_clear = Button(window, bg='black', fg='white', text='CE', font='Arial 20', command=clear)
btn_clear.place(x=50, y=28, width=51, height=102)

btn_del = Button(window, bg='black', fg='white', text='del', font='Arial 20', command=erase)
btn_del.place(x=101, y=28, width=51, height=102)

btn_dot = Button(window, bg='black', fg='white', text='.', font='Arial 20', command=lambda: input_into_entry('.'))
btn_dot.place(x=50, y=436, width=102, height=102)


window.mainloop()