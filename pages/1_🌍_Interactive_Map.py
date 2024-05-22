import streamlit as st
import leafmap.foliumap as leafmap

markdown = """
App to vizualize the Forest Data of Cornerbrook
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo ='https://i.imgur.com/UbOXYAU.png'
st.sidebar.image(logo)


st.title("Visulizing Forest")

col1, col2 = st.columns([4, 1])
options = list(leafmap.basemaps.keys())
index = options.index("OpenTopoMap")

with col2:

    basemap = st.selectbox("Select a basemap:", options, index)


with col1:

    m = leafmap.Map(
        locate_control=True, latlon_control=True, draw_export=True, minimap_control=True
    )
    m.add_basemap(basemap)
    m.to_streamlit(height=700)
