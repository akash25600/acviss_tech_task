import streamlit as st

def sort_list(nums):
    return sorted(nums)

# Streamlit app
st.title("List Sorter")

# Input text box for list of numbers
input_text = st.text_input("Enter a list of numbers separated by commas:")

if input_text:
    # Convert the input string into a list of numbers
    try:
        nums = list(map(int, input_text.split(',')))
        # Sort the list
        sorted_nums = sort_list(nums)
        # Display the sorted list
        st.write("Sorted List:", sorted_nums)
    except ValueError:
        st.write("Please enter a valid list of numbers separated by commas.")
