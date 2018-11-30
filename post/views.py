from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from utils.decorators import login_required
from .forms import PostForm
from .models import Post

@login_required
def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'count': Post.objects.count(),
    }
    return render(request, 'post/post_list.html', context)

@login_required
def post_detail(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    context = {
        'post': post,
        'count': Post.objects.count(),
    }
    return render(request, 'post/post_detail.html', context)


@login_required
def post_create(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            # author필드를 채우기 위해 인스턴스만 생성
            post = post_form.save(commit=False)
            # author필드를 채운 후 DB에 저장
            post.author = request.user
            post.save()

            # 성공 알림을 messages에 추가 후 post_list뷰로 이동
#            messages.success(request, '일기가 등록되었습니다')
            return redirect('post:post_list')
    else:
        post_form = PostForm()

    context = {
        'post_form': post_form,
        'count': Post.objects.count(),
    }
    return render(request, 'post/post_create.html', context)
