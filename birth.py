import streamlit as st
import flask as fl

# Page config
st.set_page_config(page_title="🎁 Gift for Namyaa", page_icon="🎉", layout="centered")

# Custom CSS for beautiful design
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #ff9a9e 0%, #fad0c4 100%);
        color: #333;
        font-family: 'Trebuchet MS', sans-serif;
    }
    .title {
        font-size: 50px;
        text-align: center;
        font-weight: bold;
        color: #ff1493;
        text-shadow: 2px 2px #ff6f61;
        margin-top: 50px;
    }
    .button {
        display: flex;
        justify-content: center;
        margin-top: 40px;
    }
    .gift-text {
        font-size: 22px;
        text-align: center;
        color: #36454f;
        padding: 20px;
        background: rgba(0,0,0,0.3);
        border-radius: 20px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.3);
    }
    .teddy-text {
        font-size: 28px;
        text-align: center;
        color: #ffc0cb;
        font-weight: bold;
        margin-top: 20px;
        text-shadow: 2px 2px #ff6f61;
    }
    </style>
""", unsafe_allow_html=True)

# Track pages
if "page" not in st.session_state:
    st.session_state.page = 1

# PAGE 1 - Gift for You
if st.session_state.page == 1:
    st.markdown("<div class='title'>🎁 Gift for You 🎁</div>", unsafe_allow_html=True)
    st.markdown("<div class='gift-text'>Click below to open your special birthday surprise 💖</div>", unsafe_allow_html=True)
    if st.button("Open Gift 🎉"):
        st.session_state.page = 2
        st.experimental_rerun()

# PAGE 2 - Birthday Message
elif st.session_state.page == 2:
    st.markdown("<div class='title'>🎂 Happy Birthday Namyaa 🎂</div>", unsafe_allow_html=True)
    st.markdown("""
        <div class='gift-text'>
        Dearest Namyaa,<br><br>
        On this special day, I just want to remind you how truly special you are to me. 
        You bring happiness, warmth, and light into my life with every smile and every word. 
        May this birthday bring you endless joy, laughter, and unforgettable memories. 
        Thank you for being such a beautiful part of my world. Today and always, you deserve all the happiness in the universe. 
        💖🎉🌸<br><br>
        With all my heart,<br>
        – Amrit
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='button'>", unsafe_allow_html=True)
    if st.button("A Gift for Namaya 🎁"):
        st.session_state.page = 3
        st.experimental_rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# PAGE 3 - Final Gift (Teddy Bear)
elif st.session_state.page == 3:
    st.markdown("<div class='title'>🧸 A Gift for You 🧸</div>", unsafe_allow_html=True)
    st.image(
        "teddybear.png",
        caption="A cute teddy bear just for you 💕",
        use_container_width=True
    )
    st.markdown("<div class='teddy-text'>This gift is from Amrit 💝</div>", unsafe_allow_html=True)