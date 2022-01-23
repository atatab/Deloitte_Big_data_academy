from django.urls import path, include

urlpatterns = [
    path("service/", include("siteDataApi.urls.service")),
    path("team_member/", include("siteDataApi.urls.team_member")),
    path("blog_post/", include("siteDataApi.urls.blog_post"))
]