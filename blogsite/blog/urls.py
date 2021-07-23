from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('keyword', views.KeywordList.as_view(), name='keyword_list'),
    path('keyword/<str:keyword>/', views.keyword_posts_view, name='keyword')
]
