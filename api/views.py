from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import ProjectSerializer
from projects.models import Project
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from projects.models import Review

# @api_view -> denotes what are the routes to be used


@api_view(['GET'])
def getRoutes(req):
    routes = [
        {'GET': "/api/projects"},
        {'GET': "/api/projects/id"},
        {'POST': "/api/projects/id/vote"},

        {"POST": "/api/users/token"},
        {"POST": "/api/users/token/refresh"}
    ]

    # safe = False -> means we can send any form of data that can converted to javascript, if not it only accepts the dictionary
    return Response(routes)


# first it checks whethere the method is GET
# next it checks whether any user is authenticated
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getProjects(req):
    print("user : ", req.user)
    projects = Project.objects.all()
    # many - > true, if we are seralizing one field or more
    sr = ProjectSerializer(projects, many=True)

    return Response(sr.data)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getProject(req, pk):
    project = Project.objects.get(id=pk)
    # for i in range(0, len(project['tags'])):
    #     project['tags'][i] = TagSerializer(project['tags'][i])

    sr = ProjectSerializer(project, many=False)
    return Response(sr.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def projectVote(req, pk):
    project = Project.objects.get(id=pk)
    user = req.user.profile
    data = req.data

    # if no object in the database with the keyword arguments, creates a new one, if there is an object pulls out the existing one
    review, created = Review.objects.get_or_create(
        owner=user,
        project=project,
        # value
    )

    review.value = data['value']
    review.save()

    sr = ProjectSerializer(project, many=False)
    return Response(sr.data)
