import os
import shutil

def duplicate_folder_template(code_number, project_name):
    # Define source and destination paths
    source_path = "_folder_template"
    destination_path = f"{code_number} - {project_name}"
    
    # Create the new project folder
    os.makedirs(destination_path, exist_ok=True)
    
    # Function to rename project files
    def rename_project_files(root):
        for file in os.listdir(root):
            if file.endswith(('.prproj', '.sesx', '.psd', '.aep', '.fcpx', '.ppj', '.veg', '.drp', '.rpp')):
                old_file_path = os.path.join(root, file)
                new_file_path = os.path.join(root, f"{code_number} - {project_name}{os.path.splitext(file)[1]}")
                if not os.path.exists(new_file_path):
                    os.rename(old_file_path, new_file_path)
                else:
                    # Handle file name conflicts
                    i = 1
                    while True:
                        new_file_path = os.path.join(root, f"{code_number} - {project_name} ({i}){os.path.splitext(file)[1]}")
                        if not os.path.exists(new_file_path):
                            os.rename(old_file_path, new_file_path)
                            break
                        i += 1
    
    # Walk through the source directory and duplicate files and folders
    for root, dirs, files in os.walk(source_path):
        # Construct the destination directory
        dest_dir = os.path.join(destination_path, os.path.relpath(root, source_path))
        os.makedirs(dest_dir, exist_ok=True)
        
        # Duplicate files
        for file in files:
            shutil.copy(os.path.join(root, file), os.path.join(dest_dir, file))
        
        # Rename project files
        rename_project_files(dest_dir)

# Main program
if __name__ == "__main__":
    code_number = input("Enter code number for the project: ")
    project_name = input("Enter project name: ")
    duplicate_folder_template(code_number, project_name)
    print("Folder template duplicated successfully!")
