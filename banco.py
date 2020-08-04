import sqlite3

conn = sqlite3.connect("recursos/UserData.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS Users(
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Email TEXT NOT NULL,
    Password TEXT NOT NULL,
    Estado TEXT NOT NULL
);
""")

# cadastroUsuario()
