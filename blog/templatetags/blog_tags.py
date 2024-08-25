from django import template
from blog.models import Post, Category, Comment
from django.utils.text import slugify
import re

register = template.Library()

@register.simple_tag(name='totalposts')
def function():
    posts = Post.objects.filter(status=1).count()
    return posts

@register.simple_tag(name='posts')
def function():
    posts = Post.objects.filter(status=1).count()
    return posts

@register.simple_tag(name='comments_count')
def function(pid):
    post = Post.objects.get(pk=pid)
    return Comment.objects.filter(post=post.id, approved=True).count()

@register.filter
def snippet(value):
    return value[:100]