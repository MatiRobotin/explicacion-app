import streamlit as st

st.set_page_config(page_title="Explicación", page_icon="📄", layout="centered")

st.markdown(
    """
    <style>
        /* Ocultar el menú y el pie de Streamlit para dejar solo el texto */
        #MainMenu, footer, header { visibility: hidden; }

        /* Centrar vertical y horizontalmente dentro de la ventana */
        .block-container {
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .centro {
            text-align: center;
            font-size: 4rem;
            font-weight: 700;
            letter-spacing: 0.02em;
            margin: 0;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<p class="centro">Explicación</p>', unsafe_allow_html=True)
