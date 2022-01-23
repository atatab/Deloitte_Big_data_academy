from django.urls import path
from siteDataApi import views

urlpatterns = [
    path("",views.ListServiceAPIView.as_view(),name="list_service"),
    path("create/", views.CreateServiceAPIView.as_view(),name="create_service"),
    path("update/<int:pk>/",views.UpdateServiceAPIView.as_view(),name="update_service"),
    path("delete/<int:pk>/",views.DestroyServiceAPIView.as_view(),name="delete_service")
]