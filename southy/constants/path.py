"""使用PATH

使用するPATHの一覧

    Args:
        ROOT (str): 現在ディレクトリから算出したrootの絶対パス
        TMP  (str): 一時保存用ディレクトリへの絶対パス
"""

import os
import sys
sys.path.append('../')


ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
TMP = f'{ROOT}/tmp'
