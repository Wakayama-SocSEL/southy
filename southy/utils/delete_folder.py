import shutil

def delete_folder(path):
    
    """ディレクトリ削除

    引数で指定したpathのディレクトリの強制削除

    Args:
        path (str): 削除したいディレクトリへのpath
    """
    try:
        shutil.rmtree(path)
    except OSError as e:
        print(f"Error deleting folder: {e}")