from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

def create100(requests):
    me = User.objects.get(username='admin')
    for i in range(100):
        p=Post.objects.create(author=me, title='Sample title', text='Test')
        p.publish()

    return HttpResponse('done')
def post_list(request):
    ls= Post.objects.all()
    content={"posts":ls}
    return render(request, 'blog/post_list.html',content)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

# Create your views here.
