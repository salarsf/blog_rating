from django.urls import path
from .views import (
    PostList,
    PostDetail,
)

urlpatterns = [
    path('v1.0/posts/', PostList.as_view(), name='post_list'),
    path('v1.0/posts/<int:pk>/', PostDetail.as_view(), name='post_detail'),
]
