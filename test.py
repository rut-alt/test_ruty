import streamlit as st
import base64

# ---------- CONFIGURACIÓN INICIAL ----------
st.set_page_config(page_title="¿Cuánto me conoces?", layout="centered")

# ---------- FONDO CON BASE64 ----------
def set_background(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("data:image/jpg;base64,{encoded_string}");
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                background-attachment: fixed;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

# Nombre de tu imagen (asegúrate que esté en la misma carpeta que este script)
set_background("fondo-brillante-elegante-con-estilo-borroso.jpg")

# ---------- CONTENIDO ----------
st.markdown("<h1 style='text-align: center;'>¿Cuánto me conoces?</h1>", unsafe_allow_html=True)
st.write("Responde las siguientes preguntas. ¡Veamos qué tanto sabes sobre mí!")

# ---------- PREGUNTAS Y RESPUESTAS ----------
preguntas = [
    {
        "pregunta": "¿Con qué libro he llorado más?",
        "opciones": [
            "El retrato de Dorian Gray",
            "Lolita",
            "Un mundo feliz de Aldous Huxley"
        ],
        "respuesta_correcta": "El retrato de Dorian Gray"
    }
]

respuestas_usuario = []
puntaje = 0

# ---------- FORMULARIO DE TEST ----------
with st.form("quiz_form"):
    for idx, item in enumerate(preguntas):
        respuesta = st.radio(f"{idx+1}. {item['pregunta']}", item['opciones'], key=idx)
        respuestas_usuario.append(respuesta)
    submitted = st.form_submit_button("Enviar respuestas")

# ---------- RESULTADO ----------
if submitted:
    for idx, item in enumerate(preguntas):
        if respuestas_usuario[idx] == item['respuesta_correcta']:
            puntaje += 1

    puntaje_final = round((puntaje / len(preguntas)) * 10, 1)
    st.success(f"¡Terminaste! Tu nota es: **{puntaje_final} / 10**")



