import tkinter as tk
from PIL import Image, ImageTk
import pygame
import threading

# Función para calcular el IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Función para reproducir el audio usando pygame
def reproducir_audio():
    pygame.mixer.init()
    pygame.mixer.music.load("oye_gelda_escuchate_esto.mp3")
    pygame.mixer.music.play()

# Muestra el resultado del IMC y ejecuta acciones si es mayor a 27
def mostrar_resultado(imc):
    resultado_text = f"Tu IMC es: {imc:.2f}"
    resultado_label.config(text=resultado_text)

    if imc > 27:
        # Carga y muestra la imagen
        imagen = Image.open("no_gordas.jpg")
        imagen = imagen.resize((300, 300))
        imagen_tk = ImageTk.PhotoImage(imagen)
        imagen_label.config(image=imagen_tk)
        imagen_label.image = imagen_tk

        # Reproducir audio en hilo separado para no congelar la GUI
        threading.Thread(target=reproducir_audio).start()
    else:
        imagen_label.config(image='', text="IMC en rango saludable ✅")

# Obtiene datos del usuario y calcula el IMC
def calcular():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        imc = calcular_imc(peso, altura)
        mostrar_resultado(imc)
    except ValueError:
        resultado_label.config(text="❌ Ingresa valores válidos.")

# Interfaz gráfica (Tkinter)
root = tk.Tk()
root.title("Calculadora de IMC con flow 😎")

tk.Label(root, text="Peso (kg):").pack()
entry_peso = tk.Entry(root)
entry_peso.pack()

tk.Label(root, text="Altura (m):").pack()
entry_altura = tk.Entry(root)
entry_altura.pack()

tk.Button(root, text="Calcular IMC", command=calcular).pack(pady=10)

resultado_label = tk.Label(root, text="", font=("Arial", 14))
resultado_label.pack()

imagen_label = tk.Label(root)
imagen_label.pack()

root.mainloop()
