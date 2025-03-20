import streamlit as st
import subprocess
from PIL import Image
from io import BytesIO
import os
import re

# Define the predefined command
predefined_command = "C:/Users/VATSAL/OneDrive/Documents/DF-GAN-master/code/scripts/sample.bat C:/Users/VATSAL/OneDrive/Documents/DF-GAN-master/code/cfg/bird.yml"

# Streamlit app
st.title("Run Command on Enter App")

# Collect user input for the command
user_input = st.text_input("Enter command and press Enter:")

def write_to_file(data):
    with open("code/example_captions/bird.txt", "w") as file:
       file.write(data+"\n") 


if user_input:
    # Button to trigger writing to file
    if st.button("Write to File"):
        write_to_file(user_input)
        st.success("Data written to file successfully!")
        
with open("code/example_captions/bird.txt", "r") as file:
    file_contents = file.read()

st.subheader("Contents of the File:")
st.write(file_contents)


# JavaScript to capture Enter key press
st.markdown(
    """
    <script>
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Enter') {
                const commandInput = document.getElementById("command-input");
                Streamlit.setComponentValue(commandInput.value);
            }
        });
    </script>
    """,
    unsafe_allow_html=True,
)

# Listen for Enter key press
if st.button("Run Command"):
    try:
        # Execute the predefined command
        result = subprocess.run(predefined_command, shell=True, capture_output=True, text=True)

        # Display command output
        # st.subheader("Command Output:")
        # st.text(result.stdout)

        saved_to_pattern = re.compile(r"saved to(.*?)\n")
        match = saved_to_pattern.search(result.stdout)
        
        if match:
    # Alternatively, directly call the group(1) method to get the extracted content as a string
            saved_to_path = match.group(1)
            saved_to_path = saved_to_path.strip()
            print("Jayu", "Vatsal",saved_to_path)
            saved_to_path = saved_to_path.replace("./", "code/")
            print("Jayu", saved_to_path)
            image_folder = saved_to_path
            image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
            for image_file in image_files:
                image_path = os.path.join(image_folder, image_file)
                image_path = image_path.replace("\\", "/")
                print(image_path)
                image = Image.open(image_path)
                st.image(image, caption=image_file, use_column_width=True)
                
                
        else:
            print("No 'saved to' path found in the command output.")
        # Display any errors or exceptions
        
        
        if result.stderr:
            print("Error Output:")
            print(result.stderr)
            
            
        # image_folder = str(match)  # Replace with the actual folder path
        # image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

        # for image_file in image_files:
        #     image_path = os.path.join(image_folder, image_file)
        #     image = Image.open(image_path)
        #     st.image(image, caption=image_file, use_column_width=True)
        
        # image_path = "code/samples/bird/2024_01_27_20_41_41/"  # Replace with the actual image path
        # image = Image.open(image_path)
        # st.image(image, caption="Image Caption", use_column_width=True)

    except Exception as e:
        print(f"An error occurred: {e}")






