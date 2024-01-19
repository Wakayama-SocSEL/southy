import sys
import subprocess
sys.path.append('../')


def get_all_hash(path):
    """ハッシュ値の取得
    クローンしてきたプロジェクトの全部のハッシュ値の取得
    Args:
        path (str): クローンしてきたプロジェクトを一時保存している場所への絶対パス

    Raises:
            subprocess.CalledProcessError:  gitコマンドに失敗した場合に発生

    """
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