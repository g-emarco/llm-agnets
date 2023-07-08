import streamlit as st

from main import sdr_start


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)


st.set_page_config(
    page_icon="static/robot-1.1s-200px.png",
    layout="wide",
    page_title="Eden-SDR",
    initial_sidebar_state="expanded",
)

st.markdown(
    f'<div class="header"><figure><embed type="image/svg+xml" src="/static/sdr.svg" /><figcaption></figcaption></figure><h3> Eden PaLM2 SDR.</h3></div>',
    unsafe_allow_html=True,
)

st.image("static/sdr.jpeg", width=300)





with st.expander("How to use Eden-SDR 🤖", expanded=True):
    st.markdown(
        """
		This agent:\n
		 1. Google Search {full_name}
		 2. Scrape {full_name}'s Linkedin Information  
		 3. Create gmail cold email draft
		"""
    )


st.markdown("---")

st.sidebar.write("Tech Stack")
st.sidebar.markdown(
    """
- [LangChain 🦜🔗](https://python.langchain.com/en/latest/index.html)
- [GCP Palm2 LLM Model](https://ai.google/discover/palm2)   
- [Pinecone 🌲 Vectorestore](https://www.pinecone.io/)
- [Streamlit](https://streamlit.io/)
"""
)
st.sidebar.write("Made by [Eden Marco](https://www.linkedin.com/in/eden-marco/)")

full_name_target = st.text_input("Full Name of Target")
topic = st.text_area("Give your Agent-SDR a topic")


generate = st.button("Run Agent🤖")

if generate:
    with st.spinner("Agent running..."):
        sdr_start(full_name=full_name_target, topic=topic)
        st.balloons()

local_css("static/frontend.css")
remote_css("https://fonts.googleapis.com/icon?family=Material+Icons")
remote_css(
    "https://fonts.googleapis.com/css2?family=Red+Hat+Display:wght@300;400;500;600;700&display=swap"
)
