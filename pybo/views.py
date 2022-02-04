from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question, Answer, Category
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator
from django.db.models import Q, Count
# from django.http import HttpResponse

# Create your views here.

def pybo(request, category_name='carbon'):
    """
    pybo 목록 출력
    """
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    so = request.GET.get('so', 'recent')  # 정렬기준

    category_list = Category.objects.all()
    category = get_object_or_404(Category, name=category_name)
    question_list = Question.objects.filter(category=category)

    # 정렬
    if so == 'recommend':
        question_list = Question.objects.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular':
        question_list = Question.objects.annotate(num_answer=Count('answer')).order_by('-num_answer', '-create_date')
    else:  # recent
        question_list = Question.objects.order_by('-create_date')

    # 조회, 검색
    # question_list = Question.objects.order_by('-create_date')

    # 페이징처리
    paginator = Paginator(question_list, 5)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj, 'page': page, 'so': so,
               'category_list': category_list, 'category': category}
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    """
    pybo 내용 출력
    """
    question = get_object_or_404(Question, pk=question_id) # pk = primary key
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

def question_create(request, category_name):
    """
    pybo 질문등록
    """
    category = Category.objects.get(name=category_name)

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.category = category
            question.save()
            return redirect(category)
    else: # request.method == 'GET'
        form = QuestionForm()
    context = {'form': form, 'category':category }
    return render(request, 'pybo/question_form.html', context)

def answer_create(request, question_id):
    """
    pybo 답변등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)

def vote_question(request, question_id):
    """
    pybo 질문추천등록
    """
    question = get_object_or_404(Question, pk=question_id)
    # if request.user == question.author:
    #     messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    # else:
    question.voter.add(request.user)
    return redirect('pybo:detail', question_id=question.id)