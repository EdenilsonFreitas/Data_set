import streamlit as st
from streamlit_option_menu import option_menu

# 1. as sidebar menu

with st.sidebar:
    
    selected = option_menu(
        menu_title=None,  # required
        options=["Home", "Projects", "Contact"],  # required
        icons=["house","book","envelope"], #optionol
        menu_icon= "cast",
        default_index=0,
        orientation="horizontal",
        styles={
            "container":{
                "padding":"0!important", "backgraund-color"
                "icon":{
                    "color":"orange","font-size":"25px"
                },
                "nav-link":{"font-size":"25px","text-align":"left","marigin":"0px",
                "--hover-color":"#eee",

                },
                "nav-link-selected":{"backgraund-color":"green"},
            },
        },
    )

if selected == "Home":
    st.title(f"You have selected {selected}")
elif selected == "Projects":
    st.title(f"You have selected {selected}")
elif selected == "Contact":
    st.title(f"You have selected {selected}")

st.title("Streamlit Option Menu")

