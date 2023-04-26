from django.shortcuts import render
from rest_framework import mixins, viewsets
from .models import Post
from .serializers import PostSerializer
from .paginations import DocumentPagination


# Create your views here.
class PostViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
       queryset = Post.objects.all()
       serializer_class = PostSerializer