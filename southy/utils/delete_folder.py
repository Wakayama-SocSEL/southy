import shutil

#指定pathのフォルダの削除
def delete_folder(path):
    try:
        shutil.rmtree(path)
    except OSError as e:
        print(f"Error deleting folder: {e}")