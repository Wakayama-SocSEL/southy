import sys
import subprocess
from utils import clone_project
sys.path.append('../')

#プロジェクトのすべてのハッシュ値の取得
def get_all_hash(url: str):
    command = [
        'git',
        'log',
        '--date=short',
        '--no-merges',
        '--pretty=format:%cd %h'
    ]
    try:
        result = subprocess.check_output(command, text=True, cwd='../tmp')
        return result
    except subprocess.CalledProcessError as e:
        return(f"Error executing Git command: {e}")