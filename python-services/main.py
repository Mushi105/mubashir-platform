from fastapi import FastAPI
import psycopg2
import os
from datetime import date

app = FastAPI()
DB_URL = os.getenv("DATABASE_URL", "postgresql://postgres:mubashir.105@mubashir-db:5432/postgres")

# --- NEW: DATABASE INITIALIZER ---
@app.get("/setup-db")
def setup_db():
    try:
        conn = psycopg2.connect(DB_URL)
        cur = conn.cursor()
        
        # Table create karne ki command
        cur.execute("""
            CREATE TABLE IF NOT EXISTS tech_news (
                id SERIAL PRIMARY KEY,
                title TEXT UNIQUE,
                source VARCHAR(100),
                status VARCHAR(20),
                published_at DATE
            );
        """)
        
        conn.commit()
        cur.close()
        conn.close()
        return {"message": "Tables created successfully! Now you can crawl news."}
    except Exception as e:
        return {"error": str(e)}

@app.get("/crawl-news")
async def crawl_news():
    fake_news_source = [
        {"title": "Quantum Computing in Banking 2026", "source": "TechNews"},
        {"title": "The Rise of AI Agents in Fintech", "source": "FinanceAI"},
        {"title": "How .NET 9 is Changing Enterprise Apps", "source": "DevMag"}
    ]
    
    try:
        conn = psycopg2.connect(DB_URL)
        cur = conn.cursor()
        for news in fake_news_source:
            cur.execute(
                "INSERT INTO tech_news (title, source, status, published_at) VALUES (%s, %s, %s, %s) ON CONFLICT (title) DO NOTHING",
                (news['title'], news['source'], 'NEW', date.today())
            )
        conn.commit()
        cur.close()
        conn.close()
        return {"message": "News crawled successfully!"}
    except Exception as e:
        return {"error": str(e)}

@app.get("/view-news")
def view_news():
    try:
        conn = psycopg2.connect(DB_URL)
        cur = conn.cursor()
        cur.execute("SELECT title, status, published_at FROM tech_news ORDER BY published_at DESC")
        rows = cur.fetchall()
        return [{"title": r[0], "status": r[1], "date": r[2]} for r in rows]
    except Exception as e:
        return {"error": str(e)}
