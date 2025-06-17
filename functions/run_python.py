import subprocess
import os

def run_python_file(working_directory, file_path):
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(abs_working_directory, file_path))

    if not abs_file_path.startswith(abs_working_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'

    if not abs_file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    output = ""
    try:
        result = subprocess.run(["python3", file_path], capture_output=True, text=True, cwd=abs_working_directory, timeout=30)
        output += f"STDOUT: {result.stdout}\n"
        output += f"STDERR: {result.stderr}\n"
        if result.returncode != 0:
            output += f"Process exited with code {result.returncode}\n"
        return output
    except Exception as e:
        return f"Error: executing Python file: {e}"
