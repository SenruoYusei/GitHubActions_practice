# GitHubActions_practice
This is the repo to practice using GitHub Actions.
他の人が同じ状況を再現するための手順
他の人が同じ状況を再現するためには、以下のコマンドを実行して必要なファイルをダウンロードし、環境をセットアップします。

リポジトリをクローン：
```
git clone <repository_url>
cd <repository_directory>
```
Python 環境をセットアップ：
```
brew install pyenv
pip install sphinx
```
Sphinx プロジェクトの初期化（必要な場合）：
```
cd docs/source
sphinx-quickstart
```
ドキュメントのビルド：
```
cd docs
make html
```