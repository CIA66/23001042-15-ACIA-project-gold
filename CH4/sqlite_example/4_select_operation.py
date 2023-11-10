import sqlite3

conn = sqlite3.connect('data/binar_data_science.db')
print("Opened database successfully")

print("List of Users:")
cursor = conn.execute("SELECT * FROM users WHERE umur = 22;")
# print(cursor)

for row in cursor:
    print(row[0])

print()
print("Operation done successfully")
conn.close()

