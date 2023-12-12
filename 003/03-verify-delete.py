import os

def delete_files_in_folder(folder_path, use_found_prefix=False):
    try:
        # Get the list of files in the folder
        file_list = os.listdir(folder_path)

        # Choose the prefix based on the option
        prefix = "Found for deletion" if use_found_prefix else "Deleted"

        # Iterate through the files and perform the operation
        for file_name in file_list:
            file_path = os.path.join(folder_path, file_name)
            file_path += ".html"
            print (file_path)
            
            # Check if it's a file before attempting to delete
            if os.path.isfile(file_path):
                # Choose the appropriate prefix for the message
                operation_prefix = f"{prefix}:" if use_found_prefix else "Deleted:"

                # Perform the operation (delete or found for deletion)
                if use_found_prefix:
                    print(f"Found for deletion: {file_path}")
                else:
                    os.unlink(file_path)
                    print(f"Deleted: {file_path}")

        print("All files processed successfully.")

    except Exception as e:
        print(f"Error: {e}")

# Specify the folder path
folder_path = './Underv231212/003/'

# Call the function with the default prefix ("Deleted")
# delete_files_in_folder(folder_path)

# Call the function with the alternative prefix ("Found for deletion")
delete_files_in_folder(folder_path, use_found_prefix=True)
