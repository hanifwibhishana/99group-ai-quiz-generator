import streamlit as st
from src.ai_core.generator import generate_quiz_with_rag
from src.database.db_handler import save_quiz

def render():
    st.header("🛠️ Admin Dashboard: Buat Kuis Baru")
    st.write("Sistem akan mencari data terbaru di web sebelum membuat kuis.")

    topic = st.text_input("Masukkan Topik (Contoh: Aturan Pajak Properti 2026)")

    if st.button("Generate & Draft Quiz") and topic:
        with st.spinner("Scraping web & meng-generate kuis dengan gpt-oss-120b"):
            try:
                quiz_data = generate_quiz_with_rag(topic)
                st.session_state['draft_quiz'] = quiz_data
                st.session_state['draft_topic'] = topic
                st.success("Draft Kuis berhasil dibuat!")
            except Exception as e:
                st.error(f"Gagal membuat kuis: {e}")

    # Menampilkan Draft Kuis untuk direview (Human-in-the-Loop)
    if 'draft_quiz' in st.session_state:
        st.subheader("Preview Draft Kuis")
        for i, q in enumerate(st.session_state['draft_quiz']):
            st.write(f"**Q{i+1}: {q['question']}**")
            st.write(f"Jawaban Benar: `{q['answer']}`")
            st.caption(f"Penjelasan: {q['explanation']}")
            st.write("---")

        if st.button("✅ Approve & Publish"):
            save_quiz(st.session_state['draft_topic'], st.session_state['draft_quiz'])
            st.success("Kuis berhasil di-publish ke halaman User!")
            del st.session_state['draft_quiz'] # Bersihkan draft setelah publish