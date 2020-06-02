from django.conf.urls import url
from .views import (
    PostListView,
    PostCreateView,
    PostDetailView,
    PostUpdateView,
    PostDeleteView
)

app_name = 'insta'

urlpatterns = [
    # Local : http://127.0.0.1:8000/
    url(r'^$', PostListView.as_view(), name='post-list'),
    url(r'^create/', PostCreateView.as_view(), name='post-create'),
    url(r'^post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    url(r'^post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    url(r'^post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
]