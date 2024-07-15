import os
import shutil
import sys


def copy_files_recursive(src, dest):
    
    if not os.path.exists(src):
        print(f"Source directory not exists: {src}")
        return
    
    if not os.path.exists(dest):
        os.makedirs(dest)

    for item in os.listdir(src):
        item_path = os.path.join(src, item)

        if os.path.isdir(item_path):
            copy_files_recursive(item_path, dest)
        elif os.path.isfile(item_path):
            file_extension = os.path.splitext(item)[1][1:] 
            if file_extension: 
                extension_dir = os.path.join(dest, file_extension)

                if not os.path.exists(extension_dir):
                    os.makedirs(extension_dir)

                try:
                    shutil.copy2(item_path, extension_dir)
                except Exception as e:
                    print(f"Failed to copy file {item_path}: {e}")


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Entry <path to source directory> [path to destination directory]")
        sys.exit(1)

    source_directory = sys.argv[1]
    destination_directory = sys.argv[2] if len(sys.argv) > 2 else os.path.join(source_directory, 'dist')

    copy_files_recursive(source_directory, destination_directory)

