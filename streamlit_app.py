import streamlit as st

# audio

audio_file = open("audio/sound.wav", "rb")
audio_bytes = audio_file.read()

# default style

style_css = ""

# main app

# --------- Infor ---------

st.subheader("| General code")

st.code(
    """
st.markdown("<style>" + style_css + "</style>", unsafe_allow_html=True)
""",
    language="python",
)

st.write("Below we present potential values of `style_css`")

st.subheader("| Examples")

# --------- background ---------

st.write("Change media player background")

st.code(
    """audio::-webkit-media-controls-panel,
audio::-webkit-media-controls-enclosure {
    background-color: #9c9d9f;
}""",
    language="css",
)


if st.button("Apply", key=1):
    style_css = """
    audio::-webkit-media-controls-panel,
    audio::-webkit-media-controls-enclosure {
        background-color: #9c9d9f;
    }
    """

# --------- background ---------

st.write("Change media player text")

st.code(
    """audio::-webkit-media-controls-time-remaining-display,
audio::-webkit-media-controls-current-time-display {
    color: pink;
}""",
    language="css",
)


if st.button("Apply", key=2):
    style_css = """
audio::-webkit-media-controls-time-remaining-display,
audio::-webkit-media-controls-current-time-display {
    color: red;}
    """

st.markdown("<style>" + style_css + "</style>", unsafe_allow_html=True)


st.audio(audio_bytes, format="audio/wav")
