import streamlit as st
import sqlite3

# Function to initialize SQLite database
def init_db():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # Create a table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
    ''')
    conn.commit()
    return conn, cursor

# Function to insert data into the database
def insert_data(cursor, name, age):
    cursor.execute('''
    INSERT INTO users (name, age) VALUES (?, ?)
    ''', (name, age))

# Function to retrieve all data
def get_all_data(cursor):
    cursor.execute('SELECT * FROM users')
    return cursor.fetchall()

# Function to perform a simple query
def get_users_older_than(cursor, age):
    cursor.execute('SELECT * FROM users WHERE age > ?', (age,))
    return cursor.fetchall()

# Streamlit app
def main():
    st.title("SQLite with Streamlit")

    # Initialize database and create table
    conn, cursor = init_db()

    st.header("Insert Data")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0, step=1)

    if st.button("Add User"):
        if name and age:
            insert_data(cursor, name, age)
            conn.commit()
            st.success(f"User {name} added successfully!")
        else:
            st.error("Please provide both name and age.")

    st.header("View Data")
    if st.button("Show All Users"):
        data = get_all_data(cursor)
        st.write("Data from SQLite:")
        st.write(data)

    age_filter = st.number_input("Filter users older than", min_value=0, step=1)
    if st.button("Show Users Older Than"):
        filtered_data = get_users_older_than(cursor, age_filter)
        st.write(f"Users older than {age_filter}:")
        st.write(filtered_data)

    # Close the connection
    conn.close()

if __name__ == "__main__":
    main()
