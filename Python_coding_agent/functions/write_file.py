import os

def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_working_dir):
        return f"Error: '{file_path}' is not in the working directory"

    if not os.path.isfile(abs_file_path):
        parent_dir = os.path.dirname(abs_file_path)
        try:
            os.makedirs(parent_dir)
        except Exception as e:
            return f"Couldn't create parent directories: {parent_dir} = {e}"

}"