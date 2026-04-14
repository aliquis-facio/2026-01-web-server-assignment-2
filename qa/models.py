"""
데이터 구조 정의

Question 모델 필드:
  - title: CharField(max_length=200)
  - content: TextField()
  - author: ForeignKey(User, on_delete=models.CASCADE)
  - created_at: DateTimeField(auto_now_add=True)

Answer 모델 필드:
  - question: ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
  - content: TextField()
  - author: ForeignKey(User, on_delete=models.CASCADE)
  - created_at: DateTimeField(auto_now_add=True)
"""
from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    # 제목, 최대 200자
    title = models.CharField(max_length=200)

    # 내용
    content = models.TextField()

    # 작성자, User와 N:1 관계, 사용자가 삭제되면 질문도 삭제
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # 작성일, 생성 시각 자동 저장
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Answer(models.Model):
    # 질문 참조, 질문 삭제 시 답변도 삭제
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')

    # 답변 내용
    content = models.TextField()

    # 작성자 (ForeignKey → User, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # 작성일 (DateTimeField, auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Answer to {self.question.title} by {self.author.username}"
