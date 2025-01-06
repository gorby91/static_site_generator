import os
import shutil

def copy_files(source_folder, destination_folder):
    # delete all the contents of the destination (public) directory
    if os.path.exists(destination_folder):
        pre_deletion_folders = list(map(lambda file: f"{destination_folder}/{file}", os.listdir(destination_folder)))
        print(f"{destination_folder} contains {pre_deletion_folders}")
        shutil.rmtree(destination_folder)
        if not os.path.exists(destination_folder):
            print(f"{destination_folder} deleted")
    os.mkdir(destination_folder)
    if os.path.exists(destination_folder):
        print(f"Clean copy of {destination_folder} restored")
    copier(source_folder, destination_folder)
   
    # copy all files, subdirectories, nested files, etc
    # log the path of each file coipied so you can see what is happening

def copier(source_folder, destination_folder):
    source_contents = os.listdir(source_folder)
    source_contents_paths = []
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