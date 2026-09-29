import streamlit as st
import ollama

# =========================
# PAGE SETTINGS
# =========================

st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered"
)


# =========================
# CSS
# =========================

st.markdown("""
<style>

/* Main background */
.stApp {
    background:
        radial-gradient(
            circle at 10% 20%,
            rgba(99, 102, 241, 0.35),
            transparent 35%
        ),
        radial-gradient(
            circle at 90% 80%,
            rgba(139, 92, 246, 0.30),
            transparent 35%
        ),
        linear-gradient(
            135deg,
            #dbeafe 0%,
            #ede9fe 45%,
            #e0e7ff 100%
        );

    min-height: 100vh;
}

/* Main container */
.block-container {
    max-width: 850px;
    padding-top: 45px;
    padding-bottom: 100px;
}

/* Title */
h1 {
    text-align: center;
    font-size: 40px !important;
    font-weight: 800 !important;

    background: linear-gradient(
        90deg,
        #4f46e5,
        #7c3aed,
        #2563eb
    );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    margin-bottom: 35px;
}

/* Chat messages */
[data-testid="stChatMessage"] {
    border-radius: 18px;
    padding: 14px 18px;
    margin-bottom: 14px;

    border: 1px solid rgba(99, 102, 241, 0.15);

    box-shadow:
        0 5px 15px rgba(79, 70, 229, 0.08);
}

/* User message */
[data-testid="stChatMessage"]:has(
    [data-testid="stChatMessageAvatarUser"]
) {
    background: linear-gradient(
        135deg,
        #e0e7ff,
        #ede9fe
    );

    border-left: 4px solid #6366f1;
}

/* AI message */
[data-testid="stChatMessage"]:has(
    [data-testid="stChatMessageAvatarAssistant"]
) {
    background: linear-gradient(
        135deg,
        #ffffff,
        #f8faff
    );

    border-left: 4px solid #8b5cf6;
}

/* Chat text */
[data-testid="stChatMessage"] p {
    color: #1e293b;
    font-size: 16px;
    line-height: 1.6;
}

/* Chat input */
[data-testid="stChatInput"] {
    border-radius: 18px;
}

/* Input box */
[data-testid="stChatInput"] textarea {
    background: white !important;
    color: #1e293b !important;

    border: 2px solid #c7d2fe !important;
    border-radius: 16px !important;

    font-size: 16px !important;
    padding: 13px !important;

    box-shadow:
        0 5px 20px rgba(79, 70, 229, 0.10);
}

/* Input focus */
[data-testid="stChatInput"] textarea:focus {
    border-color: #6366f1 !important;

    box-shadow:
        0 0 0 3px rgba(99, 102, 241, 0.15),
        0 5px 20px rgba(79, 70, 229, 0.12) !important;
}

/* Send button */
[data-testid="stChatInput"] button {
    background: linear-gradient(
        135deg,
        #6366f1,
        #7c3aed
    ) !important;

    color: white !important;

    border-radius: 12px !important;
    border: none !important;

    transition: 0.2s ease;
}

/* Send button hover */
[data-testid="stChatInput"] button:hover {
    background: linear-gradient(
        135deg,
        #4f46e5,
        #6d28d9
    ) !important;

    transform: scale(1.05);
}

/* Mobile */
@media (max-width: 600px) {

    .block-container {
        padding: 25px 15px 80px 15px;
    }

    h1 {
        font-size: 30px !important;
    }

    [data-testid="stChatMessage"] {
        border-radius: 15px;
        padding: 12px 14px;
    }
}

</style>
""", unsafe_allow_html=True)


# =========================
# TITLE
# =========================

st.title("🤖 AI Chatbot")


# =========================
# CHAT HISTORY
# =========================

if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])


# =========================
# USER INPUT
# =========================

user_input = st.chat_input(
    "Type your message here..."
)


# =========================
# AI RESPONSE
# =========================

if user_input:

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.write(user_input)

    response = ollama.chat(
        "llama3.2",
        messages=st.session_state.messages
    )

    bot_response = response["message"]["content"]

    st.session_state.messages.append({
        "role": "assistant",
        "content": bot_response
    })

    with st.chat_message("assistant"):
        st.write(bot_response)