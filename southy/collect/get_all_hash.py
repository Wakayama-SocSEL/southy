import sys
import subprocess
from utils import clone_project
sys.path.append('../')

#プロジェクトのすべてのハッシュ値の取得
def get_all_hash(url: str):
    #クローン
    clone_project(url)
    
    #全ハッシュ値の取得
    command = [
        'git',
        'log',
        '--date=short',
        '--no-merges',
        '--pretty=format:%cd %h'
    ]
    try:
        result = subprocess.check_output(command, text=True)
        return result
    except subprocess.CalledProcessError as e:
        return(f"Error executing Git command: {e}")