from django.urls import path
from . import views

urlpatterns = [
    path("", views.profiles, name="profiles"),
    path("profile/<str:pk>/", views.userProfile, name="user-profile"),
    # path("create-project", views.create_project, name="create-project"),
    # path("update-project/<str:pk>/", views.update_project, name="update-project"),
    # path("delete-project/<str:pk>/", views.delete_project, name="delete-project"),
]
