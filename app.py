import streamlit as st

from src.rag_pipeline import ask

st.set_page_config(
    page_title="IITB Insti-Assist",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 IITB Insti-Assist")

query = st.text_input(
    "Ask a question about IIT Bombay"
)

if st.button("Ask"):

    if query.strip():

        with st.spinner("Searching..."):

            answer, sources = ask(query)

        st.subheader("Answer")

        st.write(answer)

        st.subheader("Sources")

        if len(sources) == 0:
            st.info("No relevant document found.")

        else:
            for s in sources:

                with st.expander(
                    f"{s['source']} | Page {s['page']} | Score {s['score']:.3f}"
                ):
                    st.write(s["text"])