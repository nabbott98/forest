# # trees/views.py
# from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status


# # def index(request):
# #   return HttpResponse('<h1>Welcome to the forest! 🌲</h1>')

# from trees.models import Tree
# from trees.serializers import TreeSerializer

# serializer_class = TreeSerializer
# def index(request):
#     trees = Tree.objects.all()
#     # data = list(trees.values())
#     serializer = TreeSerializer(trees, many=True)
#     return Response({'trees': serializer.data})

from django.shortcuts import render, get_object_or_404
from trees.serializers import TreeSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Tree

# Create your views here.
#localhost:3000/trees/ get post
class TreesView(APIView):
    """View class for trees/ for viewing all and creating"""
    def get(self, request):
        trees = Tree.objects.all()
        serializer = TreeSerializer(trees, many=True)
        return Response({'trees': serializer.data})

    def post(self, request):
        serializer = TreeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#localhost:3000/trees/:id get delete update
class TreeDetailView(APIView):
    """View class for trees/:pk for viewing a single tree, updating a single tree, or removing a single tree"""
    def get(self, request, pk):
        tree = get_object_or_404(Tree, pk=pk)
        serializer = TreeSerializer(tree)
        return Response({'tree': serializer.data})


    def patch(self, request, pk):
            tree = get_object_or_404(Tree, pk=pk)
            serializer = TreeSerializer(tree, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, pk):
        tree = get_object_or_404(Tree, pk=pk)
        tree.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
