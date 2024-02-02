import subprocess
import os
import shutil

def clone_project(root, url):
    
    """
    入力したurlのプロジェクトをクローンするメソッド\n
    root直下のtmpにプロジェクトがクローンされる

    Args:
        root(str): プロジェクトのrootへのpath
        url (str): クローンしたいプロジェクトへのurl

    Raises:
            subprocess.CalledProcessError:  git cloneのコマンドに失敗した場合に発生
    """
    
    destination_path = f'{root}/tmp/origin'
    command = ['git', 'clone', url, destination_path]

    try:
        if os.path.exists(destination_path):
            shutil.rmtree(destination_path)
        os.makedirs(destination_path, exist_ok=True)
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error cloning repository: {e}")

