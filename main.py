import os
from groq import Groq
import streamlit as st

# Configurar el cliente de GroqCloud con la API Key
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Agregar la imagen al inicio
st.image("https://github.com/Fx2048/bogo28/blob/main/Imagenes/bogologo.jpg", caption="bogo28 - Tu Asistente Virtual", use_column_width=True)  # Asegúrate de que la imagen esté en la misma carpeta

st.title("bogo28 - Chatbot")

if "groqcloud_model" not in st.session_state:
    st.session_state["groqcloud_model"] = "mixtral-8x7b-32768"  # Modelo por defecto de GroqCloud

if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar los mensajes anteriores
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Capturar nuevo input del usuario
if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Realizar la llamada a la API de GroqCloud
    with st.chat_message("assistant"):
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model=st.session_state["groqcloud_model"],  # Usar el modelo definido en GroqCloud
        )
        
        # Obtener la respuesta del asistente
        response = chat_completion.choices[0].message.content
        st.markdown(response)

    # Agregar respuesta del asistente al historial de mensajes
    st.session_state.messages.append({"role": "assistant", "content": response})

