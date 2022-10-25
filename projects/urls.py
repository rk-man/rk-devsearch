from django.urls import path


from projects.views import getProject, projects, createProject, updateProject, deleteProject

urlpatterns = [
    path('', projects, name="projects"),
    path("<str:pk>/", getProject, name="get-project"),
    path("create-project", createProject, name="create-project"),
    path("update-project/<str:pk>/",
         updateProject, name="update-project"),
    path("delete-project/<str:pk>/",
         deleteProject, name="delete-project"),

]
