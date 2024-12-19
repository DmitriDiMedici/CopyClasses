import os
import shutil
import pandas as pd

#Initial config
EXCEL_FILE = r"" #Complete route tothe excel file, with it's name at the end
MASTER_DIR = r"" #Complete route to the repo, checked out to master branch
DESTINATION_DIR = r"" #Complete route to the destination folder

#Functions
def read_file(excel_file):
    """Reads the excel file with the classes list"""
    df = pd.read_excel(excel_file)
    class_list = df['Class'].tolist()
    return class_list

def create_destination_folder(dest_dir):
    """Creates a subfolder in the destination route where it's going to paste all the classes obtained"""
    backup_dir = os.path.join(dest_dir, "Backup")
    if os.path.exists(backup_dir):
        shutil.rmtree(backup_dir)
    os.makedirs(backup_dir)
    return backup_dir

def copy_classes(master_dir, backup_dir, class_list):
    """Copies the classes (and their meta) obtained from the excel from Master to the Backup folder"""
    for file in class_list:
        class_file = f"{file}.cls"
        meta_file = f"{file}.cls-meta.xml"
        paths = [class_file, meta_file]

        for path in paths:
            source_path = os.path.join(master_dir, path)
            dest_path = os.path.join(backup_dir, path)

            if os.path.exists(source_path):
                shutil.copy(source_path, dest_path)
                print(f"Copied {path} to {dest_path}")
            else:
                print(f"File not found: {source_path}")


#Execution
class_list = read_file(EXCEL_FILE)
backup_dir = create_destination_folder(DESTINATION_DIR)
copy_classes(MASTER_DIR, backup_dir, class_list)
