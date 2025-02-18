import tkinter as tk
from tkinter import messagebox
import math
import pickle

# Guardar el estado en un archivo
def save_state(entry, history):
    state = {
        "entry": entry,
        "history": history
    }
    with open("calculator_state.pkl", "wb") as f:
        pickle.dump(state, f)

# Cargar el estado desde un archivo
def load_state():
    try:
        with open("calculator_state.pkl", "rb") as f:
            state = pickle.load(f)
            return state["entry"], state["history"]
    except FileNotFoundError:
        return "", ""  # Si no existe el archivo, retornar valores por defecto

def on_click(button_text):
    global new_result
    if button_text == "AC":
        entry_var.set("")
        history_var.set("")
        new_result = False
    elif button_text == "←":
        entry_var.set(entry_var.get()[:-1])
    elif button_text == "=":
        try:
            expression = entry_var.get().replace("×", "*").replace("÷", "/").replace("^", "**")
            if expression and not expression.endswith("=") and "=" not in history_var.get().split("\n")[-1]:
                result = eval(expression,
                              {"sin": math.sin, "cos": math.cos, "tan": math.tan, "log": math.log10, "ln": math.log,
                               "sqrt": math.sqrt, "pi": math.pi, "e": math.e, "factorial": math.factorial,
                               "deg": math.degrees})
                history_var.set(history_var.get() + expression + " = " + str(result) + "\n")
                entry_var.set(str(result))
                new_result = True
        except Exception as e:
            messagebox.showerror("Error", "Expresión inválida")
    else:
        if new_result:
            if button_text.isdigit() or button_text in ["sin", "cos", "tan", "lg", "ln", "deg", "sqrt", "x^y"]:
                entry_var.set("")
            new_result = False

        current_text = entry_var.get()
        if button_text in ["sin", "cos", "tan", "lg", "ln", "deg"]:
            entry_var.set(current_text + button_text + "(")
        elif button_text == "x^y":
            if current_text and current_text[-1].isdigit():
                entry_var.set(current_text + "^")
        elif button_text.isdigit():
            if current_text and current_text[-1] == "0" and (len(current_text) == 1 or not current_text[-2].isdigit()):
                entry_var.set(current_text[:-1] + button_text)
            else:
                entry_var.set(current_text + button_text)
        else:
            entry_var.set(current_text + button_text)

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora Científica")
root.geometry("400x600")
root.configure(bg="#2E2E2E")  # Color de fondo oscuro para comodidad visual

# Cargar el estado anterior
entry_text, history_text = load_state()

entry_var = tk.StringVar(value=entry_text)
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), justify="right", bd=10, relief=tk.GROOVE,
                 bg="#A4A4A4", fg="black")
entry.pack(fill="both")

# Área de historial
history_var = tk.StringVar(value=history_text)
history_label = tk.Label(root, textvariable=history_var, font=("Arial", 12), justify="left", anchor="w", height=5,
                         bg="#6E6E6E", fg="white")
history_label.pack(fill="both")

new_result = False  # Bandera para borrar el resultado al escribir un nuevo número

# Crear botones con diseño similar a la imagen
buttons = [
    ("2nd", "deg", "sin", "cos", "tan"),
    ("x^y", "lg", "ln", "(", ")"),
    ("sqrt", "AC", "←", "%", "÷"),
    ("x!", "7", "8", "9", "×"),
    ("1/x", "4", "5", "6", "-"),
    ("pi", "1", "2", "3", "+"),
    ("e", "0", ".", "=", "")
]

frame = tk.Frame(root, bg="#2E2E2E")
frame.pack(expand=True, fill="both")

for row_values in buttons:
    row_frame = tk.Frame(frame, bg="#2E2E2E")
    row_frame.pack(expand=True, fill="both")
    for value in row_values:
        if value:  # Evitar botones vacíos
            button = tk.Button(row_frame, text=value, font=("Arial", 15), command=lambda v=value: on_click(v), width=5,
                               height=2, bg="#424242", fg="white", activebackground="#585858", activeforeground="white")
            button.pack(side="left", expand=True, fill="both")

# Guardar el estado al cerrar la ventana
def on_close():
    save_state(entry_var.get(), history_var.get())
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_close)

root.mainloop()
