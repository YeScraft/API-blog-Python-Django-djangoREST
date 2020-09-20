from .views import PostList, PostDetail, CategoryList, CategoryDetail
from django.urls import path

app_name = 'app'
urlpatterns = [
    path('', PostList.as_view(), name='post-list'),
    path('<int:pk>', PostDetail.as_view(), name='post-detail'),
    path('categories/', CategoryList.as_view(), name='categories-list'),
    path('categories/<int:pk>', CategoryDetail.as_view(), name='category-detail'),
]
