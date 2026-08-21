import os
from tavily import TavilyClient

def search_99group_context(topic: str) -> str:
    """Mencari konteks di web menggunakan Tavily API."""
    tavily_key = os.getenv("TAVILY_API_KEY")
    if not tavily_key:
        return "Tidak ada API key Tavily."
        
    client = TavilyClient(api_key=tavily_key)
    try:
        # Fokuskan pencarian pada konteks industri properti / 99 Group
        query = f"99.co property market updates {topic}"
        response = client.search(query=query, search_depth="basic", max_results=10)
        
        # Gabungkan teks hasil pencarian
        context = "\n\n".join([res['content'] for res in response.get('results', [])])
        return context
    except Exception as e:
        return f"Gagal mengambil data: {e}"