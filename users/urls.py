from django.conf import settings

from django.urls import path
from .views import BlogListView, BlogListbyAuthorView, BlogDetailView, BloggerListView, BlogCommentCreate
from .views import index

app_name = 'users'

urlpatterns = [
    path('', index, name='/'),
    path('users/blogs', BlogListView.as_view(), 'users/blogs'),
    path('users/blogs-by-author/<int:pk>', BlogListbyAuthorView.as_view(), name='blogs-by-author'),
    path('users/blog-detail/<int:pk>', BlogDetailView.as_view(), name='blog-detail'),
    path('users/blogauthor-list/bloggers', BloggerListView.as_view(), name='bloggers'),
    path('users/blogcomment-form/<int:pk>', BlogCommentCreate.as_view(), name='blog-comment'),
]
