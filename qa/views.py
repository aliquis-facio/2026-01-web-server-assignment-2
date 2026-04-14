"""
실제 요청 처리
"""
from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer
from django.contrib.auth.decorators import login_required


def question_list(request):
    """질문 목록 뷰: 최신순으로 정렬된 모든 질문을 표시"""
    # DB에서 Question 전체 조회
    # created_at 내림차순 정렬
    questions = Question.objects.order_by('-created_at')

    # questions를 템플릿에 전달
    # question_list.html 렌더링
    return render(request, 'qa/question_list.html', {'questions': questions})


def question_detail(request, pk):
    """질문 상세 뷰: 질문 내용과 답변 목록을 표시하고, 답변 작성 처리"""
    # pk로 Question을 가져오세요 (없으면 404)
    question = get_object_or_404(Question, pk=pk)

    # POST
    if request.method == 'POST':
        # 같은 질문 조회
        # content 추출
        content = request.POST.get('content')
        # 로그인 여부 확인
        if content and request.user.is_authenticated:
            # Answer 객체 생성
            Answer.objects.create(
                question=question,
                content=content,
                author=request.user,
            )
            # 상세 페이지로 redirect
            return redirect('question_detail', pk=pk)

    # GET
    # 상세 페이지 렌더링
    # 템플릿에서 question.answers.all로 답변 목록 표시
    return render(request, 'qa/question_detail.html', {'question': question})


@login_required
def ask_question(request):
    """질문 작성 뷰: 로그인한 사용자만 질문을 작성할 수 있음"""
    # POST
    if request.method == 'POST':
        # 제목과 내용 추출
        title = request.POST.get('title')
        content = request.POST.get('content')
        # 둘 다 존재하면
        if title and content:
            # Question 객체 생성
            Question.objects.create(
                title=title,
                content=content,
                author=request.user,
            )
            # 질문 목록 페이지로 redirect
            return redirect('question_list')

    # GET
    # 질문 작성 폼 표시
    return render(request, 'qa/ask_question.html')
