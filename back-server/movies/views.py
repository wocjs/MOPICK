from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from .models import Movies
from .serializers import MovieSerializer

from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

# Create your views here.

# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def getMovies(request):
    if request.method == "GET":
        movies = get_list_or_404(Movies)
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
