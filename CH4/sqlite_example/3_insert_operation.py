import sqlite3

conn = sqlite3.connect('data/binar_data_science.db')
print("Opened database successfully")

# conn.execute("INSERT INTO users (username, email, umur) VALUES ('binaria', 'binaria@binar.com', 52)")
# conn.execute("INSERT INTO users VALUES ('bintang', 'bintang@binar.com', 42, 'Bandung')")
conn.execute("INSERT INTO users VALUES ('bintang', 'bintang@binar.com', 32, 'jakarta timur')")

conn.commit()
print("Records created successfully")
conn.close()

