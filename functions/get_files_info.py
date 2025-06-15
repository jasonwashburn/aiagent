import os


def get_files_info(working_directory, directory=None):
    if directory is None:
        directory = "."

    abs_working_directory = os.path.abspath(working_directory)
    abs_directory = os.path.abspath(os.path.join(abs_working_directory, directory))
    if not os.path.isdir(abs_directory):
        return f'Error: "{directory}" is not a directory'

    if not abs_directory.startswith(abs_working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    output_strings = []
    for item in os.listdir(abs_directory):
        absolute_item_path = os.path.join(abs_directory, item)
        filename = item
        file_size = os.path.getsize(absolute_item_path)
        is_dir = os.path.isdir(absolute_item_path)
        output_strings.append(
            f"- {filename}: file_size={file_size} bytes, is_dir={is_dir}"
        )

    return "\n".join(output_strings)
