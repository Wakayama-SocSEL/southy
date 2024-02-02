import subprocess
import os
from collect import GetHash
from utils import clone_project

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


def get_diff(root, url = None, begin_date = None):
    """開始日以降のdiffをとる

    Args:
        root(str): プロジェクトのrootへのpath
        url(str): diffをとりたいプロジェクトへのurl.引数がない場合,"./tmp/origin"にあるプロジェクトに対してdiffを取る
        begin_date (str): 測定の開始日.引数がない場合,2000-1-1になる

    """
    hash_list = []
    save_path = f'{root}/tmp/out'
    os.makedirs(save_path, exist_ok=True)

    if url != None:
        clone_project(url, root)
    #ハッシュ値の取得
    gh = GetHash(begin_date)
    hash_list = gh.get_hash(root)

    for i in range(len(hash_list) - 1):
        # hash値間の差分を取得
        diff_command = ['git', 'diff', hash_list[i], hash_list[i+1]]
        diff_result = subprocess.run(diff_command, capture_output=True, text=True, errors='replace')
        
        # 出力ファイルのパス
        output_file_path = f'{save_path}/{hash_list[i]}_{hash_list[i+1]}_output.txt'

        # ファイルに結果を書き込む
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(diff_result.stdout)

        print(f"Diff has been saved to {output_file_path}")
