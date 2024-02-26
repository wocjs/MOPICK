from django.urls import path
from articles import views

urlpatterns = [
    path('articles/', views.article_list),
    path('articles/<int:article_pk>/', views.article_detail),
    path('articles/<int:article_pk>/comments/', views.comment_list),

    # path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    path('articles/current_user/', views.current_user),
    path('comments/<int:comment_pk>/like/', views.like_comment)
    # path('comments/current_comment/', views.current_comment)

]
