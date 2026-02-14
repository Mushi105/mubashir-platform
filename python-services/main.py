from fastapi import FastAPI
import psycopg2
import os
import httpx # Is se hum internet se news uthayenge
from datetime import date

app = FastAPI()
DB_URL = os.getenv("DATABASE_URL", "postgresql://postgres:mubashir.105@mubashir-db:5432/postgres")

@app.get("/crawl-news")
async def crawl_news():
    # Mock News Fetching (Yahan hum TechCrunch ya Google News ka RSS feed bhi laga sakte hain)
    fake_news_source = [
        {"title": "Quantum Computing in Banking 2026", "source": "TechNews"},
        {"title": "The Rise of AI Agents in Fintech", "source": "FinanceAI"},
        {"title": "How .NET 9 is Changing Enterprise Apps", "source": "DevMag"}
    ]
    
    try:
        conn = psycopg2.connect(DB_URL)
        cur = conn.cursor()
        
        for news in fake_news_source:
            # Check karein ke ye title pehle se to nahi?
            cur.execute("SELECT id FROM tech_news WHERE title = %s", (news['title'],))
            if not cur.fetchone():
                cur.execute(
                    "INSERT INTO tech_news (title, source, status, published_at) VALUES (%s, %s, %s, %s)",
                    (news['title'], news['source'], 'NEW', date.today())
                )
        
        conn.commit()
        cur.close()
        conn.close()
        return {"message": f"Successfully crawled {len(fake_news_source)} news items!"}
    except Exception as e:
        return {"error": str(e)}

@app.get("/view-news")
def view_news():
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()
    cur.execute("SELECT title, status, published_at FROM tech_news ORDER BY published_at DESC")
    rows = cur.fetchall()
    return [{"title": r[0], "status": r[1], "date": r[2]} for r in rows]
