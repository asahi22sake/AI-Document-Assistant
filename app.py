import streamlit as st

from loader import extract_pdf_text
from splitter import split_text
from embeddings import create_embeddings
from vector_store import create_vector_store, search_vector_store
from chatbot import ask_ai

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Document Assistant",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Document Assistant")
st.write("Upload PDF documents and chat with them using AI.")

# -----------------------------
# Session State
# -----------------------------
if "vector_db" not in st.session_state:
    st.session_state.vector_db = None

if "processed" not in st.session_state:
    st.session_state.processed = False

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.header("Upload Documents")

    uploaded_files = st.file_uploader(
        "Choose PDF files",
        type=["pdf"],
        accept_multiple_files=True
    )

    if uploaded_files:
        st.success(f"{len(uploaded_files)} PDF(s) uploaded successfully!")

        if st.button("📖 Process Documents"):

            with st.spinner("Reading PDFs..."):

                # Extract Text
                pdf_text = extract_pdf_text(uploaded_files)

                # Split into Chunks
                chunks = split_text(pdf_text)

                # Generate Embeddings
                embeddings = create_embeddings(chunks)

                # Create Vector Store
                st.session_state.vector_db = create_vector_store(
                    chunks,
                    embeddings
                )

                st.session_state.processed = True

            st.success("✅ Documents processed successfully!")

# -----------------------------
# Main Page
# -----------------------------
if st.session_state.processed:

    st.header("💬 Ask Questions")

    question = st.text_input(
        "Ask something about your uploaded documents:"
    )

    if st.button("Ask AI"):

        if question.strip() == "":
            st.warning("Please enter a question.")

        else:

            with st.spinner("Thinking..."):

                # Retrieve relevant chunks
                results = search_vector_store(
                    st.session_state.vector_db,
                    question
                )

                context = "\n\n".join(results)

                # Ask Groq
                answer = ask_ai(
                    question,
                    context
                )

            st.subheader("🤖 Answer")

            st.write(answer)

            with st.expander("📚 Context Used"):

                for i, chunk in enumerate(results):

                    st.markdown(f"### Chunk {i+1}")
                    st.write(chunk)

else:

    st.info("Upload PDF(s) and click **Process Documents** to begin.")