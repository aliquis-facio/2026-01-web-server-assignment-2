"""
앱 설정 클래스
"""
from django.apps import AppConfig

class QaConfig(AppConfig):
    # 기본 PK 타입 설정
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'qa'
