import streamlit as st

st.title("Multimodal Stress Detection System")

st.write("This is my AI project for detecting stress using face and voice.")

st.write("Upload an image to detect emotion")

image = st.file_uploader("Upload Image", type=["jpg","png","jpeg"])

if image:
    st.image(image, caption="Uploaded Image", use_column_width=True)

st.write("Voice emotion and stress prediction will appear here.")