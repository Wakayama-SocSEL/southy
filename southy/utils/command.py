import codecs
import subprocess


class Command:
    """コマンドを実行するクラス
    """

    def __init__(self, command:str, cwd:str, test:list[str]=None):
        """初期値の設定

        Args:
            command(str): コマンド名
            cwd(str): コマンドを実行するディレクトリのパス
            test(list): コマンドの呼び出しを確認するためのコマンドオプション

        Raises:
            subprocess.CalledProcessError: コマンドに失敗した場合に発生
        """
        self.command = command
        self.cwd = cwd

        if test:
            self.__call__(test)


    def __call__(self, options:list[str]):
        """呼び出し時の設定
        Args:
            command(str): コマンドオプション
        
        Raises:
            subprocess.CalledProcessError: コマンドに失敗した場合に発生

        Returns:
            str: コマンドの標準出力結果
        """
        return codecs.decode(
            subprocess.check_output([self.command] + options, cwd=self.cwd, stderr=subprocess.DEVNULL), errors='ignore'
        )
