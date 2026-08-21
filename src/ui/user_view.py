import streamlit as st
from src.database.db_handler import load_quizzes

def render():
    st.header("🎯 Kuis Karyawan 99 Group")
    quizzes = load_quizzes()
    
    # Filter hanya kuis yang sudah di-publish
    published_quizzes = [q for q in quizzes if q['status'] == 'published']

    if not published_quizzes:
        st.info("Belum ada kuis yang tersedia saat ini.")
        return

    # Dropdown untuk memilih kuis
    quiz_options = {f"Kuis #{q['id']}: {q['topic']}": q for q in published_quizzes}
    selected_quiz_name = st.selectbox("Pilih Kuis untuk Dikerjakan:", list(quiz_options.keys()))
    selected_quiz = quiz_options[selected_quiz_name]

    st.write("---")
    
    # Render soal kuis
    for i, q in enumerate(selected_quiz['quiz_data']):
        st.subheader(f"Q{i+1}: {q['question']}")
        
        choice = st.radio("Pilih jawaban:", q['options'], key=f"q_{selected_quiz['id']}_{i}", index=None)
        
        if st.button(f"Submit Q{i+1}", key=f"btn_{selected_quiz['id']}_{i}"):
            if choice is None:
                st.warning("Pilih jawaban terlebih dahulu.")
            elif choice.strip() == q['answer'].strip():
                st.success("Benar!")
                st.info(f"Penjelasan: {q['explanation']}")
            else:
                st.error(f"Salah. Jawaban yang benar: {q['answer']}")
                st.info(f"Penjelasan: {q['explanation']}")