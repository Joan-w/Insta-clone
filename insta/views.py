from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.urls import reverse
from .models import Post
from .forms import PostForm
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
)
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

class PostListView(ListView):
    template_name = 'insta/home.html'
    queryset = Post.objects.all().filter(created_date__lte=timezone.now()).order_by('-created_date')
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

class PostDetailView(DetailView):
    template_name = 'insta/details.html'
    queryset = Post.objects.all().filter(created_date__lte=timezone.now())
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Post, id=id_)

def register(request):
    form = UserCreationForm()
    return render(request, 'users/register.html', {"form":form})