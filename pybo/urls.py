from django.urls import path

from . import views

app_name = 'pybo'

urlpatterns = [
    # path('', views.index),
    # path('<int:question_id>/', views.detail),
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    # 상세 화면에서 <질문답변> 버튼을 눌렀을 때 작동할 form 엘리먼트의 /pybo/answer/create/2/에 대한 URL 매핑을 추가한 것이
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
]