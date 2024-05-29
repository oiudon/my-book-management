# 書籍管理サイト
## Git準備
1. GitHubでリポジトリ＆developブランチ作成
2. cd /Users/mac/Documents/Django # 作業ディレクトリに移動
3. git clone -b develop https://github.com/oiudon/my-book-management.git # クローン

## APIバックエンド構築手順（by DRF）
1. プロジェクトを新規作成して、DjangoおよびDjangoパッケージをインストール
2. my_book_managementアプリケーションを作成してモデルを作成
3. 管理サイトの設定
4. apiv1アプリケーションを作成してREST APIバックエンドを作成
5. ルーティングの設定

## SPAフロントエンドの構築手順（by create-vue）
1. npmをインストール
2. create-vueでVueプロジェクトをDjangoプロジェクト内に新規作成
3. 各種Nodeパッケージをインストール
4. Vue、JavaScriptファイルを実装

## Django環境構築
1. cd /Users/mac/Documents/Django/my-book-management # プロジェクトルートに移動
2. python -m venv venv # 仮想環境を作成する
3. source venv/bin/activate # 仮想環境に入る
4. pip install --upgrade pip # pipのアップグレード
5. pip install "django==3.2.*" # Django 3.2をインストール
6. pip install "djangorestframework==3.14.*" # DRF 3.14をインストール
7. pip install "djangorestframework-simplejwt==5.2.*" # SimpleJWT 5.2をインストール
8. pip install "dj-rest-auth==2.2.*" # dj-rest-auth 2.2をインストール
9. pip install "django-cors-headers==3.13.*" # django-cors-headersをインストール
10. pip install psycopg2-binary # psycopg2-binaryをインストール
11. VSCodeでflake8、black、isort、mypyの拡張機能追加 # 参照：https://qiita.com/siruku6/items/6a8412c41616b558df66　https://itc-engineering-blog.netlify.app/blogs/vscode-extensions-black-flake8　https://nujust.hatenablog.com/entry/2022/07/24/114715

## Djangoプロジェクト〜アプリケーションの作成
1. django-admin startproject config . # Djangoプロジェクトを作成
2. python manage.py startapp my_book_management # モデル用のmy_book_managementアプリケーションを作成
3. python manage.py startapp apiv1 # APIバックエンド用のapiv1アプリケーションを作成

## データベース設定（PostgreSQL）
1. brew services start postgresql # PostgreSQL起動
2. createdb mybook-db # データベース作成

