from tkinter import *
import math as m

window = Tk()
window.title("Scientific Calculator")
window.configure(bg="white")


def click(to_print):
    old = e.get()
    e.delete(0, END)
    e.insert(0, old + to_print)
    return


def sc(event):
    key = event.widget
    text = key['text']
    num = e.get()
    result = ''
    if text == 'deg':
        result = str(m.degrees(float(num)))
    if text == 'sin':
        result = str(m.sin(float(num)))
    if text == 'cos':
        result = str(m.cos(float(num)))
    if text == 'tan':
        result = str(m.tan(float(num)))
    if text == 'lg':
        result = str(m.log10(float(num)))
    if text == 'ln':
        result = str(m.log(float(num)))
    if text == 'Sqrt':
        result = str(m.sqrt(float(num)))
    if text == 'x!':
        result = str(m.factorial(int(num)))
    if text == '1/x':
        result = str(1 / (float(num)))
    if text == 'pi':
        if num == "":
            result = str(m.pi)
        else:
            result = str(float(num) * m.pi)
    if text == 'e':
        if num == "":
            result = str(m.e)
        else:
            result = str(m.e ** float(num))

    e.delete(0, END)
    e.insert(0, result)


def clear():
    e.delete(0, END)
    return


def backspace():
    current = e.get()
    length = len(current) - 1
    e.delete(length, END)


def evaluate():
    ans = e.get()
    ans = eval(ans)
    e.delete(0, END)
    e.insert(0, ans)


e = Entry(window, width=50, borderwidth=5, relief=RIDGE, fg="white", bg="black")
e.grid(row=0, column=0, columnspan=5, padx=10, pady=15)

lg = Button(window, text="lg", padx=28, pady=10, relief=RAISED)
lg.bind("<Button-1>", sc)
lg.grid(row=1, column=0)

ln = Button(window, text="ln", padx=28, pady=10, relief=RAISED)
ln.bind("<Button-1>", sc)
ln.grid(row=1, column=1)

parentheses1 = Button(window, text="(", padx=29, pady=10, relief=RAISED, command=lambda: click("("))
parentheses1.grid(row=1, column=2)

parentheses2 = Button(window, text=")", padx=30, pady=10, relief=RAISED, command=lambda: click(")"))
parentheses2.grid(row=1, column=3)

e_btn = Button(window, text="e", padx=29, pady=10, relief=RAISED)
e_btn.bind("<Button-1>", sc)
e_btn.grid(row=1, column=4)

exp = Button(window, text="^", padx=29, pady=10, relief=RAISED, command=lambda: click("^"))
exp.grid(row=2, column=0)

deg = Button(window, text="deg", padx=23, pady=10, relief=RAISED)
deg.bind("<Button-1>", sc)
deg.grid(row=2, column=1)

sin = Button(window, text="sin", padx=24, pady=10, relief=RAISED)
sin.bind("<Button-1>", sc)
sin.grid(row=2, column=2)

cos = Button(window, text="cos", padx=23, pady=10, relief=RAISED)
cos.bind("<Button-1>", sc)
cos.grid(row=2, column=3)

tan = Button(window, text="tan", padx=23, pady=10, relief=RAISED)
tan.bind("<Button-1>", sc)
tan.grid(row=2, column=4)

sqrt = Button(window, text="Sqrt", padx=23, pady=10, relief=RAISED)
sqrt.bind("<Button-1>", sc)
sqrt.grid(row=3, column=0)

clr = Button(window, text="C", padx=28, pady=10, relief=RAISED, command=clear)
clr.grid(row=3, column=1)

delete = Button(window, text="B", padx=28, pady=10, relief=RAISED, command=backspace)
delete.grid(row=3, column=2)

mod = Button(window, text="%", padx=28, pady=10, relief=RAISED, command=lambda: click("%"))
mod.grid(row=3, column=3)

div = Button(window, text="/", padx=29, pady=10, relief=RAISED, command=lambda: click("/"))
div.grid(row=3, column=4)

factorial = Button(window, text="x!", padx=29, pady=10, relief=RAISED)
factorial.bind("<Button-1>", sc)
factorial.grid(row=4, column=0)

seven = Button(window, text="7", padx=29, pady=10, relief=RAISED, command=lambda: click("7"))
seven.grid(row=4, column=1)

eight = Button(window, text="8", padx=29, pady=10, relief=RAISED, command=lambda: click("8"))
eight.grid(row=4, column=2)

nine = Button(window, text="9", padx=29, pady=10, relief=RAISED, command=lambda: click("9"))
nine.grid(row=4, column=3)

mul = Button(window, text="*", padx=29, pady=10, relief=RAISED, command=lambda: click("*"))
mul.grid(row=4, column=4)

frac = Button(window, text="1/x", padx=25, pady=10, relief=RAISED)
frac.bind("<Button-1>", sc)
frac.grid(row=5, column=0)

four = Button(window, text="4", padx=30, pady=10, relief=RAISED, command=lambda: click("4"))
four.grid(row=5, column=1)

five = Button(window, text="5", padx=29, pady=10, relief=RAISED, command=lambda: click("5"))
five.grid(row=5, column=2)

six = Button(window, text="6", padx=29, pady=10, relief=RAISED, command=lambda: click("6"))
six.grid(row=5, column=3)

sub = Button(window, text="-", padx=29, pady=10, relief=RAISED, command=lambda: click("-"))
sub.grid(row=5, column=4)

pi = Button(window, text="pi", padx=28, pady=10, relief=RAISED)
pi.bind("<Button-1>", sc)
pi.grid(row=6, column=0)

one = Button(window, text="1", padx=30, pady=10, relief=RAISED, command=lambda: click("1"))
one.grid(row=6, column=1)

two = Button(window, text="2", padx=29, pady=10, relief=RAISED, command=lambda: click("2"))
two.grid(row=6, column=2)

three = Button(window, text="3", padx=29, pady=10, relief=RAISED, command=lambda: click("3"))
three.grid(row=6, column=3)

add = Button(window, text="+", padx=28, pady=10, relief=RAISED, command=lambda: click("+"))
add.grid(row=6, column=4)

zero = Button(window, text="0", padx=30, pady=10, relief=RAISED, command=lambda: click("0"))
zero.grid(row=7, column=1)

dot = Button(window, text=".", padx=30, pady=10, relief=RAISED, command=lambda: click("."))
dot.grid(row=7, column=2)

equal = Button(window, text="=", padx=28, pady=10, relief=RAISED, command=evaluate)
equal.grid(row=7, column=3)

window.mainloop()
