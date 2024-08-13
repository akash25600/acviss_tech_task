import streamlit as st

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

# Streamlit app
st.title("Factorial Calculator")

# Input number box
number = st.number_input("Enter a number to calculate its factorial:", min_value=0, value=0, step=1)

if number is not None:
    # Calculate factorial
    result = factorial(int(number))
    
    # Display the factorial
    st.write(f"Factorial of {int(number)} is: {result}")
