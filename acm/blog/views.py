from django.shortcuts import render
from .models import Blog


# Create your views here.
def blog_list(request, template_name='blog/index.html'):
    context = dict()

    blog_posts = Blog.objects.all()
    context['blog_posts'] = blog_posts

    return render(request, template_name, context=context)
