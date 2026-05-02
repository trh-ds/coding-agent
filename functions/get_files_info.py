import os

def get_files_info(working_directory, directory="."):
    abs_working_directory = os.path.abspath(working_directory)
    abs_directory = os.path.abspath(directory)
    if not abs_directory.startswith(abs_working_directory):
        print(f"Error: The directory '{directory}' is not within the working directory '{working_directory}'.")
        return
    
    

    
    
get_files_info(os.getcwd(), ".")
