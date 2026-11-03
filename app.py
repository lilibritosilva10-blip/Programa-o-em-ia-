import os
import streamlit as st
from groq import Groq

# Configuração da página
st.set_page_config(page_title="Meu Agente de IA", page_icon="🤖")
st.title("🤖 Meu Agente de IA")

# Inicialização do cliente Groq
# Certifique-se de configurar a GROQ_API_KEY no seu ambiente local ou Streamlit Secrets
api_key = os.environ.get("GROQ_API_KEY")

if not api_key:
    st.error("Chave de API da Groq não encontrada. Configure a variável GROQ_API_KEY.")
    st.stop()

client = Groq(api_key=api_key)

# Prompt do Agente (COSTAR)
SYSTEM_PROMPT = """
Context: Você é um assistente especializado em ajudar usuários com dúvidas sobre estudos.
Objective: Responder dúvidas de forma simples, didática e direta.
Style: Educativo e estruturado.
Tone: Amigável e motivador.
Audience: Estudantes.
Response: Use bullet points quando apropriado e seja objetivo.
"""

# Histórico de mensagens no Streamlit
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe histórico de chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Entrada do usuário
if user_input := st.chat_input("Como posso ajudar você hoje?"):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Chamada para a API da Groq
    with st.chat_message("assistant"):
        try:
            messages_payload = [{"role": "system", "content": SYSTEM_PROMPT}] + [
                {"role": m["role"], "content": m["content"]} for m in st.session_state.messages
            ]
            
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=messages_payload,
                temperature=0.7,
            )
            
            bot_reply = response.choices[0].message.content
            st.markdown(bot_reply)
            st.session_state.messages.append({"role": "assistant", "content": bot_reply})
            
        except Exception as e:
            st.error(f"Erro ao comunicar com a API da Groq: {e}")