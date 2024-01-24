import subprocess
from constant import path
from datetime import datetime

class GetHash:
    """指定した日付以降のハッシュ値を取得するクラス
    """

    def __init__(self, begin_date='2000-01-01'):
        """初期値設定

        Args:
            begin_date (str):観測を開始する日にち.2024-1-1など.デフォルトは2000-1-1で定義された値.
        """
        self.begin_date = begin_date
    
    def __get_all_hash(self):
        """ クローンしてきたプロジェクトの全部のハッシュ値の取得

        Args:
            path (str): クローンしてきたプロジェクトを一時保存している場所への絶対パス

        Raises:
            subprocess.CalledProcessError:  gitコマンドに失敗した場合に発生

        Returns:
        str: '日付' 'ハッシュ値'の形で返す
        """
        command = [
            'git',
            'log',
            '--date=short',
            '--no-merges',
            '--pretty=format:%cd %H'
        ]
        try:
            result = subprocess.check_output(command, text=True, cwd=path.ORIGIN)
            return result
        except subprocess.CalledProcessError as e:
            return(f"Error executing Git command: {e}")
        
    def get_hash(self):
        """指定日以降のhash値の取得

        Args:
            begin_date (str): 観測を開始する日にち.
            date_hash(str): get_all_hashメソッドの受け取り用
        """
        hash_list = []
        date_hash = self.__get_all_hash()

        for line in  date_hash.split('\n'):
            if line:
                date, hash_val = line.split(' ')

                # 日付をdatetimeオブジェクトに変換
                date_obj = datetime.strptime(date, '%Y-%m-%d')
                begin_date_obj = datetime.strptime(self.begin_date, '%Y-%m-%d')

                if date_obj > begin_date_obj:
                    hash_list.append(hash_val)

        return hash_list
    
