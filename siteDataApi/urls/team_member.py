from django.urls import path
from siteDataApi import views

urlpatterns = [
    path("",views.ListTeamMemberAPIView.as_view(),name="list_team_member"),
    path("create/", views.CreateTeamMemberAPIView.as_view(),name="create_team_member"),
    path("update/<int:pk>/",views.UpdateTeamMemberAPIView.as_view(),name="update_team_member"),
    path("delete/<int:pk>/",views.DestroyTeamMemberAPIView.as_view(),name="delete_team_member")
]