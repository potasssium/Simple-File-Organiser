import os
import shutil

#define the directory 
DIRECTORY_TO_ORGANIZE = '/path/to/your/directory'

FOLDER_PATHS = {
    'Images': '/path/to/your/directory',
    'Documents': '/path/to/your/directory',
    'Videos': '/path/to/your/directory',
    'Others': '/path/to/your/directory'
}

FILE_TYPES = {
    'Images': ['jpg', 'jpeg', 'png', 'gif'],
    'Documents': ['txt', 'pdf', 'docx', 'xlsx'],
    'Videos': ['mp4', 'avi', 'mov'],
}


def organize_files(directory):
    # Ensure destination folders exist
    for folder_path in FOLDER_PATHS.values():
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Move files to the corresponding folders
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_extension = filename.split('.')[-1].lower()
            moved = False
            for folder, extensions in FILE_TYPES.items():
                if file_extension in extensions:
                    dest_folder = FOLDER_PATHS[folder]
                    shutil.move(file_path, os.path.join(dest_folder, filename))
                    moved = True
                    break
            if not moved:
                # Move unknown file types to "Others"
                other_folder = FOLDER_PATHS['Others']
                shutil.move(file_path, os.path.join(other_folder, filename))

if __name__ == '__main__':
    DIRECTORY_TO_ORGANIZE = '/path/to/your/directory'
    organize_files(DIRECTORY_TO_ORGANIZE)
    print('Files have been organized!')
    
    
