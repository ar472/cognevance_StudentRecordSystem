import sqlite3
import matplotlib.pyplot as plt

# Database connection
conn = sqlite3.connect('expenses.db')
cursor = conn.cursor()

# Table banana
cursor.execute('''CREATE TABLE IF NOT EXISTS expenses 
                  (id INTEGER PRIMARY KEY, category TEXT, amount REAL)''')

def add_expense(category, amount):
    cursor.execute("INSERT INTO expenses (category, amount) VALUES (?, ?)", (category, amount))
    conn.commit()

def show_chart():
    # Yahan se data lekar matplotlib se graph banana hai
    pass

# Aise hi menu-driven system banana hoga