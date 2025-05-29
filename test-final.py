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
st.markdown("<p style='text-align: center; color: white;'>Responde las siguientes preguntas. ¡Vamos a ver cuánto me conoces chulit@!</p>", unsafe_allow_html=True)

# ---------- PREGUNTAS Y RESPUESTAS ----------
preguntas = [
    {
        "pregunta": "¿Qué significa mi nombre?",
        "opciones": ["La guardiana de la galaxia", "Compañera fiel", "Estrella del alba"],
        "respuesta_correcta": "Compañera fiel"
    },
    {
        "pregunta": "¿Con qué libro he llorado más?",
        "opciones": ["El retrato de Dorian Gray", "Lolita", "Un mundo feliz de Aldous Huxley"],
        "respuesta_correcta": "El retrato de Dorian Gray"
    },
    {
        "pregunta": "¿Cómo se llama mi perro?",
        "opciones": ["Max", "Maximilian", "Máximo Décimo Meridio", "Todas son correctas"],
        "respuesta_correcta": "Todas son correctas"
    },
    {
        "pregunta": "¿Cuál es mi color favorito?",
        "opciones": ["El rosita", "El plateado", "El negro"],
        "respuesta_correcta": "El plateado"
    },
    {
        "pregunta": "¿Qué objeto no falta nunca en mi bolso?",
        "opciones": ["Las llaves", "Un libro", "Pañuelos"],
        "respuesta_correcta": "Un libro"
    },
    {
        "pregunta": "¿Tú qué opinas?",
        "opciones": ["Prefiero no opinar", "Llámame y te cuento", "Yo copazas"],
        "respuesta_correcta": "Yo copazas"
    },
    {
        "pregunta": "¿Cómo me llama mi hermana pequeña?",
        "opciones": ["Tata", "Sis", "Rata"],
        "respuesta_correcta": "Rata"
    },
    {
        "pregunta": "¿Cuál es mi mayor fobia?",
        "opciones": ["Aracnofobia", "Tripofobia", "Fobia social"],
        "respuesta_correcta": "Tripofobia"
    },
    {
        "pregunta": "¿Qué es lo primero que haría si ganase la lotería?",
        "opciones": ["Un viaje todo incluido con mis amigas", "Comprarme un GTI", "Ponerme un piso en la playa"],
        "respuesta_correcta": "Un viaje todo incluido con mis amigas"
    },
    {
        "pregunta": "¿Te puedo cantar una canción?",
        "opciones": ["Teeeeee quiero mucho...", "Vale", "No me gusta cantar"],
        "respuesta_correcta": "Teeeeee quiero mucho..."
    },
    {
        "pregunta": "¿Qué bebo cuando salgo?",
        "opciones": ["Ron con sprite", "y pone opciones... lo que te pongan!", "Ginebra con limón"],
        "respuesta_correcta": "y pone opciones... lo que te pongan!"
    },
    {
        "pregunta": "¿Quienes son los guardianes de la galaxia?",
        "opciones": ["Personajes que te encantan de Marvel", "Tu serie favorita", "La policía nacional"],
        "respuesta_correcta": "La policía nacional"
    },
    {
        "pregunta": "¿Cuál fue el viaje de mi vida?",
        "opciones": ["Georgia", "Campo Solare", "Letonia"],
        "respuesta_correcta": "Campo Solare"
    },
    {
        "pregunta": "¿Qué es lo que más me gusta en un chico?",
        "opciones": ["Las manos cuidadas", "La nariz grande", "Los ojos claros"],
        "respuesta_correcta": "La nariz grande"
    },
        {
        "pregunta": "¿Cuál es mi plan de cita perfecto",
        "opciones": ["Que me lleven a comer y beber hasta explotar", "Ir al cine de la mano", "Netflix y relax en casita"],
        "respuesta_correcta": "Que me lleven a comer y beber hasta explotar"
    },
    {
        "pregunta": "¿Qué me gustaría que dijeran de mí cuando no estoy?",
        "opciones": ["Que soy buena persona", "Que soy extremadamente guapa", "Que soy súper humilde"],
        "respuesta_correcta": "Que soy buena persona"
    },
    {
        "pregunta": "¿Cuál es mi sabor de helado favorito?",
        "opciones": ["Vainilla", "Nube", "Menta y chocolate"],
        "respuesta_correcta": "Menta y chocolate"
    },
    {
        "pregunta": "¿Cuál es mi muletilla?",
        "opciones": ["Vale?", "Me entiendes?", "Que no?"],
        "respuesta_correcta": "Que no?"
    },
    {
        "pregunta": "¿Mis género de pelis/serie favoritas?",
        "opciones": ["Comedia", "Terror elevado", "Románticas"],
        "respuesta_correcta": "Terror elevado"
    },
    {
        "pregunta": "¿Si tuviese que asegurarme de alguna respuesta de mi propio test, ¿a quién preguntaría?",
        "opciones": ["A Julia, Lori y Martillo", "A mi madre", "A la policía nacional"],
        "respuesta_correcta": "A Julia, Lori y Martillo"
    }
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

        # Botón para reiniciar
        if st.button("🔁 Volver a intentarlo"):
            st.experimental_rerun()




