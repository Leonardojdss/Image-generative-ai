import streamlit as st
from generate_image import text_to_image, image_and_text_to_image

st.title("Desinger generativo")

tab1, tab2 = st.tabs(["Criar nova imagem", "Editar imagem e referência"])

with tab1:
    
    st.title("Criar nova imagem")

    prompt_input = st.text_input("Inserir a descrição da imagem", key="prompt_input")

    number_of_images_create = st.select_slider("Quantas imagens devem ser geradas?", options=[1, 2, 3, 4], value=1, key="number_of_images_create")

    if st.button("Gerar imagem", key="generate_image"):
        if prompt_input:
            with st.spinner("Gerando imagem..."):
                image = text_to_image(prompt_input, number_of_images_create)
                st.image(image, width=300)
        else:
            st.warning("Por favor, insira uma descrição para gerar a imagem.")

with tab2:
    st.title("Editar imagem com referência")

    prompt_input = st.text_input("Inserir a descrição da imagem", key="prompt_input_edit")

    number_of_images_edit = st.select_slider("Quantas imagens devem ser geradas?", options=[1, 2, 3, 4], value=1, key="number_of_images_edit")

    uploaded_files = st.file_uploader("Escolha uma ou mais imagens", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

    if st.button("Gerar imagem", key="generate_image_edit"):
        if prompt_input and uploaded_files:
            with st.spinner("Gerando imagem..."):
                image = image_and_text_to_image(prompt_input, uploaded_files, number_of_images_edit)
                st.image(image, width=300)
        else:
            st.warning("Por favor, insira uma descrição e faça o upload de uma imagem para gerar a imagem.")