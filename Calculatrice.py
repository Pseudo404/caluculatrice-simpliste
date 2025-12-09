import math
import customtkinter

app = customtkinter.CTk()
app.geometry("320x290")

customtkinter.set_default_color_theme("dark-blue")

ch = ""

def un():
    global ch
    ch += "1"
    label.configure(text=f"{ch}")
def deux():
    global ch
    ch += "2"
    label.configure(text=f"{ch}")
def trois():
    global ch
    ch += "3"
    label.configure(text=f"{ch}")
def quatre():
    global ch
    ch += "4"
    label.configure(text=f"{ch}")
def cinque():
    global ch
    ch += "5"
    label.configure(text=f"{ch}")
def six():
    global ch
    ch += "6"
    label.configure(text=f"{ch}")
def sept():
    global ch
    ch += "7"
    label.configure(text=f"{ch}")
def huit():
    global ch
    ch += "8"
    label.configure(text=f"{ch}")
def neuf():
    global ch
    ch += "9"
    label.configure(text=f"{ch}")
def zero():
    global ch
    ch += "0"
    label.configure(text=f"{ch}")
def moins():
    global ch
    ch += "-"
    label.configure(text=f"{ch}")
def plus():
    global ch
    ch += "+"
    label.configure(text=f"{ch}")
def virgule():
    global ch
    ch += "."
    label.configure(text=f"{ch}")
def fois():
    global ch
    ch += "*"
    label.configure(text=f"{ch}")
def divise():
    global ch
    ch += "/"
    label.configure(text=f"{ch}")
def egal():
    global ch
    try:
        result = str(eval(ch))
        ch = result
    except:
        ch = "Erreur"
    label.configure(text=f"{ch}")
def backspaces():
    global ch
    ch = ch[:len(ch)-1:]
    label.configure(text=f"{ch}")
def resets():
    global ch
    ch = ""
    label.configure(text=f"{ch}")

label = customtkinter.CTkLabel(app, text="", fg_color="transparent", font=("Arial", 24), anchor='ne', width=200)

k=0
for j in range(4):
    for i in range(4):
        liste = [7, 8, 9, '+', 4, 5, 6, '-', 1, 2, 3, 'x', "=",  0, ',', '/']
        liste_event= [sept, huit, neuf, plus, quatre, cinque, six, moins, un, deux, trois, fois, egal, zero, virgule, divise]
        
        button = customtkinter.CTkButton(app, text=f"{liste[k]}", width=77, height=45, command=liste_event[k])
        button.grid(row=j+4, column=i, padx=2, pady=2)
        k += 1

backspace = customtkinter.CTkButton(app, text=f"⌫", width=77, height=40, command=backspaces)
backspace.grid(row=1, column=i, padx=2, pady=2)

reset = customtkinter.CTkButton(app, text=f"C", width=77, height=40, command=resets)
reset.grid(row=1, column=i-1, padx=2, pady=2)

label.grid(row=0, column=0, columnspan=10, padx=10, pady=10, sticky="we")

app.grid_columnconfigure(3, weight=1)
app.grid_rowconfigure(3, weight=1)
app.mainloop()
