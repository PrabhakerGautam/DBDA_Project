import streamlit as st 

st.set_page_config(page_title="Home",
                   layout='wide',
                   page_icon='./images/home.png')

st.title("YOLO V8 for License Plate Recognition App")
st.caption('This web application demostrate License Plate detection and reading text from the number plate')

# Content
st.markdown("""
### This App detects objects from Images
- Automatically detects License Platefrom image
- [Click here for App](/YOLO_for_License/)  
            """)