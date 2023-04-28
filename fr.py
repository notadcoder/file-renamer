import os


def rename_files(directory, pattern, new_name_format):
    # Loop through all files in the directory
    for i, filename in enumerate(os.listdir(directory)):
        # Check if the file matches the pattern
        if pattern in filename:
            # Generate the new name for the file
            new_name = new_name_format.format(i+1)
            # Rename the file
            os.rename(os.path.join(directory, filename),
                      os.path.join(directory, new_name + os.path.splitext(filename)[1]))


def main():
    # Prompt the user for the directory, pattern, and new name format
    directory = input("Enter the directory containing the files to rename: ")
    pattern = input("Enter the pattern to match for the files: ")
    new_name_format = input("Enter the new name format (use {filename} to include the original filename): ")

    # Rename the files in the directory
    rename_files(directory, pattern, new_name_format)


if __name__ == '__main__':
    main()
