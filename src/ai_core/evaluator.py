import os
import json
from groq import Groq

def evaluate_quiz_accuracy(quiz_data: list, original_context: str) -> dict:
    """
    Menggunakan LLM sebagai Juri untuk memvalidasi apakah kuis yang dibuat 
    benar-benar berdasar pada konteks (RAG) atau mengandung halusinasi.
    """
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    
    evaluation_prompt = f"""
    You are a strict Quality Assurance AI for 99 Group.
    Your task is to evaluate a generated property quiz against the retrieved source context.
    
    SOURCE CONTEXT (Truth):
    {original_context}
    
    GENERATED QUIZ TO EVALUATE:
    {json.dumps(quiz_data)}
    
    INSTRUCTIONS:
    1. Verify that every answer and explanation in the quiz is factually supported by the SOURCE CONTEXT.
    2. Check for any hallucinations (information not present in the context).
    3. Output your evaluation in strictly valid RAW JSON format (no markdown blocks).
    
    SCHEMA:
    {{
        "is_valid": true or false,
        "feedback": "Detailed explanation of what is accurate or what is hallucinated."
    }}
    """
    
    try:
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": evaluation_prompt}],
            model="openai/gpt-oss-120b", 
            temperature=0.0, # Temperature 0 agar AI sangat analitis dan tidak kreatif
            response_format={"type": "json_object"}
        )
        
        raw_text = response.choices[0].message.content.strip()
        
        if raw_text.startswith("```json"): raw_text = raw_text[7:-3]
        elif raw_text.startswith("```"): raw_text = raw_text[3:-3]
            
        return json.loads(raw_text)
    except Exception as e:
        return {"is_valid": False, "feedback": f"Evaluasi gagal: {e}"}