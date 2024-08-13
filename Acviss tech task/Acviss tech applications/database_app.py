import streamlit as st
import sqlite3

def sqlite_operations():
    # Connect to SQLite database (or create it)
    conn = sqlite3.connect('acviss.db')
    c = conn.cursor()

    # Create a table if it doesn't exist
    c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)''')

    # Insert data (only if the table is empty)
    c.execute("SELECT COUNT(*) FROM users")
    if c.fetchone()[0] == 0:
        c.execute("INSERT INTO users (name) VALUES ('Alice')")
        c.execute("INSERT INTO users (name) VALUES ('Bob')")
        conn.commit()

    # Retrieve all data
    c.execute('SELECT * FROM users')
    results = c.fetchall()

    conn.close()

    return results

def get_user_name(user_id):
    # Connect to SQLite database
    conn = sqlite3.connect('acviss.db')
    c = conn.cursor()

    # Perform a query to get the name by ID
    c.execute("SELECT name FROM users WHERE id = ?", (user_id,))
    result = c.fetchone()

    conn.close()

    if result:
        return result[0]
    else:
        return None

# Streamlit app
st.title("SQLite Operations with Streamlit")

# Display all users
st.subheader("All Users")
results = sqlite_operations()
st.write(results)

# Input box for user ID
user_id = st.number_input("Enter User ID to fetch the name:", min_value=1, step=1)

# Button to fetch the user name
if st.button("Get User Name"):
    user_name = get_user_name(user_id)
    if user_name:
        st.write(f"Name of user with ID {user_id}:", user_name)
    else:
        st.write(f"No user found with ID {user_id}.")
