import streamlit as st
from groq import Groq

# === Configuration ===
st.set_page_config(page_title="Groq AI Chatbot", page_icon="🤖", layout="centered")

# Replace with your Groq API key
API_KEY = "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"  # ← Put your key here
client = Groq(api_key=API_KEY)

# List of available Groq models
GROQ_MODELS = {
    "Llama 3.3 70B (Versatile)": "llama-3.3-70b-versatile",
    "Llama 3.1 70B (Versatile)": "llama3-70b-8192",
    "Llama 3.1 8B (Instant)": "llama3-8b-8192",
    "Llama 3.2 90B (Vision + Text)": "llama-3.2-90b-vision-preview",
    "Llama 3.2 11B (Vision + Text)": "llama-3.2-11b-vision-preview",
    "Mixtral 8x7B (Instruct)": "mixtral-8x7b-32768",
    "Gemma 2 9B (It)": "gemma2-9b-it",
    "Gemma 2 27B (It)": "gemma-2-27b-it",
}

# === Sidebar: Model Selection ===
st.sidebar.title("⚙️ Settings")
selected_model_name = st.sidebar.selectbox(
    "Choose a model",
    options=list(GROQ_MODELS.keys()),
    index=0  # Default to the first one
)
model_id = GROQ_MODELS[selected_model_name]

st.sidebar.caption(f"Current model: `{model_id}`")

temperature = st.sidebar.slider("Temperature (creativity)", 0.0, 1.0, 0.7, 0.05)
max_tokens = st.sidebar.slider("Max tokens", 50, 512, 256, 50)

# Clear chat button
if st.sidebar.button("🗑️ Clear Chat History"):
    st.session_state.messages = [SYSTEM_PROMPT]
    st.rerun()

# === System Prompt ===
SYSTEM_PROMPT_CONTENT = st.sidebar.text_area(
    "System Prompt",
    value="You are a helpful, witty, and friendly AI assistant.",
    height=100
)
SYSTEM_PROMPT = {"role": "system", "content": SYSTEM_PROMPT_CONTENT}

# === Initialize Chat History ===
if "messages" not in st.session_state:
    st.session_state.messages = [SYSTEM_PROMPT]

# === Main App ===
st.title("Groq AI Chatbot")
st.write("Chat with powerful open-source models powered by Groq's ultra-fast inference!")

# Display chat history
for message in st.session_state.messages[1:]:  # Skip system prompt
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if user_input := st.chat_input("Type your message here..."):
    # Append user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                chat_completion = client.chat.completions.create(
                    messages=st.session_state.messages,
                    model=model_id,
                    temperature=temperature,
                    max_tokens=max_tokens,
                )
                response = chat_completion.choices[0].message.content
                st.markdown(response)
            except Exception as e:
                st.error(f"Error: {str(e)}")
                response = "Sorry, something went wrong."

    # Append assistant response

    st.session_state.messages.append({"role": "assistant", "content": response})
