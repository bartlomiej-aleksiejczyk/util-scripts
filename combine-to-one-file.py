import os

def collect_files_content(start_path, output_file, file_extensions):
    """
    Recursively collects the contents of files with specific extensions starting
    from the given directory, and writes them to a single output file.

    Each file's content is preceded by the file name and followed by a series of
    dashes to separate the contents of different files.

    Args:
        start_path (str): The starting directory path where the search for files begins.
        output_file (str): The path to the file where the contents will be written.
        file_extensions (tuple): A tuple of file extension strings to include in the search.

    The function does not return any value; it writes directly to the output file.
    """
    with open(output_file, 'w') as outfile:
        for root, dirs, files in os.walk(start_path):
            for file in files:
                if file.endswith(file_extensions):
                    file_path = os.path.join(root, file)
                    outfile.write(f"{file}\n")
                    try:
                        with open(file_path, 'r') as infile:
                            outfile.write(infile.read())
                    except UnicodeDecodeError:
                        outfile.write("Error reading this file due to encoding issues.\n")
                    outfile.write("\n----------\n")

if __name__ == "__main__":
    FILE_EXTENSIONS = ('.xml', '.java', '.properties')
    OUTPUT_FILENAME = 'combined_files.txt'
    current_directory = '.'
    collect_files_content(current_directory, OUTPUT_FILENAME, FILE_EXTENSIONS)
