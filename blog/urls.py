from django.urls import path
from .views import PostListView,PostDetailView,PostCreateView , PostUpdateView , PostDeleteView
from . import views

urlpatterns = [
    
    path('',views.PostListView.as_view(), name = 'blog-home'),
    path('post/new/',views.PostCreateView.as_view(), name = 'post-create'),
    path('post/<int:pk>/',views.PostDetailView.as_view(), name = 'post-detail'),
    path('post/<int:pk>/update/',views.PostUpdateView.as_view(), name = 'post-update'),
     path('post/<int:pk>/delete/',views.PostDeleteView.as_view(), name = 'post-delete'),
    path('about/',views.about, name = 'blog-about'),

]


