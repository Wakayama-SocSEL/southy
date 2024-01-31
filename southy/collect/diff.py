import subprocess
import os
import shutil
from collect import GetHash
from utils import clone_project
from constant import path

def main(url,ROOT, begin_date = None):
    """main関数.

    Args:
        url (_type_): _description_
        begin_date (_type_): _description_
    """
    clone_project(url, ROOT)
    get_diff(ROOT, begin_date)

# def __checkout_project_at_hash(hash_val, from_path):
#     """ 指定されたハッシュ値でプロジェクトを復元する

#     Args:
#         hash_val (str): プロジェクトを復元するハッシュ値
#         project_path (str): プロジェクトのディレクトリへのパス
#     """
#     command = ['git', 'checkout', hash_val]
#     try:
#         subprocess.run(command, check=True, cwd=from_path, text=False)
#     except subprocess.CalledProcessError as e:
#         print(f"Error checking out to {hash_val}: {e}")


def get_diff(root, begin_date = None):
    """開始日以降のdiffをとる

    Args:
        begin_date (str): 測定の開始日
        TMP: 一時保存用ディレクトリ

    """
    hash_list = []
    save_path = f'{root}/tmp/out'

    gh = GetHash(begin_date)
    hash_list = gh.get_hash(root)

    for i in range(len(hash_list) - 1):
        # 'from' と 'to' 間の差分を計算
        diff_command = ['git', 'diff', hash_list[i], hash_list[i+1]]
        diff_result = subprocess.run(diff_command, capture_output=True, text=True, errors='replace')
        
        # 出力ファイルのパス
        output_file_path = f'{save_path}/{hash_list[i]}_{hash_list[i+1]}_output.txt'

        # ファイルに結果を書き込む
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(diff_result.stdout)

        print(f"Diff has been saved to {output_file_path}")


if __name__ == '__main__':
    main('https://github.com/Wakayama-SocSEL/southy.git',path.ROOT)