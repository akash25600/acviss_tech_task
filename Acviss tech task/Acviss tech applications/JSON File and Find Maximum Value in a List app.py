import streamlit as st

# Function to find the maximum value in a list
def find_max_value(numbers):
    max_value = max(numbers)
    return max_value

# Streamlit app
def main():
    st.title("Find Maximum Value in a List")

    # Input JSON string
    json_input = st.text_area("Enter your JSON data:", '{"numbers": [23, 45, 12, 89, 34, 67, 91, 38]}')

    if st.button("Find Maximum"):
        try:
            # Convert the input JSON string to a dictionary
            json_data = eval(json_input)
            numbers = json_data['numbers']

            # Find the maximum value
            max_value = find_max_value(numbers)

            st.success(f"The maximum value is: {max_value}")
        except:
            st.error("Invalid JSON data. Please check your input.")

if __name__ == "__main__":
    main()
