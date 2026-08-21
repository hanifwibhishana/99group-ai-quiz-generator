import json
import os

DB_PATH = "data/quizzes.json"

def init_db():
    """Membuat folder dan file JSON dengan array kosong jika belum ada atau file kosong."""
    if not os.path.exists("data"):
        os.makedirs("data")
        
    # Buat file dengan awalan [] jika file tidak ada ATAU ukuran filenya 0 bytes (kosong)
    if not os.path.exists(DB_PATH) or os.path.getsize(DB_PATH) == 0:
        with open(DB_PATH, "w") as f:
            json.dump([], f)

def load_quizzes():
    """Membaca semua kuis dari file dengan penanganan error JSON."""
    init_db()
    
    try:
        with open(DB_PATH, "r") as f:
            return json.load(f)
    except json.decoder.JSONDecodeError:
        # Jika file corrupt atau kosong secara tiba-tiba, reset dengan mengembalikan list kosong
        return []

def save_quiz(topic, quiz_data, status="published"):
    """Menyimpan kuis baru ke dalam file JSON."""
    quizzes = load_quizzes()
    
    new_quiz = {
        "id": len(quizzes) + 1,
        "topic": topic,
        "status": status,
        "quiz_data": quiz_data
    }
    quizzes.append(new_quiz)
    
    with open(DB_PATH, "w") as f:
        json.dump(quizzes, f, indent=4)