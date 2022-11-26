from django.shortcuts import render, get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from ..models.park import Park
from ..serializers import ParkSerializer, ParkViewSerializer

# Create your views here.
# localhost:3000/parks/ get post
class ParksView(APIView):
    """View class for parks/ for viewing all and creating"""
    serializer_class = ParkSerializer
    def get(self, request):
        parks = Park.objects.all()
        serializer = ParkViewSerializer(parks, many=True)
        return Response({'parks': serializer.data})

    def post(self, request):
        serializer = ParkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# localhost:3000/parks/:id get delete update
class ParkDetailView(APIView):
    serializer_class = ParkSerializer
    """View class for parks/:pk for viewing a single park, updating a single park, or removing a single park"""
    def get(self, request, pk):
        park = get_object_or_404(Park, pk=pk)
        serializer = ParkViewSerializer(park)
        return Response({'park': serializer.data})


    def patch(self, request, pk):
            park = get_object_or_404(Park, pk=pk)
            serializer = ParkSerializer(park, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, pk):
        park = get_object_or_404(Park, pk=pk)
        park.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
