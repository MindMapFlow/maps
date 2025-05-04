from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Map
from .serializers import MapSerializer

class MapListAPIView(APIView):
    def get(self, request):
        maps = Map.objects.all()
        serializer = MapSerializer(maps, many=True)
        result = {}
        for item in serializer.data:
            result.update(item)
        return Response(result, status=status.HTTP_200_OK)