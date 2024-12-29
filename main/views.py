from django.shortcuts import render

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .models import Post
from .serializers import PostSerializer

# Create your views here.


class PostViewSet(ViewSet):

    permission_classes = [IsAuthenticatedOrReadOnly, ]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request  # requestni contextga qo'shish
        return context

    def list(self, request, pk=None):
        try:
            if not pk:
                posts = Post.objects.all()
                serializer = PostSerializer(posts, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({'message': 'This method does not require an ID.'})
        except Exception as e:
            return Response({'error': f"{e}"})
    
    def retrieve(self, request, pk=None):
        try:
            if pk:
                post = Post.objects.get(pk=pk)
                serializer = PostSerializer(post)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({'message': 'This method requires an ID.'})
        except Post.DoesNotExist:
            return Response({'message': f'Object with ID {pk} not found.'})
    
    def create(self, request, pk=None):
        if not pk:
            serializer = PostSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save(author=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'This method does not require an ID.'})
    
    def update(self, request, pk=None):
        try:
            if pk:
                post = Post.objects.get(pk=pk)
                if post.author != request.user.account:
                    return Response({'error': "You don't have permission to edit to edit this post."}, status=status.HTTP_403_FORBIDDEN)
                serializer = PostSerializer(post, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_200_OK)
            return Response({'message': 'This method does not require an ID.'})
        except Post.DoesNotExist:
            return Response({'message': f'Object with ID {pk} not found.'}, status=status.HTTP_404_NOT_FOUND)        
    
    def delete(self, request, pk=None):
        try:
            if pk:
                post = Post.objects.get(pk=pk)
                if post.author != request.user.account:
                    return Response({'error': "You don't have permission to delete this post."}, status=status.HTTP_403_FORBIDDEN)
                post.delete()
                return Response({'message': 'Object deleted successfuly.'}, status=status.HTTP_200_OK)
            return Response({'message': 'This method requires an ID.'}, status=status.HTTP_200_OK)
        except Post.DoesNotExist:
            return Response({'message': f'Object with ID {pk} not found.'}, status=status.HTTP_404_NOT_FOUND)
        