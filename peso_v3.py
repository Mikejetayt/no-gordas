import tkinter as tk
from tkinter import messagebox
import pygame

def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load(r"C:/Users/Admin/OneDrive/Desktop/python/oye_gelda_escuchate_esto.mp3")  # Cambia a tu ruta
    pygame.mixer.music.play()

def check_weight():
    try:
        weight = float(entry.get())
        if weight > 80:
            img_label.pack()
            play_music()  # Reproducir música
        else:
            messagebox.showinfo("Resultado", "Tu peso es saludable.")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa un número válido.")

# Configuración de la ventana
root = tk.Tk()
root.title("Peso y Música")

# Entrada de peso
entry_label = tk.Label(root, text="Ingresa tu peso (kg):")
entry_label.pack()
entry = tk.Entry(root)
entry.pack()

# Botón para verificar peso
check_button = tk.Button(root, text="Verificar Peso", command=check_weight)
check_button.pack()

# Imagen que se mostrará
img = tk.PhotoImage(file=r"C:/Users/Admin/OneDrive/Desktop/python/no_gordas.png")  # Cambia a tu ruta
img_label = tk.Label(root, image=img)

# Iniciar el bucle principal
root.mainloop()