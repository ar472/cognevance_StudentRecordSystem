import requests
import sqlite3
import pandas as pd
import time
from datetime import datetime

# 1. API se Data fetch karna
def fetch_data():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    return response.json()

# 2. Database mein Save karna
def save_to_db(data):
    conn = sqlite3.connect('enterprise.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS data (id INTEGER, title TEXT)')
    for item in data[:5]:
        cursor.execute("INSERT INTO data VALUES (?, ?)", (item['id'], item['title']))
    conn.commit()
    conn.close()
    print("Automation: Data saved to database!")

# 3. Excel Report Generate karna
def export_to_excel():
    conn = sqlite3.connect('enterprise.db')
    df = pd.read_sql_query("SELECT * FROM data", conn)
    filename = f"Report_{datetime.now().strftime('%Y-%m-%d')}.xlsx"
    df.to_excel(filename, index=False)
    print(f"Excel report generate ho gayi: {filename}")
    conn.close()

# Run
if __name__ == "__main__":
    data = fetch_data()
    save_to_db(data)
    export_to_excel()