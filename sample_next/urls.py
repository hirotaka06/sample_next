"""
URL configuration for sample_next project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path

from web_app import views


def root_redirect(request):
    """
    ルートパス（/）にアクセスした際の処理
    認証済みユーザーはホームページへ、未認証ユーザーはログインページへリダイレクト
    """
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return redirect('login')


urlpatterns = [
    # 管理画面
    path('admin/', admin.site.urls),

    # ルートパス - 自動リダイレクト機能
    path('', root_redirect, name='root'),

    # ログイン関連
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    # メインページ（ログイン必須）
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
]
