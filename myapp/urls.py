from django.urls import path
from .views import (
    AuthorListCreateView,
    AuthorDetailView,
    PostListCreateView,
    PostDetailView,
)

urlpatterns = [
    path("authors/", AuthorListCreateView.as_view(), name="author-list-create"),
    path("authors/<int:pk>/", AuthorDetailView.as_view(), name="author-detail"),
    path("posts/", PostListCreateView.as_view(), name="post-list-create"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
]
