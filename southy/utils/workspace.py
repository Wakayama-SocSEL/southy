import atexit
import os
import shutil

from .. import constant


def create_tmp_dir():
    """一時ディレクトリの作成

    Returns:
        str: 一時ディレクトリのパス
    """
    parent_path = f'{constant.path.TMP}/{os.getpid()}'
    os.makedirs(parent_path, exist_ok=True)

    path = f'{parent_path}/{len(os.listdir(parent_path))}'
    os.makedirs(path, exist_ok=True)
    atexit.register(delete_tmp_dir, parent_path)
    return path


def delete_tmp_dir(path:str):
    """一時ディレクトリの削除

    Args:
        path(str): 一時ディレクトリのパス

    Raises:
        OSError: ディレクトリの削除に失敗した場合に発生
    """
    if os.path.isdir(path):
        shutil.rmtree(path)
