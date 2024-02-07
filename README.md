## このライブラリのインストール方法
まずdistディレクトリから`southy-0.1.0.tar.gz`か`southy-0.1.0-py3-none-any.whl`をダウンロードし，以下のコマンドを実行
```
pip install {southy-0.1.0.tar.gzへのpath}
```

## 使用方法
ソースコード内に以下を記述
```
from {モジュール名} import {関数名}
```
これで，指定した関数を使用可能
関数は[モジュール一覧](https://wakayama-socsel.github.io/southy/)を参照

### 使用例
クラス`LocalRepository`をインポートし，コミット差分を取得
```python
from southy import LocalRepository

repo = LocalRepository('https://github.com/Wakayama-SocSEL/southy.git')
diffs = repo.findall_commit_diffs()
print(diffs[0])
```
