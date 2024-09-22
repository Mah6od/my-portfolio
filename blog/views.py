from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from blog.models import Post, Comment
from blog.forms import CommentForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def blog_view(request, **kwargs):
    now = timezone.now()
    posts = Post.objects.filter(status = 1, published_date__lte=now)

    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name = kwargs['cat_name'])

    if kwargs.get('author_username') != None:
            posts = posts.filter(author__username = kwargs['author_username'])
    if kwargs.get('tag_name') != None:
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])

    posts = Paginator(posts, 3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)

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

def blog_category(request, cat_name):
    now = timezone.now()
    posts = Post.objects.filter(status=1, published_date__lte=now, category__name=cat_name)

    # Debugging to ensure correct data is being fetched
    print("Category Post Count:", posts.count())

    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page', 1)
    posts_page = paginator.get_page(page_number)

    context = {'posts': posts_page}
    return render(request, 'website/blog.html', context)

def blog_search(request):
    # print(request.__dict__)
    now = timezone.now()
    posts = Post.objects.filter(status = 1)
    if request.method == 'GET':
         # print(request.GET.get('s'))
         if s := request.GET.get('s'): # Walrus
            posts = posts.filter(content__contains=s)
         
    
    context = {"posts":posts}
    return render(request, 'website/blog.html', context)