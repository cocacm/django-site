from django.views.generic import TemplateView
from django.urls import path
from .views import blog_list

app_name = 'blog'
urlpatterns = [
    path('', TemplateView.as_view(template_name='blog/index.html'), name='index'),
    path('', blog_list, name='get_posts')
]
