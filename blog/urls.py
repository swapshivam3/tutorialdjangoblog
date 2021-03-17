from . import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView
from django.urls import path

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),
    path('post/new/',PostCreateView.as_view(),name='post-create'),
    path('about/',views.about, name='blog-about'),
    path('user/<str:username>',UserPostListView.as_view(),name='user-posts'),
    path('b0d5ca0798bf6a4356b249b97a35ab2d.html',views.verification_smtp,name='verification-smtp')
]


#<app>/<model>_<viewtype>.html
#blog/post_list