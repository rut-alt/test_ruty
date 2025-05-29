import streamlit as st
import base64

# ---------- CONFIGURACIÓN INICIAL ----------
st.set_page_config(page_title="¿Cuánto me conoces?", layout="centered")

# ---------- FONDO CON BASE64 + ESTILOS ----------
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
            .question-box, .result-box {{
                background-color: rgba(0, 0, 0, 0.5);
                padding: 20px;
                border-radius: 15px;
                margin-bottom: 20px;
                color: white;
            }}
            .stRadio > label {{
                color: white !important;
            }}
            .correct-answer {{
                color: lightgreen;
                font-weight: bold;
            }}
            .wrong-answer {{
                color: #ff9999;
                font-weight: bold;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

# Fondo
set_background("fondo-brillante-elegante-con-estilo-borroso.jpg")

# ---------- CONTENIDO ----------
st.markdown("<h1 style='text-align: center; color: white;'>¿Cuánto me conoces?</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: white;'>Responde las siguientes preguntas. ¡Vamos a ver cuánto me conoces chulit@!</p>", unsafe_allow_html=True)

# ---------- PREGUNTAS ----------
preguntas = [
    {"pregunta": "¿Qué crees que nos hará discutir más?", "opciones": ["Competir entre nosotros", "Mis celos", "Tus celos"], "respuesta_correcta": "Mis celos"},
    {"pregunta": "¿Sabes qué es lo que más me gusta de ti?", "opciones": ["Cómo me río contigo", "Que puedas elegir coches para recogerme", "Que vivas cerca de la playa"], "respuesta_correcta": "Cómo me río contigo"},
    {"pregunta": "¿Qué me pone tontorrona?", "opciones": ["Tu voz", "Cuando parlas Catalá", "Tu respuesta a mi gesto de leona", "Todas son correctas"], "respuesta_correcta": "Todas son correctas"},
    {"pregunta": "¿Qué es lo que más me ha faltado estos días?", "opciones": ["Dormir juntos", "Que me beses", "La playa", "1 y 2 son correctas"], "respuesta_correcta": "1 y 2 son correctas"},
    {"pregunta": "¿Qué me da más miedo de esto?", "opciones": ["Que trabajemos juntos", "La distancia", "Que entre una comercial guapa en Zona Luis"], "respuesta_correcta": "La distancia"}
]

# ---------- FORMULARIO ----------
respuestas_usuario = [None] * len(preguntas)
with st.form("quiz_form"):
    for idx, item in enumerate(preguntas):
        with st.container():
            st.markdown(f"<div class='question-box'><b>{idx+1}. {item['pregunta']}</b></div>", unsafe_allow_html=True)
            respuesta = st.radio("", item["opciones"], key=idx, index=None)
            respuestas_usuario[idx] = respuesta

    submitted = st.form_submit_button("Enviar respuestas")

# ---------- RESULTADO ----------
if submitted:
    preguntas_sin_responder = [i for i, r in enumerate(respuestas_usuario) if r is None]

    if preguntas_sin_responder:
        st.warning("¡Ups! Asegúrate de responder todas las preguntas antes de enviar.")
    else:
        puntaje = sum(
            1 for idx, item in enumerate(preguntas)
            if respuestas_usuario[idx] == item['respuesta_correcta']
        )
        puntaje_final = round((puntaje / len(preguntas)) * 10, 1)

        if puntaje_final < 6:
            mensaje = "😢 No me conoces nada..."
        elif 6 <= puntaje_final < 9:
            mensaje = "🫣 Pff, muy justillo... ¿nos tomamos una cerve y te cuento cositas?"
        else:
            mensaje = "🥹 Te quiero mucho, ¡menuda notaza!"

        st.success(f"¡Terminaste! Tu nota es: **{puntaje_final} / 10**")
        st.markdown(f"<h3 style='color: white; text-align: center;'>{mensaje}</h3>", unsafe_allow_html=True)

        st.markdown("<h4 style='color: white;'>📋 Detalle de tus respuestas:</h4>", unsafe_allow_html=True)
        for idx, item in enumerate(preguntas):
            user_resp = respuestas_usuario[idx]
            correcta = item["respuesta_correcta"]
            if user_resp == correcta:
                st.markdown(f"<div class='result-box correct-answer'>✅ {idx+1}. {item['pregunta']}<br><b>Tu respuesta:</b> {user_resp}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='result-box wrong-answer'>❌ {idx+1}. {item['pregunta']}<br><b>Tu respuesta:</b> {user_resp}<br><b>Correcta:</b> {correcta}</div>", unsafe_allow_html=True)

        # Botón para reiniciar
        if st.button("🔁 Volver a intentarlo"):
            st.experimental_rerun()
