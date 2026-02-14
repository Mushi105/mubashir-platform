from fastapi import FastAPI
import psycopg2
import os
import httpx
from datetime import date

app = FastAPI()
DB_URL = os.getenv("DATABASE_URL", "postgresql://postgres:mubashir.105@mubashir-db:5432/postgres")

@app.get("/ai-summarize")
async def ai_summarize():
    try:
        conn = psycopg2.connect(DB_URL)
        cur = conn.cursor()
        
        # Sirf wo news uthayein jin ki summary abhi tak nahi bani
        cur.execute("SELECT id, title FROM tech_news WHERE summary IS NULL OR summary = ''")
        news_items = cur.fetchall()
        
        results = []
        async with httpx.AsyncClient(timeout=120.0) as client:
            for item in news_items:
                news_id, title = item
                
                # Ollama (Mistral) ko request bhenjna
                response = await client.post(
                    "http://mubashir-ai-engine:11434/api/generate",
                    json={
                        "model": "mistral",
                        "prompt": f"As a Solution Architect, summarize this in one short sentence: {title}",
                        "stream": False
                    }
                )
                
                summary = response.json().get("response", "No summary generated")
                
                # Database mein summary save karna
                cur.execute("UPDATE tech_news SET summary = %s WHERE id = %s", (summary, news_id))
                results.append({"id": news_id, "summary": summary})
        
        conn.commit()
        cur.close()
        conn.close()
        return {"status": "AI processing complete", "processed_items": len(results), "details": results}
    
    except Exception as e:
        return {"error": str(e)}

@app.get("/view-news")
def view_news():
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()
    cur.execute("SELECT title, summary, status FROM tech_news ORDER BY id DESC")
    rows = cur.fetchall()
    return [{"title": r[0], "summary": r[1], "status": r[2]} for r in rows]
