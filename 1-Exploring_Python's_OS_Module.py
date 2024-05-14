import os

# Task 1: Directory Inspector

def list_directory_contents(path): # Function to list all files and directories from a specified path
    try:
        return os.listdir(path)
    except Exception as e: # Return the error to user if detected
        return f"Error: {e}"
    
# Task 2: File Size Reporter

def report_file_sizes(directory): # Function to list only files and their sizes in a specified directory
    all_files_names = list(os.listdir(directory)) # retrieve all files from provided path
    result = dict() # Store result in a dictionary

    for file in all_files_names:
        if (os.path.isfile(file)): # Check to see if it is a file or a folder. Only files are listed
            result[file] = os.stat(file).st_size # Store size in bytes in dictionary
    
    return result # Return the dictionary with all sizes for only files

# Task 3: File Extension Counter:

def count_file_extensions(directory): # Function to count and print number of files of each extention type in specified directory
    all_file_names = list(os.listdir(directory)) # retrieve all files from provided path
    result = dict() # Store results in a dictionary

    for file in all_file_names:
        if (os.path.isfile(file)): # Check to see if it is a file or a folder. Only files are considered
            _, extension = os.path.splitext(file) # Split the file name into two strings. One is the file name, and the other is the extension
            extension = extension[1:].upper() # Remove the '.' at the start of the extension and capitalize for better formatting

            if extension in result.keys(): # If a file with the same extension has already been viewed, the total is updated in the dictionary
                result[extension] = result[extension] + 1
            else: # If a new file extension is viewed, a new slot in the dictionary will be created
                result[extension] = 1
        
    return result


# Testing
correct_path = "C:/Users/tejas/OneDrive/Documents/2024/Coding Temple/Module 3/File Handling"
incorrect_path = "C:/Users/tejas/OneDrive/Documents/2024/Coding Temple/Module 3/File Handlin"

# Task 1
print(list_directory_contents(correct_path))
print(list_directory_contents(incorrect_path))
print()

# Task 2
for file, size in report_file_sizes(correct_path).items():
    print(f"{file}: {size} Bytes")
print()

# Task 3
for extension, amount in count_file_extensions(correct_path).items():
    print(f"{extension}: {amount}")