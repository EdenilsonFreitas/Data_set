import streamlit as st
from streamlit_option_menu import option_menu

# 1. as sidebar menu

with st.sidebar:
    
    selected = option_menu(
        menu_title=None,  # required
        options=["Home", "Projects", "Contact"],  # required
    )

if selected == "Home":
    st.title(f"You have selected {selected}")
elif selected == "Projects":
    st.title(f"You have selected {selected}")
elif selected == "Contact":
    st.title(f"You have selected {selected}")

st.title("Streamlit Option Menu")

