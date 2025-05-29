import streamlit as st

# ---------- CONFIGURACIÓN INICIAL ----------
st.set_page_config(page_title="¿Cuánto me conoces?", layout="centered")

# ---------- FONDO PERSONALIZADO CON CSS ----------
def set_background_from_file(image_path):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{image_path}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_background_from_file("cerca-brillo-brillante_23-2149140052.jpg")  # Cambia a tu archivo real

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
    },
    # Aquí puedes ir agregando más preguntas...
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

