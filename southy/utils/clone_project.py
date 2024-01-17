import subprocess
import sys
sys.path.append('../')

#リポジトリのクローン
def clone_project(url: str):
    destination_path = f'{sys.path[-1]}/tmp'
    command = ['git', 'clone', url, destination_path]

    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error cloning repository: {e}")