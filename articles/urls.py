from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path("", views.main, name="main"),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/update/', views.update, name='update'),
    path("<int:pk>/delete/", views.delete, name="delete"),
    path('<int:pk>/comments/', views.comment_create, name='comment_create'),
    path('comments/<int:comment_pk>/comment_delete/', views.comment_delete, name='comment_delete'),
    path('<int:pk>/like/', views.like, name='like'),
    # path("search/", views.SearchView.as_view(), name="search"),
    path("search/", views.search, name="search"),
]
