from ..utils import Command, workspace

class LocalRepository:
    """ローカルリポジトリを操作するクラス
    """

    def __init__(self, url:str=None, path:str=None):
        """初期値の設定

        Args:
            url(str): リポジトリのURL
            path(str): ローカルディレクトリのパス

        Raises:
            subprocess.CalledProcessError: gitコマンドに失敗した場合に発生
        """
        if not path:
            path = workspace.create_tmp_dir()

        self.git = Command('git', path, test=['--version'])

        if url:
            self.git(['clone', url, '.'])


    def findall_commit_hashes(self, begin_date:str='2000-01-01'):
        """開始日以降のコミットハッシュ値の取得
        
        Args:
            begin_date(str): 観測を開始する日にち. デフォルトは2000-01-01

        Raises:
            subprocess.CalledProcessError: gitコマンドに失敗した場合に発生

        Returns:
            list: コミットハッシュ値のリスト
        """
        return self.git(['log', '--after', begin_date, '--no-merges', '--pretty=format:%H']).split('\n')


    def findall_commit_diffs(self, begin_date:str='2000-01-01'):
        """開始日以降のコミット差分の取得

        Args:
            begin_date(str): 観測を開始する日にち. デフォルトは2000-01-01

        Raises:
            subprocess.CalledProcessError: gitコマンドに失敗した場合に発生

        Returns:
            list: コミット差分のリスト
        """
        commit_diffs = []
        for commit_hash in self.findall_commit_hashes(begin_date)[:-1]:
            commit_diffs.append(self.git(['diff', f'{commit_hash}^..{commit_hash}']))

        return commit_diffs
