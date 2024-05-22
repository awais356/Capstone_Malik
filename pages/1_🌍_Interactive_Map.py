import streamlit as st
import leafmap.foliumap as leafmap

markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://www.google.com/search?sca_esv=8b3c2fe050857b40&sca_upv=1&rlz=1C1GCEA_enCA1108CA1108&sxsrf=ADLYWIKoP1MpZtkX389JfUnjLqBiSNlYCg:1716382799857&q=forest+inventory&uds=ADvngMiIMiMH9LyyITANaU-tP7TxQuwMPkmMIDT9KRv6DBOKIQcfaCui7d1kodamqjWYyeZmhfZNpuLIXVfSmc8wrnNSMGJsWz7XZyAO7e09qkRFXKsDOGOcJamnquTwQKT5totFTZ7pktUHDpdx43SPDjc8jc7Is-U2UUtAeJc3p0oKQ2bOAebJR3UK89Q7-Z0wfxQPYqIq_viNhTqlk2pdwYg0cEfM06nJz7LgbL_9BJKjpmzMMIDpfWSo92059MgozjEYi-IhXJy2k2nL-Y24cTC4IbImBGfFzzm-SCXgCXguu2qRXUZWzh0OMHPlZPPqEFuvph5xbXokrQwZAGcjYK9QVeuhkA&udm=2&prmd=ivnsmbtz&sa=X&ved=2ahUKEwjsitWYqKGGAxUNHzQIHX2LATcQtKgLegQIEBAB&biw=1280&bih=855&dpr=1#vhid=rRaLSrPtAeaVVM&vssid=mosaic"
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
