from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render


# ログインが必要なページにデコレータを追加
@login_required
def home(request):
    return render(request, 'home.html')


@login_required
def about(request):
    return render(request, 'about.html')


def user_login(request):
    """
    ユーザーログイン機能
    - GETリクエスト: ログインページを表示
    - POSTリクエスト: ログイン処理を実行
    """
    if request.method == 'POST':
        # フォームからユーザー名とパスワードを取得
        username = request.POST['username']
        password = request.POST['password']

        # ユーザー認証を実行
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # 認証成功: ユーザーをログインさせてホームページにリダイレクト
            login(request, user)
            messages.success(request, 'ログインに成功しました。')
            # ログイン後のリダイレクト先を取得（デフォルトは/home/）
            next_url = request.GET.get('next', '/home/')
            return redirect(next_url)
        else:
            # 認証失敗: エラーメッセージを表示
            error_message = 'ユーザー名またはパスワードが正しくありません。'
            return render(request, 'login.html', {
                'error_message': error_message,
                'username': username  # 入力されたユーザー名を保持
            })

    # GETリクエストの場合はログインページを表示
    return render(request, 'login.html')


def user_logout(request):
    """
    ユーザーログアウト機能
    ログアウト後はログインページにリダイレクト
    """
    logout(request)
    messages.info(request, 'ログアウトしました。')
    return redirect('login')
