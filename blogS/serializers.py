from django.contrib.auth.models import User
from rest_framework import serializers

from blogS.models import Article


class UserSerializer(serializers.HyperlinkedModelSerializer):

   class Meta:
       model = User
       fields = ('username', 'first_name', 'email')



class ArticleSerializer(serializers.HyperlinkedModelSerializer):

       au = UserSerializer()

       class Meta:
           model = Article
           fields = ('id', 'url', 'title', 'body', 'im', 'au')