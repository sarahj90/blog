from django.shortcuts import render
from rest_framework import viewsets

from blogS.models import Article
from blogS.serializers import ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
