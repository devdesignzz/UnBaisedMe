from django.urls import path
from .views import HomeView, PostView, PostDetailView, AddPostView, UpdatePostView, DeletePostView, CategoryView, CategoryListView, AddCommentView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('all-posts/', PostView.as_view(), name='posts'),
    path('post/<slug:slug>', PostDetailView.as_view(), name='post'),
    path('add-post/', AddPostView.as_view(), name='add-post'),
    path('update-post/<slug:slug>', UpdatePostView.as_view(), name='update-post'),
    path('delete-post/<slug:slug>', DeletePostView.as_view(), name='delete-post'),
    path('posts/category/<slug:slug>', CategoryView, name='category'),
    path('all-categories/', CategoryListView, name='categories'),
    path('post/<slug:slug>/add-comment', AddCommentView.as_view(), name='add-comment'),
]

