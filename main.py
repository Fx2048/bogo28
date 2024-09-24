import groqcloud as gc  # Asumiendo que la librería se llama groqcloud
import streamlit as st

st.title("The BoGo28")

# Asumimos que la API key de GroqCloud se almacena en las configuraciones de Streamlit
client = gc.Client(api_key=st.secrets["GROQCLOUD_API_KEY"])  # Cambiar a la clave de GroqCloud

if "groqcloud_model" not in st.session_state:
    st.session_state["groqcloud_model"] = "gpt-3.5-turbo"  # O el modelo equivalente en GroqCloud

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

    # Respuesta del asistente a través de GroqCloud API
    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["groqcloud_model"],  # Usar el modelo de GroqCloud
            messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
            stream=True,
        )
        response = st.write_stream(stream)

    # Agregar respuesta del asistente al historial de mensajes
    st.session_state.messages.append({"role": "assistant", "content": response})
