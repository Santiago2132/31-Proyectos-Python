import tkinter as tk
from tkinter import messagebox

#Ventana Principal
root = tk.Tk()
root.title("Lista de Tareas")
root.geometry("400x400")

#Funciones Principales
def agregar_tarea():
    tarea = entrada_tarea.get()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Debes ingresar una tarea.")

def eliminar_tarea():
    try:
        seleccion = lista_tareas.curselection()
        lista_tareas.delete(seleccion)
    except:
        messagebox.showwarning("Advertencia", "Debes seleccionar una tarea para eliminar.")

def marcar_completada():
    try:
        seleccion = lista_tareas.curselection()
        tarea = lista_tareas.get(seleccion)
        lista_tareas.delete(seleccion)
        lista_tareas.insert(seleccion,f"✓ {tarea}")
    except:
        messagebox.showwarning("Advertencia", "Debes seleccionar una tarea para marcar como completada.")

    
entrada_tarea = tk.Entry(root,width=40)
entrada_tarea.pack(pady=10)

boton_agregar = tk.Button(root, text="Agregar Tarea", command=agregar_tarea)
boton_agregar.pack(pady=5)

lista_tareas = tk.Listbox(root, width=40, height=10)
lista_tareas.pack(pady=10)

boton_eliminar = tk.Button(root, text="Eliminar Tarea", command=eliminar_tarea)
boton_eliminar.pack(pady=5)

boton_completar = tk.Button(root, text="Marcar como Completada", command=marcar_completada)
boton_completar.pack(pady=5)



#Estilo
root.configure(bg="#f0f0f0")
estilo_boton = {"bg": "#4CAF50", "fg": "white", "font": ("Arial", 10)}
estilo_lista = {"bg": "white", "fg": "black", "font": ("Arial", 12)}

entrada_tarea.configure(font=("Arial", 12))
boton_agregar.configure(**estilo_boton)
boton_eliminar.configure(**estilo_boton)
boton_completar.configure(**estilo_boton)
lista_tareas.configure(**estilo_lista)

root.mainloop()