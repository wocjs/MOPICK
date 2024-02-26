from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer

from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

from django.contrib.auth import authenticate, get_user_model

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def getLikeMovie(request):
    User = get_user_model()
    user = request.user
    serializer = UserSerializer(user)
    if request.method == 'POST':
        # POST 요청의 body에서 업데이트할 데이터를 가져옵니다.
        like_movie_data = request.data.get('like_movie')
        
        if like_movie_data:
            user.like_movie = like_movie_data
            user.save()
            
            return Response({'message': 'like_movie 업데이트 완료'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'like_movie 데이터가 없습니다.'}, status=status.HTTP_400_BAD_REQUEST)
        

    elif request.method == 'GET':
        
        return Response(serializer.data, status=status.HTTP_200_OK)
