import streamlit as st
from chatbot import AIInternChatbot

# -----------------------------------
# Page Configuration
# -----------------------------------
st.set_page_config(
    page_title="AI Intern Support Assistant",
    page_icon="🤖",
    layout="centered"
)

# -----------------------------------
# Load Chatbot
# -----------------------------------
@st.cache_resource
def load_chatbot():
    return AIInternChatbot()

chatbot = load_chatbot()
# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>
.main {
    padding-top: 1rem;
}

.stChatMessage {
    border-radius: 12px;
    padding: 12px;
}

div[data-testid="stMetric"] {
    background-color: #f5f7fa;
    border-radius: 12px;
    padding: 10px;
    border: 1px solid #dcdcdc;
}

section[data-testid="stSidebar"] {
    background-color: #f8f9fc;
}

footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------------
# Sidebar
# -----------------------------------
with st.sidebar:
    st.title("📚 AI Intern Assistant")

    st.markdown("### 💡 Example Questions")

    st.markdown("""
- How do I submit my task?
- How do I deploy my Streamlit project?
- What should I include in my GitHub repository?
- How do I contact my mentor?
- My Streamlit deployment is not working.
""")

    st.markdown("---")

    st.markdown("### ℹ️ About")

    st.write(
        "AI Intern Support Assistant uses Natural Language Processing(NLP) and Hugging Face Sentence Transformers to provide intelligent semantic search across 60+ internship FAQs and 40+ historical support tickets, enabling interns to recieves fast and accurate support."
    )

    st.markdown("---")

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# -----------------------------------
# Header
# -----------------------------------
st.title("🤖 AI Intern Support Assistant")

st.caption(
    "An AI-powered chatbot developed using Hugging Face Sentence Transformers "
    "and Streamlit to provide intelligent support for internship-related queries."
)

st.divider()

# -----------------------------------
# Project Statistics
# -----------------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("FAQs", "60+")

with col2:
    st.metric("Support Tickets", "40+")

with col3:
    st.metric("AI Model", "MiniLM")

st.divider()

# -----------------------------------
# Suggested Questions
# -----------------------------------
st.markdown("### 💡 Try asking:")

col1, col2 = st.columns(2)

with col1:
    if st.button("📤 Submit my task"):
        st.session_state["suggested_question"] = "How do I submit my task?"

    if st.button("☁️ Deploy project"):
        st.session_state["suggested_question"] = "How do I deploy my Streamlit project?"

with col2:
    if st.button("📂 GitHub Repository"):
        st.session_state["suggested_question"] = "What should I include in my GitHub repository?"

    if st.button("👨‍🏫 Contact Mentor"):
        st.session_state["suggested_question"] = "How do I contact my mentor?"

# -----------------------------------
# Chat History
# -----------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# -----------------------------------
# User Input
# -----------------------------------
user_input = st.session_state.pop("suggested_question", None)

if user_input is None:
    user_input = st.chat_input("Ask your internship-related question...")

# -----------------------------------
# Generate Response
# -----------------------------------
if user_input:

    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.write(user_input)

    answer, confidence = chatbot.get_response(user_input)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

    with st.chat_message("assistant", avatar="🤖"):
        st.write(answer)

        if confidence >= 0.80:
            st.success(f"✅ Confidence Score: {confidence:.2f}")
        elif confidence >= 0.60:
            st.info(f"ℹ️ Confidence Score: {confidence:.2f}")
        else:
            st.warning(f"⚠️ Confidence Score: {confidence:.2f}")

# -----------------------------------
# Footer
# -----------------------------------
st.divider()

st.caption(
    "Built with ❤️  by Ramisa Pirzada |Python . Streamlit . Hugging Face Sentence Transformer. Pandas. and NLP."
)