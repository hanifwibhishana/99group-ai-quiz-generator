import streamlit as st
from dotenv import load_dotenv

# Memuat .env file (termasuk API Key Groq dan Tavily)
load_dotenv()

st.set_page_config(page_title="99 Group RAG Quiz", page_icon="🏢")

menu = st.sidebar.selectbox("Pilih Hak Akses:", ["Admin (Buat Kuis)", "Karyawan (Ambil Kuis)"])

if menu == "Admin (Buat Kuis)":
    import src.ui.admin_view as admin_view
    admin_view.render()
else:
    import src.ui.user_view as user_view
    user_view.render()