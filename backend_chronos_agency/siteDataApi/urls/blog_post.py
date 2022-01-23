from django.urls import path
from siteDataApi import views

urlpatterns = [
    path("",views.ListBlogPostAPIView.as_view(),name="list_blog_post"),
    path("create/", views.CreateBlogPostAPIView.as_view(),name="create_blog_post"),
    path("update/<int:pk>/",views.UpdateBlogPostAPIView.as_view(),name="update_blog_post"),
    path("delete/<int:pk>/",views.DestroyBlogPostAPIView.as_view(),name="delete_blog_post")
]