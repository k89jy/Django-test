<<<<<<< HEAD
from django.views.generic import ListView, DetailView
from .models import Post
# Create your views here.

class PostList(ListView):
    model = Post
    ordering = '-pk'


class PostDetail(DetailView):
    model = Post
=======
from django.shortcuts import render
from .models import Post
# Create your views here.

def index(request):
    posts = Post.objects.all().order_by('-pk')

    return render(
        request,
        'blog/index.html',
        {
            'posts' : posts,
        },
    )
>>>>>>> origin/changrae
