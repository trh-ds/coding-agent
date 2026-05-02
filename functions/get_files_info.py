import os

def get_files_info(working_directory, directory="."):
    abs_working_directory = os.path.abspath(working_directory)
    abs_directory = os.path.abspath(directory)
    if not abs_directory.startswith(abs_working_directory):
        print(f"Error: The directory '{directory}' is not within the working directory '{working_directory}'.")
        return
    
    final_response =""
    
    contents = os.listdir(abs_directory)
    for content in contents:
        content_path = os.path.join(abs_directory, content)
        if os.path.isfile(content_path):
            size = os.path.getsize(content_path)
            final_response += f"File: {content}, Size: {size} bytes\n"
        elif os.path.isdir(content_path):
            final_response += f"Directory: {content}\n"

    return final_response

get_files_info(os.getcwd(), "/mnt/c/Users/Tirth Patel/OneDrive/Desktop/Python_Projects/AI_Agent/calculator")
