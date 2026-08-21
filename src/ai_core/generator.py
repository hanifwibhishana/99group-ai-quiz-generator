import os, json
from groq import Groq
from src.tools.web_search import search_99group_context

def generate_quiz_with_rag(topic: str) -> list:
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    
    # 1. Ambil konteks dari internet
    live_context = search_99group_context(topic)
    
    # 2. Masukkan ke dalam prompt
    system_prompt = f"""
    You are a Property Industry Quiz Master for 99 Group.
    Based STRICTLY on the following real-time data, generate a 10-question multiple-choice quiz in valid JSON format.
    RANDOMIZE ANSWER POSITION: The correct answer MUST NOT always be the first option. Randomly distribute the correct answer across the 1st, 2nd, 3rd, and 4th positions throughout the 10 questions to prevent predictable patterns.
        
    
    REAL-TIME DATA:
    {live_context}
    
    Do not invent facts outside this data. Output RAW JSON only.
    Schema: [{{"question": "...", "options": ["...", "...", "...", "..."], "answer": "...", "explanation": "..."}}]
    """
    
    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Topic: {topic}"}
        ],
        model="openai/gpt-oss-120b",
        temperature=0.2
    )
    
    raw_text = response.choices[0].message.content.strip()
    if raw_text.startswith("```json"): raw_text = raw_text[7:-3]
    elif raw_text.startswith("```"): raw_text = raw_text[3:-3]
    
    return json.loads(raw_text)