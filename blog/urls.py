from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    # urls , view, name
    path('', blog_view, name= 'index'),
]