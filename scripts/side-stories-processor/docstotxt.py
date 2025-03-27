import textract
import os

def docx_to_txt_and_modify_in_place(file_path):
    """
    Extracts text from a .docx file, modifies the lines, saves it as .txt, and removes the .docx.

    Args:
        file_path (str): The path to the .docx file.
    """
    try:
        txt_file_path = os.path.splitext(file_path)[0] + ".txt"  # Create .txt path from .docx path
        text = textract.process(file_path).decode('utf-8')
        text_lines = text.split("\n")
        modified_lines = []
        index = 0
        for line in text_lines:
            index += 1
            if index == 1:
                modified_lines.append(line)
                continue
            else:
                index = 0

        with open(txt_file_path, 'w', encoding='utf-8') as f:
            f.write("\n".join(modified_lines))
        print(f"Successfully extracted and modified text from '{file_path}' to '{txt_file_path}'")

        os.remove(file_path)  # Remove the original .docx file
        print(f"Removed: {file_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

def process_directory_docx_to_txt_in_place(directory_path):
    """
    Scans a directory for .docx files, converts them to .txt, modifies the lines, and removes the .docx.

    Args:
        directory_path (str): The path to the directory containing .docx files.
    """
    for filename in os.listdir(directory_path):
        if filename.endswith(".docx"):
            file_path = os.path.join(directory_path, filename)
            docx_to_txt_and_modify_in_place(file_path)

# Example usage:
input_directory = "chapters/cont"  # Replace with your input directory

process_directory_docx_to_txt_in_place(input_directory)