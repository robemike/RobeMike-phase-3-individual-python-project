import sqlite3

conn = sqlite3.connect("sessions.db")
cursor = conn.cursor()