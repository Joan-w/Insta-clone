from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.views.generic import (
    ListView,
    CreateView,
)

# Create your views here.

class PostListView(ListView):
    template_name = 'insta/home.html'
    queryset = Post.objects.all().filter(created_date__lte=timezone.now())
    context_object_name = 'posts'

class PostCreateView(CreateView):
    template_name = 'insta/create_post.html'
    form_class = PostForm
    queryset = Post.objects.all()
    success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        form.instance.author = self.request.user
        return super().form_valid(form)