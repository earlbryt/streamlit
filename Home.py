import streamlit as st

st.set_page_config(
    page_title="Your App",
    page_icon="👋",
)

st.write("# Welcome to Coral's Hub! 👋")


uploaded_files = st.file_uploader(
    "Choose a CSV file", accept_multiple_files=True
)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)


audio_value = st.audio_input("Leave a voice message")

if audio_value:
    st.audio(audio_value)


pages = {
    "Your account": [
        st.Page("./pages/create_account.py", title="Create your account"),
        st.Page("./pages/manage_account.py", title="Manage your account"),
    ],
    "Resources": [
        st.Page("./pages/learn.py", title="Learn about us"),
        st.Page("./pages/trial.py", title="Try it out"),
    ],
}

import pydeck
import pandas as pd

capitals = pd.read_csv(
    "./capitals.csv",
    header=0,
    names=[
        "Capital",
        "State",
        "Abbreviation",
        "Latitude",
        "Longitude",
        "Population",
    ],
)
capitals["size"] = capitals.Population / 10

point_layer = pydeck.Layer(
    "ScatterplotLayer",
    data=capitals,
    id="capital-cities",
    get_position=["Longitude", "Latitude"],
    get_color="[255, 75, 75]",
    pickable=True,
    auto_highlight=True,
    get_radius="size",
)

view_state = pydeck.ViewState(
    latitude=40, longitude=-117, controller=True, zoom=2.4, pitch=30
)

chart = pydeck.Deck(
    point_layer,
    initial_view_state=view_state,
    tooltip={"text": "{Capital}, {Abbreviation}\nPopulation: {Population}"},
)

event = st.pydeck_chart(chart, on_select="rerun", selection_mode="multi-object")

event.selection


st.write('Leave a Rating')
sentiment_mapping = ["one", "two", "three", "four", "five"]
selected = st.feedback("stars")
if selected is not None:
    st.markdown(f"{selected + 1} star(s).")

import time
time.sleep(0.3)
st.balloons()

pg = st.navigation(pages)
pg.run()