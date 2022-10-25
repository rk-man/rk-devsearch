from django.urls import path
from api.views import getRoutes, getProjects, getProject, projectVote
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("", getRoutes, name="all-routes"),
    path("projects/", getProjects, name="all-projects"),
    path("projects/<str:pk>", getProject, name="single-project"),
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("projects/<str:pk>/vote-project/", projectVote, name="project-vote"),
]
