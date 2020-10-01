from django.urls import path, reverse_lazy
from . import views
from . import models
from ads.views import AdListView, AdDetailView, AdCreateView, AdUpdateView, AdDeleteView

app_name='well'
urlpatterns = [
    path('', views.PostListView.as_view(), name='all'),

    path('post/<int:pk>',
        AdDetailView.as_view(
            model = models.Post,
            template_name = app_name+"/detail.html"),
        name='post_detail'),

    path('post/create',
        AdCreateView.as_view(
            success_url=reverse_lazy(app_name+':all'),
            model = models.Post,
            template_name = app_name+"/form.html",
            fields = ['title', 'text']
         ), name='post_create'),

    path('post/<int:pk>/update',
        AdUpdateView.as_view(
            success_url=reverse_lazy(app_name+':all'),
            model = models.Post,
            fields = ['title', 'text'],
            template_name = app_name+"/form.html"
        ), name='post_update'),

    path('post/<int:pk>/delete',
        AdDeleteView.as_view(
            success_url=reverse_lazy(app_name+':all'),
            model = models.Post,
            template_name = app_name+"/delete.html"
        ), name='post_delete'),

]