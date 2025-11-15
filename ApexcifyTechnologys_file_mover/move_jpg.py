import os
import shutil

# Define source and destination directories
source_dir = 'source_folder'  # Relative to script directory
dest_dir = 'jpg_files'  # New folder to move .jpg files

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
source_path = os.path.join(script_dir, source_dir)
dest_path = os.path.join(script_dir, dest_dir)

# Create destination directory if it doesn't exist
if not os.path.exists(dest_path):
    os.makedirs(dest_path)

# Check if source directory exists
if not os.path.exists(source_path):
    print(f"Source directory '{source_path}' does not exist.")
    exit(1)

# Move all .jpg files from source to destination
moved_count = 0
for filename in os.listdir(source_path):
    if filename.lower().endswith('.jpg'):
        src_file = os.path.join(source_path, filename)
        dst_file = os.path.join(dest_path, filename)
        shutil.move(src_file, dst_file)
        print(f"Moved {filename} to {dest_dir}")
        moved_count += 1

print(f"All .jpg files have been moved. Total moved: {moved_count}")
