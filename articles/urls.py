from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path("", views.main, name="main"),
    # 카테고리 (좌우스크롤) 페이지
    path("index/", views.index, name="index"),
    # 글자 로딩 페이지
    path("loading/", views.loading, name="loading"),
    # 티켓 출력 페이지
    path("ticket_machine/", views.ticket_machine, name="ticket_machine"),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/update/', views.update, name='update'),
    path("<int:pk>/delete/", views.delete, name="delete"),
    path('<int:pk>/comments/', views.comment_create, name='comment_create'),
    path('comments/<int:comment_pk>/comment_delete/', views.comment_delete, name='comment_delete'),
    path('<int:pk>/like/', views.like, name='like'),
    # path("search/", views.SearchView.as_view(), name="search"),
    path("search/", views.search, name="search"),
    path("about/", views.about, name="about"),
]
