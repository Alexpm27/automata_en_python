import tkinter as tk
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt


def validar_matricula_estados(matricula):
    state = 0
    texto = tk.StringVar()
    for character in matricula:

        texto.set(texto.get() + "->q" + str(state))
        states.config(textvariable=texto)
        if state == 0:
            if character == 'U':
                state = 1
            elif character == 'V':
                state = 4
            else:
                return False
        elif state == 1:
            if character >= 'M':
                state = 2
            else:
                return False
        elif state == 2:
            if character == '-':
                state = 3
            else:
                return False
        elif state == 3:
            if character == '0':
                state = 8
            elif character <= '9':
                state = 5
            else:
                return False
        elif state == 4:
            if character <= 'K':
                state = 2
            else:
                return False
        elif state == 5:
            if character <= '9':
                state = 6
            else:
                return False
        elif state == 6:
            if character <= '9':
                state = 7
            else:
                return False
        elif state == 7:
            if character <= '9':
                state = 14
            else:
                return False
        elif state == 8:
            if character == '0':
                state = 9
            elif character <= '9':
                state = 11
            else:
                return False
        elif state == 9:
            if character == '0':
                state = 10
            elif character <= '9':
                state = 13
            else:
                return False
        elif state == 10:
            if character >= '1':
                state = 14
            else:
                return False
        elif state == 11:
            if character <= '9':
                state = 12
            else:
                return False
        elif state == 12:
            if character <= '9':
                state = 14
            else:
                return False
        elif state == 13:
            if character <= '9':
                state = 14
            else:
                return False
        elif state == 14:
            if character == '-':
                state = 15
            else:
                return False
        elif state == 15:
            if character <= 'Z':
                state = 16
            else:
                return False
        elif state == 16:
            return False

    return state == 16


def validar_matricula():
    matricula = entrada_matricula.get()

    if validar_matricula_estados(matricula):
        messagebox.showinfo("Validación", f"La matrícula {matricula} es válida.")
    else:
        messagebox.showerror("Validación", f"La matrícula {matricula} no es válida.")


# Crear la ventana
ventana = tk.Tk()
ventana.title("Validador de Matrículas")

# Etiqueta
etiqueta = tk.Label(ventana, text="Ingrese la matrícula:")
etiqueta.pack()

# Campo de entrada
entrada_matricula = tk.Entry(ventana)
entrada_matricula.pack()

# Botón de validación
boton_validar = tk.Button(ventana, text="Validar", command=validar_matricula)
boton_validar.pack()

states = tk.Label(ventana, text=" ")
states.pack()

ventana.mainloop()
