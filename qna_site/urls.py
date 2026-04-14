"""
최상위 URL 라우팅
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    # 관리자 페이지
    path('admin/', admin.site.urls),

    # qa 앱으로 위임 -> urls.py를 include
    path('', include('qa.urls')),

    # 로그인 뷰 추가
    path('login/', auth_views.LoginView.as_view(template_name='qa/login.html'), name='login'),

    # 로그아웃 뷰 추가
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
