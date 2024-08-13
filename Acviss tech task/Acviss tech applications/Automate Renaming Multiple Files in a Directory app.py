import os
import time
import streamlit as st

def rename_files_with_timestamp(directory):
    # Get a list of all files in the directory
    files = os.listdir(directory)

    renamed_files = []

    # Iterate through each file
    for file_name in files:
        # Get the full path of the file
        file_path = os.path.join(directory, file_name)

        # Check if the item is a file (not a directory)
        if os.path.isfile(file_path):
            # Get the current timestamp
            timestamp = int(time.time())

            # Create a new file name with the timestamp
            new_file_name = f"file_{timestamp}.txt"
            new_file_path = os.path.join(directory, new_file_name)

            # Rename the file
            os.rename(file_path, new_file_path)
            renamed_files.append((file_name, new_file_name))

            # Add a small delay to ensure a unique timestamp
            time.sleep(1)

    return renamed_files

# Streamlit app
st.title("File Renaming Tool")

# Directory path input
directory_path = st.text_input("Enter the directory path where the files are located:")

if st.button("Rename Files"):
    if os.path.exists(directory_path) and os.path.isdir(directory_path):
        renamed_files = rename_files_with_timestamp(directory_path)
        if renamed_files:
            st.success("Files renamed successfully!")
            for old_name, new_name in renamed_files:
                st.write(f"Renamed: {old_name} -> {new_name}")
        else:
            st.write("No files found in the directory.")
    else:
        st.error("The provided directory path does not exist or is not a directory.")
