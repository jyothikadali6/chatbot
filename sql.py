import sqlite3

# Connect to SQLite database (creates DB if not exists)
connection = sqlite3.connect("student.db")

# Create a cursor object
cursor = connection.cursor()

# Create the STUDENT table
table_info = """
DROP TABLE IF EXISTS STUDENT;
CREATE TABLE STUDENT (
    NAME TEXT,
    CLASS TEXT,
    SECTION TEXT,
    MARKS INTEGER
);
"""
cursor.executescript(table_info)

# Insert records
students = [
    ('jyothi', 'IT', 'A', 90),
    ('Durga', 'CSE', 'B', 100),
    ('srivalli', 'IT', 'A', 86),
    ('anjani', 'CSE', 'A', 50),

]

cursor.executemany("INSERT INTO STUDENT VALUES (?, ?, ?, ?)", students)

# Display all records
print("The inserted records are:")
cursor.execute("SELECT * FROM STUDENT")
for row in cursor.fetchall():
    print(row)

# Commit and close connection
connection.commit()
connection.close()
