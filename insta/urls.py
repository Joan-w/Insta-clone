from django.conf.urls import url
from .views import (
    PostListView,
    PostCreateView,
)

app_name = 'insta'

urlpatterns = [
    # Local : http://127.0.0.1:8000/
    url(r'^$', PostListView.as_view(), name='post_list'),
    url(r'^new/', PostCreateView.as_view(), name='post_new'),
]