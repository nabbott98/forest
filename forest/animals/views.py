# # animals/views.py
# from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status


# # def index(request):
# #   return HttpResponse('<h1>Welcome to the forest! 🌲</h1>')

# from animals.models import Animal
# from animals.serializers import AnimalSerializer

# serializer_class = AnimalSerializer
# def index(request):
#     animals = Animal.objects.all()
#     # data = list(animals.values())
#     serializer = AnimalSerializer(animals, many=True)
#     return Response({'animals': serializer.data})

from django.shortcuts import render, get_object_or_404
from animals.serializers import AnimalSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Animal

# Create your views here.
#localhost:3000/animals/ get post
class AnimalsView(APIView):
    """View class for animals/ for viewing all and creating"""
    def get(self, request):
        animals = Animal.objects.all()
        serializer = AnimalSerializer(animals, many=True)
        return Response({'animals': serializer.data})

    def post(self, request):
        serializer = AnimalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#localhost:3000/animals/:id get delete update
class AnimalDetailView(APIView):
    """View class for animals/:pk for viewing a single animal, updating a single animal, or removing a single animal"""
    def get(self, request, pk):
        animal = get_object_or_404(Animal, pk=pk)
        serializer = AnimalSerializer(animal)
        return Response({'animal': serializer.data})


    def patch(self, request, pk):
            animal = get_object_or_404(Animal, pk=pk)
            serializer = AnimalSerializer(animal, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, pk):
        animal = get_object_or_404(Animal, pk=pk)
        animal.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
