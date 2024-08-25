from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from blog.models import Post, Comment
from blog.forms import CommentForm
from django.contrib import messages

# Create your views here.
def blog_view(request, **kwargs):
    now = timezone.now()
    posts = Post.objects.filter(status = 1, published_date__lte=now)

    context = {"posts":posts}
    return render(request, 'website/blog.html', context)

def blog_single(request, pid):
    form = CommentForm()
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Submitted Successfully!')
            messages.add_message(request, messages.SUCCESS, 'Submitted Successfully!')
        else:
            messages.add_message(request, messages.ERROR, 'Submitted Successfully!')

    now = timezone.now()
    posts = Post.objects.filter(status = 1, published_date__lte=now)
    post = get_object_or_404(posts, pk=pid)
    comments = Comment.objects.filter(post=post.id, approved=True)
    post.counted_views += 1
    post.save()

    context = {
        'post': post,
        'comments': comments,
        'form': form,
        #'prev_post': prev_post,
        #'next_post': next_post,
    }
    return render(request, 'blog-single.html', context)