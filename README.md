# 書籍管理サイト
## Git準備
1. GitHubでリポジトリ＆developブランチ作成
2. cd /Users/mac/Documents/Django # 作業ディレクトリに移動
3. git clone -b develop https://github.com/oiudon/my-book-management.git # クローン

## Djangoプロジェクトの作成
1. cd /Users/mac/Documents/Django/my-book-management # プロジェクトルートに移動
2. python -m venv venv # 仮想環境を作成する
3. source venv/bin/activate # 仮想環境に入る
4. pip install --upgrade pip # pipのアップグレード
5. pip install "django==3.2.*" # Django 3.2をインストール
6. pip install "djangorestframework==3.14.*" # DRF 3.14をインストール
7. pip install "djangorestframework-simplejwt==5.2.*" # SimpleJWT 5.2をインストール
8. pip install "dj-rest-auth==2.2.*" # dj-rest-auth 2.2をインストール
9. django-admin startproject config . # Djangoプロジェクトを作成

## アプリケーションの作成
1. python manage.py startapp my_book_management # モデル用のmy_book_managementアプリケーションを作成
2. python manage.py startapp apiv1 # APIバックエンド用のapiv1アプリケーションを作成