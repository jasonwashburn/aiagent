import os

def write_file(working_directory, file_path, content):
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(abs_working_directory, file_path))

    if not abs_file_path.startswith(abs_working_directory):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    try:
        with open(abs_file_path, "w") as f:
            f.write(content)
    except Exception as e:
        return f'Error: Failed to write to "{file_path}": {str(e)}'

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'