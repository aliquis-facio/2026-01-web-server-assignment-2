"""
admin 사이트에 모델 등록
"""
from django.contrib import admin
from .models import Question, Answer

# Question 모델 admin 등록
admin.site.register(Question)

# Answer 모델 admin 등록
admin.site.register(Answer)
