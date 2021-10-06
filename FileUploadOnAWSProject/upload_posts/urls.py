from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.UploadPostsView.as_view(), name="upload_posts"),

    path('view-posts/<str:id>', views.ViewPostsView.as_view(), name="view_posts"),

    path('view-own-posts/', views.ViewOwnPostsView.as_view(), name="view_own_posts"),

]