from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    # urls , view, name
    path('', blog_view, name= 'index'),
    path('<int:pid>/' ,blog_single, name='single'),
    path('category/<str:cat_name>/' ,blog_view, name='category'),
    path('search/' , blog_search, name='search'),
]