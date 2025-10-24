import os
import shutil

# Defining file types (folders go to Doc)(add more for use case)
file_types = {
    "jpg": "Images",
    "png": "Images",
    "pdf": "Documents",
    "wav": "Music",
    "text": "Documents"

}

# downloads folder
downloads =os.path.expanduser("~/Downloads")
# Get the files
files = os.listdir(downloads)
# loop through and gather src 
for file in files:
    src = os.path.join(downloads, file)
    if not os.path.isfile(src):
        continue
    
    try:                          ## split name and extension into variables
        name, extension = file.rsplit(".", 1)
    except ValueError:
        print(f"Skipping {file} (no extension)")
        continue
    
    extension = extension.lower()

    if extension in file_types:
        foldername = file_types[extension]  

        folderpath = os.path.join(downloads, foldername) #Make path

        os.makedirs(folderpath, exist_ok=True)

        dst = os.path.join(folderpath, file)
        
        shutil.move(src, dst) 
        print(f"Moved {name} to {foldername}/")
    else:
        print(f"Unknown file type: {file}")    