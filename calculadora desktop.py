import tkinter as tk

def adicionar(valor):
    atual = visor.get()
    visor.delete(0, tk.END)
    visor.insert(0, atual + valor)

def calcular():
    try:
        resultado = eval(visor.get())
        visor.delete(0, tk.END)
        visor.insert(0, str(resultado))
    except:
        visor.delete(0, tk.END)
        visor.insert(0, "Erro")

def limpar():
    visor.delete(0, tk.END)

app = tk.Tk()
app.title("Calculadora Braba")
app.configure(bg="#1C1C1E")

visor = tk.Entry(app, font=("Segoe UI", 24), bd=5, relief="flat", justify="right", bg="#2C2C2E", fg="white")
visor.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipady=10)

botoes = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3),
    ('C',5,0)
]
for (txt, r, c) in botoes:
    if txt == '=':
        btn = tk.Button(app, text=txt, width=5, height=2, font=("Segoe UI", 18),
                        bg="#30D158", fg="black", command=calcular)
    elif txt == 'C':
        btn = tk.Button(app, text=txt, width=25, height=2, font=("Segoe UI", 14),
                        bg="#FF3B30", fg="white", command=limpar)
        btn.grid(row=r, column=c, columnspan=4, padx=10, pady=10)
        continue
    else:
        btn = tk.Button(app, text=txt, width=5, height=2,
                font=("Segoe UI", 20, "bold"), 
                bg="#3A3A3C", fg="white",
                relief="flat", bd=0,
                highlightthickness=0,
                activebackground="#48484A",
                command=lambda t=txt: adicionar(t))

    btn.grid(row=r, column=c, padx=5, pady=5)

app.mainloop()
