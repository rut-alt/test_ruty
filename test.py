import streamlit as st

# ---------- CONFIGURACIÓN INICIAL ----------
st.set_page_config(page_title="¿Cuánto me conoces?", layout="centered")

# ---------- FONDO PERSONALIZADO ----------
def set_background(image_path):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url("{image_path}") no-repeat center center fixed;
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Usa el nombre exacto del archivo:
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


