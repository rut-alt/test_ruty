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
            .question-box {{
                background-color: rgba(0, 0, 0, 0.7);
                padding: 20px;
                border-radius: 15px;
                margin-bottom: 20px;
                color: white;
            }}
            .stRadio > label {{
                color: white !important;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

# Fondo
set_background("fondo-brillante-elegante-con-estilo-borroso.jpg")

# ---------- CONTENIDO ----------
st.markdown("<h1 style='text-align: center; color: white;'>¿Cuánto me conoces?</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: white;'>Responde las siguientes preguntas. ¡Veamos qué tanto sabes sobre mí!</p>", unsafe_allow_html=True)

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
    },
    {
        "pregunta": "¿Cómo se llama mi perro?",
        "opciones": [
            "Max",
            "Maximilian",
            "Maximo Decimo Meridio",
            "Todas son correctas"
        ],
        "respuesta_correcta": "Todas son correctas"
    }
]

respuestas_usuario = []
puntaje = 0

# ---------- FORMULARIO DE TEST ----------
with st.form("quiz_form"):
    for idx, item in enumerate(preguntas):
        with st.container():
            st.markdown(f"<div class='question-box'><b>{idx+1}. {item['pregunta']}</b></div>", unsafe_allow_html=True)
            respuesta = st.radio("", item['opciones'], key=idx)
            respuestas_usuario.append(respuesta)
    submitted = st.form_submit_button("Enviar respuestas")

# ---------- RESULTADO ----------
if submitted:
    for idx, item in enumerate(preguntas):
        if respuestas_usuario[idx] == item['respuesta_correcta']:
            puntaje += 1

    puntaje_final = round((puntaje / len(preguntas)) * 10, 1)
    st.success(f"¡Terminaste! Tu nota es: **{puntaje_final} / 10**")



