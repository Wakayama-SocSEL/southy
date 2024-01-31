import subprocess
import os
import shutil

def clone_project(url, ROOT):
    
    """
    入力したurlのプロジェクトをクローンするメソッド,
    root直下のtmpにプロジェクトがクローンされる

    Args:
        url (str): プロジェクトのurl

    Raises:
            subprocess.CalledProcessError:  git cloneのコマンドに失敗した場合に発生
    """
    
    destination_path = f'{ROOT}/tmp/origin'
    command = ['git', 'clone', url, destination_path]

    try:
        if os.path.exists(destination_path):
            shutil.rmtree(destination_path)
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error cloning repository: {e}")

