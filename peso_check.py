import os
import pygame
from PIL import Image
import numpy as np

def mostrar_imagen_ascii(ruta_imagen, ancho=50):
    """Convierte la imagen en ASCII para mostrarla en la terminal."""
    img = Image.open(ruta_imagen)
    img = img.convert("L")  # Convertir a escala de grises
    img = img.resize((ancho, int(ancho * img.height / img.width)))

    caracteres = "@%#*+=-:. "
    pixels = np.array(img)
    ascii_img = "\n".join("".join(caracteres[pixel // 32] for pixel in row) for row in pixels)
    
    print(ascii_img)

# Pedir el peso al usuario
peso = float(input("Ingresa tu peso en kg: "))

if peso > 80:
    imagen_path = "no_gordas.jpg"
    audio_path = "oye_gelda_escuchate_esto.mp3"

    # Mostrar la imagen en la terminal (ASCII)
    if os.path.exists(imagen_path):
        mostrar_imagen_ascii(imagen_path)
    else:
        print("⚠️ Imagen no encontrada.")

    # Reproducir la canción
    if os.path.exists(audio_path):
        pygame.mixer.init()
        pygame.mixer.music.load(audio_path)
        pygame.mixer.music.play()
        input("Presiona Enter para detener la música...")
        pygame.mixer.music.stop()
    else:
        print("⚠️ Canción no encontrada.")
else:
    print("✅ Todo bien, no necesitas ver la imagen ni escuchar la canción.")
