import streamlit as st

# audio

audio_file = open("audio/sound.wav", "rb")
audio_bytes = audio_file.read()

# default style

if "style_css" not in st.session_state:
    st.session_state["style_css"] = ""

# main app

# --------- Info ---------

st.subheader("| General code")

st.code(
    """
st.markdown("<style>" + style_css + "</style>", unsafe_allow_html=True)
""",
    language="python",
)

st.write("Below we present potential values of `style_css`")

# --------- Examples ---------

st.subheader("| Examples")

st.markdown(
    "<style>" + st.session_state["style_css"] + "</style>", unsafe_allow_html=True
)

st.audio(audio_bytes, format="audio/wav")


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
    st.session_state[
        "style_css"
    ] = """
    audio::-webkit-media-controls-panel,
    audio::-webkit-media-controls-enclosure {
        background-color: #9c9d9f;
    }
    """
    st.experimental_rerun()

# --------- text ---------

st.write("Change media player text to red")

st.code(
    """audio::-webkit-media-controls-time-remaining-display,
audio::-webkit-media-controls-current-time-display {
    color: pink;
}""",
    language="css",
)


if st.button("Apply", key=2):
    st.session_state[
        "style_css"
    ] = """
audio::-webkit-media-controls-time-remaining-display,
audio::-webkit-media-controls-current-time-display {
    color: red;}
    """
    st.experimental_rerun()

# --------- height ---------

st.write("Change media player width and height")

st.code(
    """audio::-webkit-media-controls-time-remaining-display,
audio::-webkit-media-controls-current-time-display {
    max-width: 50%;
    max-height: 20px;
}""",
    language="css",
)

if st.button("Apply", key=3):
    st.session_state[
        "style_css"
    ] = """
audio::-webkit-media-controls-panel,
audio::-webkit-media-controls-enclosure {
    max-width: 300px;
    max-height: 20px;}
    """
    st.experimental_rerun()


# --------- remove  ---------

st.write("Change background text, color, play button image and slider background")

st.code(
    """audio::-webkit-media-controls-panel,
audio::-webkit-media-controls-enclosure {
    background-color:#301934;}

audio::-webkit-media-controls-time-remaining-display,
audio::-webkit-media-controls-current-time-display {
    color: white;
    text-shadow: none; 

}
audio::-webkit-media-controls-play-button{
  background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAApgAAAKYB3X3/OAAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAANCSURBVEiJtZZPbBtFFMZ/M7ubXdtdb1xSFyeilBapySVU8h8OoFaooFSqiihIVIpQBKci6KEg9Q6H9kovIHoCIVQJJCKE1ENFjnAgcaSGC6rEnxBwA04Tx43t2FnvDAfjkNibxgHxnWb2e/u992bee7tCa00YFsffekFY+nUzFtjW0LrvjRXrCDIAaPLlW0nHL0SsZtVoaF98mLrx3pdhOqLtYPHChahZcYYO7KvPFxvRl5XPp1sN3adWiD1ZAqD6XYK1b/dvE5IWryTt2udLFedwc1+9kLp+vbbpoDh+6TklxBeAi9TL0taeWpdmZzQDry0AcO+jQ12RyohqqoYoo8RDwJrU+qXkjWtfi8Xxt58BdQuwQs9qC/afLwCw8tnQbqYAPsgxE1S6F3EAIXux2oQFKm0ihMsOF71dHYx+f3NND68ghCu1YIoePPQN1pGRABkJ6Bus96CutRZMydTl+TvuiRW1m3n0eDl0vRPcEysqdXn+jsQPsrHMquGeXEaY4Yk4wxWcY5V/9scqOMOVUFthatyTy8QyqwZ+kDURKoMWxNKr2EeqVKcTNOajqKoBgOE28U4tdQl5p5bwCw7BWquaZSzAPlwjlithJtp3pTImSqQRrb2Z8PHGigD4RZuNX6JYj6wj7O4TFLbCO/Mn/m8R+h6rYSUb3ekokRY6f/YukArN979jcW+V/S8g0eT/N3VN3kTqWbQ428m9/8k0P/1aIhF36PccEl6EhOcAUCrXKZXXWS3XKd2vc/TRBG9O5ELC17MmWubD2nKhUKZa26Ba2+D3P+4/MNCFwg59oWVeYhkzgN/JDR8deKBoD7Y+ljEjGZ0sosXVTvbc6RHirr2reNy1OXd6pJsQ+gqjk8VWFYmHrwBzW/n+uMPFiRwHB2I7ih8ciHFxIkd/3Omk5tCDV1t+2nNu5sxxpDFNx+huNhVT3/zMDz8usXC3ddaHBj1GHj/As08fwTS7Kt1HBTmyN29vdwAw+/wbwLVOJ3uAD1wi/dUH7Qei66PfyuRj4Ik9is+hglfbkbfR3cnZm7chlUWLdwmprtCohX4HUtlOcQjLYCu+fzGJH2QRKvP3UNz8bWk1qMxjGTOMThZ3kvgLI5AzFfo379UAAAAASUVORK5CYII=");
}

audio::-webkit-media-controls-timeline {
  background-color: #532b5a;
  border-radius: 25px;
  margin-left: 10px;
  margin-right: 10px;
  accent-color: white;
}""",
    language="css",
)

if st.button("Apply", key=4):
    st.session_state[
        "style_css"
    ] = """

audio::-webkit-media-controls-panel,
audio::-webkit-media-controls-enclosure {
    background-color:#301934;}

audio::-webkit-media-controls-time-remaining-display,
audio::-webkit-media-controls-current-time-display {
    color: white;
    text-shadow: none; 

}
audio::-webkit-media-controls-play-button{
  background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAApgAAAKYB3X3/OAAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAANCSURBVEiJtZZPbBtFFMZ/M7ubXdtdb1xSFyeilBapySVU8h8OoFaooFSqiihIVIpQBKci6KEg9Q6H9kovIHoCIVQJJCKE1ENFjnAgcaSGC6rEnxBwA04Tx43t2FnvDAfjkNibxgHxnWb2e/u992bee7tCa00YFsffekFY+nUzFtjW0LrvjRXrCDIAaPLlW0nHL0SsZtVoaF98mLrx3pdhOqLtYPHChahZcYYO7KvPFxvRl5XPp1sN3adWiD1ZAqD6XYK1b/dvE5IWryTt2udLFedwc1+9kLp+vbbpoDh+6TklxBeAi9TL0taeWpdmZzQDry0AcO+jQ12RyohqqoYoo8RDwJrU+qXkjWtfi8Xxt58BdQuwQs9qC/afLwCw8tnQbqYAPsgxE1S6F3EAIXux2oQFKm0ihMsOF71dHYx+f3NND68ghCu1YIoePPQN1pGRABkJ6Bus96CutRZMydTl+TvuiRW1m3n0eDl0vRPcEysqdXn+jsQPsrHMquGeXEaY4Yk4wxWcY5V/9scqOMOVUFthatyTy8QyqwZ+kDURKoMWxNKr2EeqVKcTNOajqKoBgOE28U4tdQl5p5bwCw7BWquaZSzAPlwjlithJtp3pTImSqQRrb2Z8PHGigD4RZuNX6JYj6wj7O4TFLbCO/Mn/m8R+h6rYSUb3ekokRY6f/YukArN979jcW+V/S8g0eT/N3VN3kTqWbQ428m9/8k0P/1aIhF36PccEl6EhOcAUCrXKZXXWS3XKd2vc/TRBG9O5ELC17MmWubD2nKhUKZa26Ba2+D3P+4/MNCFwg59oWVeYhkzgN/JDR8deKBoD7Y+ljEjGZ0sosXVTvbc6RHirr2reNy1OXd6pJsQ+gqjk8VWFYmHrwBzW/n+uMPFiRwHB2I7ih8ciHFxIkd/3Omk5tCDV1t+2nNu5sxxpDFNx+huNhVT3/zMDz8usXC3ddaHBj1GHj/As08fwTS7Kt1HBTmyN29vdwAw+/wbwLVOJ3uAD1wi/dUH7Qei66PfyuRj4Ik9is+hglfbkbfR3cnZm7chlUWLdwmprtCohX4HUtlOcQjLYCu+fzGJH2QRKvP3UNz8bWk1qMxjGTOMThZ3kvgLI5AzFfo379UAAAAASUVORK5CYII=");
}

audio::-webkit-media-controls-timeline {
  background-color: #532b5a;
  border-radius: 25px;
  margin-left: 10px;
  margin-right: 10px;
  accent-color: white;
}






    """
    st.experimental_rerun()
st.audio(audio_bytes, format="audio/wav")
