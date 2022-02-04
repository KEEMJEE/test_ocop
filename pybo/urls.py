from django.urls import path

from . import views

app_name = 'pybo'

urlpatterns = [
    path('', views.pybo, name='pybo'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('question/create/', views.question_create, name = 'question_create'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    # vote_views.py
    path('vote/question/<int:question_id>/', views.vote_question, name='vote_question'),

    #category
    path('question/list/', views.pybo, name='pybo'),
    path('question/list/<str:category_name>/', views.pybo, name='pybo'),
    path('question/detail/<int:question_id>/', views.detail, name='detail'),
    path('question/create/<str:category_name>/', views.question_create, name='question_create_category'),
]
