import tkinter as tk


def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(screen.get())
            screen_var.set(result)
        except Exception as e:
            screen_var.set("Erro")
    elif text == "C":
        screen_var.set("")
    else:
        screen_var.set(screen.get() + text)


root = tk.Tk()
root.title("Calculadora")
root.geometry("350x500")


root.configure(bg='#ffe6f2')  


screen_var = tk.StringVar()
screen = tk.Entry(root, textvar=screen_var, font="Arial 24 bold", bg='#ff99cc', fg='#FFF', borderwidth=0, relief="solid")
screen.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)


buttons_frame = tk.Frame(root, bg='#ffe6f2')  
buttons_frame.pack()

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', 'C', '=', '+']
]

for row in buttons:
    button_row = tk.Frame(buttons_frame, bg='#ffe6f2')  
    button_row.pack()
    for button_text in row:
        button = tk.Button(button_row, text=button_text, font="Arial 18 bold", width=4, height=2,
                           bg='#ff66b2', fg='#FFF', activebackground='#ff80bf', activeforeground='#FFF', borderwidth=0)
        button.pack(side=tk.LEFT, padx=5, pady=5)
        button.bind("<Button-1>", click)


root.mainloop()
