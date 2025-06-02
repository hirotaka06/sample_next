#!/usr/bin/env python
"""
テスト用ユーザーアカウント作成スクリプト
このスクリプトを実行すると、ログインテスト用のユーザーアカウントが作成されます。
認証情報は環境変数から読み込まれるため、セキュリティが向上します。
"""
import os

import django
from django.contrib.auth.models import User
from dotenv import load_dotenv

# .envファイルから環境変数を読み込み
load_dotenv()

# Djangoの設定を読み込み
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sample_next.settings')
django.setup()


def create_test_user():
    """
    テスト用ユーザーを作成する関数
    環境変数から認証情報を読み込みます
    """
    # 環境変数からユーザー情報を読み込み（デフォルト値付き）
    username = os.getenv('TEST_USER_USERNAME', 'testuser')
    password = os.getenv('TEST_USER_PASSWORD', 'testpass123')
    email = os.getenv('TEST_USER_EMAIL', 'test@example.com')

    # 既存のユーザーをチェック
    if User.objects.filter(username=username).exists():
        print(f'ユーザー "{username}" は既に存在しています。')
        return

    # テストユーザーを作成
    user = User.objects.create_user(
        username=username,
        email=email,
        password=password
    )

    print(f'テストユーザーが作成されました！')
    print(f'ユーザー名: {username}')
    print(f'メールアドレス: {email}')
    print(f'このユーザーでログインテストができます。')
    print('注意: パスワードは環境変数で管理されています。')


def create_admin_user():
    """
    管理者ユーザーを作成する関数
    環境変数から認証情報を読み込みます
    """
    # 環境変数から管理者情報を読み込み（デフォルト値付き）
    username = os.getenv('ADMIN_USERNAME', 'admin')
    password = os.getenv('ADMIN_PASSWORD', 'admin123')
    email = os.getenv('ADMIN_EMAIL', 'admin@example.com')

    # 既存の管理者をチェック
    if User.objects.filter(username=username).exists():
        print(f'管理者ユーザー "{username}" は既に存在しています。')
        return

    # 管理者ユーザーを作成
    user = User.objects.create_superuser(
        username=username,
        email=email,
        password=password
    )

    print(f'管理者ユーザーが作成されました！')
    print(f'ユーザー名: {username}')
    print(f'メールアドレス: {email}')
    print(f'管理画面(/admin/)にアクセスできます。')
    print('注意: パスワードは環境変数で管理されています。')


def show_env_instructions():
    """
    環境変数の設定方法を説明する関数
    """
    print('=== 環境変数の設定について ===')
    print()
    print('セキュリティのため、以下の環境変数を設定することをお勧めします：')
    print()
    print('# テストユーザー用')
    print('TEST_USER_USERNAME=your_test_username')
    print('TEST_USER_PASSWORD=your_secure_test_password')
    print('TEST_USER_EMAIL=test@example.com')
    print()
    print('# 管理者ユーザー用')
    print('ADMIN_USERNAME=your_admin_username')
    print('ADMIN_PASSWORD=your_secure_admin_password')
    print('ADMIN_EMAIL=admin@example.com')
    print()
    print('これらの値は .env ファイルまたはシステムの環境変数で設定できます。')
    print()


if __name__ == '__main__':
    print('=== セキュアなユーザーアカウント作成スクリプト ===')
    print()

    # 環境変数の説明を表示
    show_env_instructions()

    # テストユーザーを作成
    create_test_user()
    print()

    # 管理者ユーザーを作成
    create_admin_user()
    print()

    print('=== 作成完了 ===')
    print('Djangoサーバーを起動して、ログイン機能をテストしてください。')
    print('コマンド: python manage.py runserver')
    print()
    print('セキュリティのため、本番環境では必ず強力なパスワードを設定してください。')
