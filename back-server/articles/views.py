from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from .models import Article, Comment, UserLike
from .serializers import ArticleListSerializer, CommentSerializer

from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.http import JsonResponse



# Create your views here.
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == "GET":
        # articles = Article.objects.all()
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = ArticleListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)





@api_view(['GET', 'DELETE', 'PUT', 'POST'])
def article_detail(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)


    if request.method == 'GET':
        serializer = ArticleListSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        if request.user == article.user:
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
    
    elif request.method == 'PUT':
        if request.user == article.user:
            serializer = ArticleListSerializer(article, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
        
    # 혹시 게시글에 post 요청이 좋아요 말고 충돌날 가능성이 뭐가 있을까요?
    elif request.method == 'POST':
        user = request.user.pk
        if article.likes.filter(id=request.user.pk).exists():
            #print('#################################################################')
            #print(request.user.id)
            # 좋아요 이미 누른 경우 좋아요 취소
            article.likes.remove(request.user)
            is_liked = False
        else:
            # 아니라면 좋아요
            article.likes.add(request.user)
            #print('아닐때!@#!@#!@$%@!%##$^!@$#%@$#@!$@!#$@#!$!@#$!@#$!@$')
            #print(request.user.id)
            is_liked = True
        context = {
            'user' : user,
            'is_liked' : is_liked,
            'like_count' : article.likes.count()
        }
        return JsonResponse(context)
    return Response(status=status.HTTP_200_OK)


@api_view(['GET','POST', 'DELETE'])
def comment_list(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    elif request.method == 'GET':
        comments = article.comment_set.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)



@api_view(['GET', 'DELETE', 'PUT', 'POST'])
@permission_classes([IsAuthenticated])
def comment_detail(request, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        if request.user == comment.user:
            comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'POST':
        user = request.user.pk
        # comment = request.comment.pk
        if comment.likes.filter(id=request.user.pk).exists():
            comment.likes.remove(request.user)
            comment_is_liked = False
        else:
            comment.likes.add(request.user)
            comment_is_liked = True
        # user_like = UserLike.objects.get_or_create(user=request.user),
        # user_like.comment_is_liked = comment_is_liked
        # user_like.save()
        context = {
            'user' : user,
            # 'comment' : comment,
            'comment_is_liked' : comment_is_liked,
            'comment_like_count' : comment.likes.count()
        }
        return JsonResponse(context)
        return Response(status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        if request.uesr == comment.user:
            serializer = CommentSerializer(comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)



#####
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user(request):
    user = request.user
    serialized_user = {
        # 'username': user.username,
        'user': user.id,
    }
    print('#####################################################################')
    print(user)
    return Response(serialized_user)


# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def current_comment(request):
#     comment = request.comment
#     serialized_comment = {
#         'commentId': comment.id,
#     }
#     return Response(serialized_comment)

def like_comment(request, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    user = request.user

    if user in comment.likes.all():
        comment.likes.remove(user)
    else:
        comment.likes.add(user)
    
    return Response(status=status.HTTP_200_OK)