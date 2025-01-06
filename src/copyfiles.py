import os
import shutil

def copy_files(source_folder, destination_folder):
    # delete all the contents of the destination folder
    if os.path.exists(destination_folder):
        shutil.rmtree(destination_folder)
    # create clean copy of the destination folder
    os.mkdir(destination_folder)
    # call the recursive copier function to copy the source directory tree across
    copier(source_folder, destination_folder)


def copier(source_folder, destination_folder):
    source_contents = os.listdir(source_folder)
    for obj in source_contents:
        obj_src_path = os.path.join(source_folder, obj)
        if os.path.isfile(obj_src_path):
            shutil.copy(obj_src_path, destination_folder)
            print(f"copied {obj_src_path} to {destination_folder}")
        else:
            obj_dst_path = os.path.join(destination_folder, obj)
            os.mkdir(obj_dst_path)
            if os.path.exists(obj_dst_path):
                print(f"created new folder {obj_dst_path}")
            if len(os.listdir(obj_src_path)) > 0:
                copier(obj_src_path, obj_dst_path)