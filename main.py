from tkinter import *
from tkinter import ttk

all_values = ''


# operaçoes
def enter_value(event):
    global all_values

    all_values += str(event)
    text_value.set(all_values)


def calculate():
    global all_values
    try:
        result = eval(all_values)
        text_value.set(str(result))
        all_values = str(result)
    except ZeroDivisionError:
        all_values = ''
        text_value.set('')
        return False
    except SyntaxError:
        return False


def clean():
    global all_values
    all_values = ''
    text_value.set('')


# definicao das cores
black = '#1e1f1e'
white = '#feffff'
blue = '#38576b'
gray = '#ECEFF1'
orange = '#FFAB40'

# criando a janela
window = Tk()
window.title('Calculadora')
icon = PhotoImage(file='logo.png')
window.iconphoto(True, icon)
window.geometry('235x310')
window.config(bg=black)

# criando os frames
window_frame = Frame(window, width=235, height=50, bg=blue)
window_frame.grid(row=0, column=0)

body_frame = Frame(window, width=235, height=268)
body_frame.grid(row=1, column=0)

# criando labels
text_value = StringVar()
app_label = Label(window_frame, textvariable=text_value, width=16, height=2, padx=7, relief=FLAT, anchor='e',
                  justify=RIGHT, font=('Ivy', 18), bg=blue, fg=white)
app_label.place(x=0, y=0)

# criando botoes

# Botao C
button_C = Button(body_frame, text='C', width=11, height=2, bg=gray, fg=black, font=('Ivy', 13, 'bold'), relief=RAISED,
                  overrelief=RIDGE, command=clean)
button_C.place(x=0, y=0)

# Porcentagem
b_percent = Button(body_frame, text='%', width=5, height=2, bg=gray, fg=black, font=('Ivy', 13, 'bold'), relief=RAISED,
                   overrelief=RIDGE, command=lambda: enter_value('%'))
b_percent.place(x=118, y=0)

# Divisao
b_division = Button(body_frame, text='/', width=5, height=2, bg=orange, fg=white, font=('Ivy', 13, 'bold'),
                    relief=RAISED, overrelief=RIDGE, command=lambda: enter_value('/'))
b_division.place(x=177, y=0)

# Botao 7
b_7 = Button(body_frame, text='7', width=5, height=2, bg=gray, fg=black, font=('Ivy', 13, 'bold'), relief=RAISED,
             overrelief=RIDGE, command=lambda: enter_value('7'))
b_7.place(x=0, y=52)

# Botao 8
b_8 = Button(body_frame, text='8', width=5, height=2, bg=gray, fg=black, font=('Ivy', 13, 'bold'), relief=RAISED,
             overrelief=RIDGE, command=lambda: enter_value('8'))
b_8.place(x=59, y=52)

# Botao 9
b_9 = Button(body_frame, text='9', width=5, height=2, bg=gray, fg=black, font=('Ivy', 13, 'bold'), relief=RAISED,
             overrelief=RIDGE, command=lambda: enter_value('9'))
b_9.place(x=118, y=52)

# Multiplicacao
b_mult = Button(body_frame, text='X', width=5, height=2, bg=orange, fg=white, font=('Ivy', 13, 'bold'),
                relief=RAISED, overrelief=RIDGE, command=lambda: enter_value('*'))
b_mult.place(x=177, y=52)

# Botao 6
b_6 = Button(body_frame, text='6', width=5, height=2, bg=gray, fg=black, font=('Ivy', 13, 'bold'), relief=RAISED,
             overrelief=RIDGE, command=lambda: enter_value('6'))
b_6.place(x=0, y=104)

# Botao 5
b_5 = Button(body_frame, text='5', width=5, height=2, bg=gray, fg=black, font=('Ivy', 13, 'bold'), relief=RAISED,
             overrelief=RIDGE, command=lambda: enter_value('5'))
b_5.place(x=59, y=104)

# Botao 4
b_4 = Button(body_frame, text='4', width=5, height=2, bg=gray, fg=black, font=('Ivy', 13, 'bold'), relief=RAISED,
             overrelief=RIDGE, command=lambda: enter_value('4'))
b_4.place(x=118, y=104)

# Subtracao
b_sub = Button(body_frame, text='-', width=5, height=2, bg=orange, fg=white, font=('Ivy', 13, 'bold'),
               relief=RAISED, overrelief=RIDGE, command=lambda: enter_value('-'))
b_sub.place(x=177, y=104)

# Botao 1
b_1 = Button(body_frame, text='1', width=5, height=2, bg=gray, fg=black, font=('Ivy', 13, 'bold'), relief=RAISED,
             overrelief=RIDGE, command=lambda: enter_value('1'))
b_1.place(x=0, y=156)

# Botao 2
b_2 = Button(body_frame, text='2', width=5, height=2, bg=gray, fg=black, font=('Ivy', 13, 'bold'), relief=RAISED,
             overrelief=RIDGE, command=lambda: enter_value('2'))
b_2.place(x=59, y=156)

# Botao 3
b_3 = Button(body_frame, text='3', width=5, height=2, bg=gray, fg=black, font=('Ivy', 13, 'bold'), relief=RAISED,
             overrelief=RIDGE, command=lambda: enter_value('3'))
b_3.place(x=118, y=156)

# Soma
b_sum = Button(body_frame, text='+', width=5, height=2, bg=orange, fg=white, font=('Ivy', 13, 'bold'),
               relief=RAISED, overrelief=RIDGE, command=lambda: enter_value('+'))
b_sum.place(x=177, y=156)

# Botao 0
button_0 = Button(body_frame, text='0', width=11, height=2, bg=gray, fg=black, font=('Ivy', 13, 'bold'), relief=RAISED,
                  overrelief=RIDGE, command=lambda: enter_value('0'))
button_0.place(x=0, y=208)

# Ponto
b_dot = Button(body_frame, text='.', width=5, height=2, bg=gray, fg=black, font=('Ivy', 13, 'bold'), relief=RAISED,
               overrelief=RIDGE, command=lambda: enter_value('.'))
b_dot.place(x=118, y=208)

# Igual
b_res = Button(body_frame, text='=', width=5, height=2, bg=orange, fg=white, font=('Ivy', 13, 'bold'),
               relief=RAISED, overrelief=RIDGE, command=calculate)
b_res.place(x=177, y=208)

window.mainloop()
