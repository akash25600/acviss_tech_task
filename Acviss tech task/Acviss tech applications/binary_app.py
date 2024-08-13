import streamlit as st

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Streamlit app
st.title("Binary Search")

# Input text box for the sorted list of numbers
input_list = st.text_input("Enter a sorted list of numbers separated by commas:")

# Input number box for the target number
target = st.number_input("Enter the target number:", step=1)

if input_list:
    # Convert the input string into a list of numbers
    try:
        arr = list(map(int, input_list.split(',')))
        # Perform binary search
        result = binary_search(arr, target)
        if result != -1:
            st.write(f"Target {target} found at index: {result}")
        else:
            st.write(f"Target {target} not found in the list.")
    except ValueError:
        st.write("Please enter a valid sorted list of numbers separated by commas.")
