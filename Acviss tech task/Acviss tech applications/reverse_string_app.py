import streamlit as st

def reverse_string(s):
    return s[::-1]

# Streamlit app
st.title("String Reverser")

# Input text box
input_text = st.text_input("Enter a string to reverse:")

if input_text:
    # Reverse the string
    reversed_text = reverse_string(input_text)
    
    # Display the reversed string
    st.write("Reversed String:", reversed_text)
