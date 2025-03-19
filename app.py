import streamlit as st
import random
from PIL import Image
import os

# Configuración de la página
st.set_page_config(page_title="Generador de Imágenes", layout="centered")
st.title("Generador de Imágenes Aleatorias")
st.write("Haz clic en el botón para obtener una imagen aleatoria.")

# Ruta donde se encuentran las imágenes
image_folder = 'images'

# Verificar si la carpeta existe
if not os.path.exists(image_folder):
    st.error("La carpeta de imágenes no existe. Asegúrate de tener una carpeta llamada 'images' con imágenes dentro.")
else:
    # Obtener la lista de imágenes
    image_files = list(set([f for f in os.listdir(image_folder) if f.endswith(('.png', '.jpg', '.jpeg', '.gif'))]))
    random.shuffle(image_files)

    funny_phrases = [
    "La cara de los polacos cuando España gana el premio a mejor árbol de Europa.",
    "La cara de Lalacus cuando la hacen ir a Bruselas al premio del árbol.",
    "Cuando descubres que el mejor árbol de Europa está en España y no en Polonia.",
    "Esa sensación cuando pensabas que ganarías el premio y luego... España lo gana.",
    "El community manager de Polonia intentando explicar por qué no ganaron.",
    "La cara de Grison cuando le para la guardia civil.",
    "David Broncano preguntando en La Resistencia: ‘¿Cuántos árboles tienes en casa?’", 
    "Ese momento en el que te das cuenta de que el árbol de tu pueblo nunca será famoso.",
    "Cuando el premio al mejor árbol de Europa importa más que las elecciones generales.",
    "Cuando descubres que hay más gente votando por concurso del árbol que en las elecciones generales.",
    "El comité europeo sin entender por qué España y Polonia están en guerra por un árbol."
    ]

if 'used_images' not in st.session_state:
    st.session_state.used_images = []

if st.button("Generar Imagen"):
        if image_files:
            remaining_images = list(set(image_files) - set(st.session_state.used_images))
            
            if not remaining_images:
                st.session_state.used_images = []
                remaining_images = image_files
                random.shuffle(remaining_images)
            
            selected_image = remaining_images.pop()
            st.session_state.used_images.append(selected_image)
            funny_text = random.choice(funny_phrases)
            st.subheader(funny_text)
            selected_image = random.choice(image_files)
            image_path = os.path.join(image_folder, selected_image)
            image = Image.open(image_path)
            
            # Redimensionar la imagen a un tamaño más pequeño
            image = image.resize((400, 400), Image.LANCZOS)
            
            st.image(image, use_container_width=True)
        else:
            st.warning("No hay imágenes disponibles en la carpeta.")
