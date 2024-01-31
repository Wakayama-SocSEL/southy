import subprocess
import os
import shutil
from collect import GetHash
from utils import clone_project

def main(url, begin_date, ROOT):
    """main関数.

    Args:
        url (_type_): _description_
        begin_date (_type_): _description_
    """
    clone_project(url, ROOT)
    get_diff(begin_date, f'{ROOT}/tmp')

def __checkout_project_at_hash(hash_val):
    """ 指定されたハッシュ値でプロジェクトを復元する

    Args:
        hash_val (str): プロジェクトを復元するハッシュ値
        project_path (str): プロジェクトのディレクトリへのパス
    """
    command = ['git', 'checkout', hash_val]
    try:
        subprocess.run(command, check=True, cwd=path.ORIGIN)
        print(f"Checked out to {hash_val}")
    except subprocess.CalledProcessError as e:
        print(f"Error checking out to {hash_val}: {e}")


def get_diff(begin_date, TMP):
    """開始日以降のdiffをとる

    Args:
        begin_date (str): 測定の開始日
        TMP: 一時保存用ディレクトリ

    """
    hash_list = []
    from_path = f'{TMP}/from'
    to_path = f'{TMP}/to'

    gh = GetHash(begin_date)
    hash_list = gh.get_hash()

    for i, hash in enumerate(hash_list):
        if i == 0:
            __checkout_project_at_hash(hash)
            if not os.path.exists(from_path):
                shutil.copytree(path.ORIGIN, from_path)
            continue

        __checkout_project_at_hash(hash)
        if os.path.exists(to_path):
            shutil.rmtree(to_path)
        shutil.copytree(path.ORIGIN, to_path)

        # 'from' と 'to' 間の差分を計算
        diff_command = ['git', 'diff', '--name-only', f'{from_path}', f'{to_path}']
        diff_result = subprocess.check_output(diff_command, text=True)
        print(f"Diff for {hash_list[i-1]} to {hash}:\n{diff_result}")

        # 次の比較のために 'to' を 'from' に移動
        shutil.rmtree(from_path)
        shutil.move(to_path, from_path)


if __name__ == '__main__':
    main('https://github.com/tomoya0318/tomoya0318.git', '2024-1-1')