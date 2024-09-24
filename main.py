import os
from groq import Groq
import streamlit as st

client = Groq(
    # This is the default and can be omitted
    api_key=os.environ.get("GROQ_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of low latency LLMs",
        }
    ],
    model="mixtral-8x7b-32768",
)
print(chat_completion.choices_0.message.content)
        response = st.write_stream(stream)

    # Agregar respuesta del asistente al historial de mensajes
    st.session_state.messages.append({"role": "assistant", "content": response})
