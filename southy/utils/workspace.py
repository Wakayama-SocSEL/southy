import atexit
import os
import shutil
from ..constant import path


def create_tmp_dir():
    """一時ディレクトリの作成

    Returns:
        str: 一時ディレクトリのパス
    """
    parent_path = f'{path.REPO_CACHE}/{os.getpid()}'
    os.makedirs(parent_path, exist_ok=True)

    tmp_repo = f'{parent_path}/{len(os.listdir(parent_path))}'
    os.makedirs(tmp_repo, exist_ok=True)
    atexit.register(delete_tmp_dir, parent_path)
    return tmp_repo


def delete_tmp_dir(tmp_repo:str):
    """一時ディレクトリの削除

    Args:
        tmp_repo(str): 一時ディレクトリのパス

    Raises:
        OSError: ディレクトリの削除に失敗した場合に発生
    """
    if os.path.isdir(tmp_repo):
        shutil.rmtree(tmp_repo)
