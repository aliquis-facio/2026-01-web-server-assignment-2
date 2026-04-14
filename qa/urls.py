"""
qa 앱 내부 URL 매핑
"""
from django.urls import path
from . import views

urlpatterns = [
    # 질문 목록 URL (루트 경로 '')
    path('', views.question_list, name='question_list'),

    # 질문 상세 URL ('question/<int:pk>/')
    path('question/<int:pk>/', views.question_detail, name='question_detail'),

    # 질문 작성 URL ('ask/')
    path('ask/', views.ask_question, name='ask_question'),
]
