# Import decorator for api view from DRF
from rest_framework.decorators import api_view

from rest_framework.response import Response
from poses.models import Pose
from .serializers import PoseSerializer


@api_view(['GET'])

def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/poses',
        'GET /api/poses/:id'
    ]

    return Response(routes)


@api_view(['GET'])
def getPoses(request):

    poses = Pose.objects.all()
    serializer = PoseSerializer(poses, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getPose(request, pk):

    yoga = Pose.objects.get(id=pk)

    serializer = PoseSerializer(yoga, many=False)
    return Response(serializer.data)
