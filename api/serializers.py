from rest_framework import serializers
from api.models import Article,Tag,gagUser,ArticleTag,TagUser,Vote
from rest_framework.validators import UniqueTogetherValidator,UniqueValidator
from django.db import models


class TagSerializer(serializers.ModelSerializer):
	text = models.CharField(max_length=50,unique=True,validators = [
            		UniqueValidator(queryset=Tag.objects.all())
        	])
	class Meta:
		model = Tag
		fields = ('id',"text")


class ArticleTagSerializer(serializers.ModelSerializer):
	class Meta:
		model = ArticleTag
		validators = [
           		 UniqueTogetherValidator(
          		      queryset=ArticleTag.objects.all(),
          		      fields=('id','article', 'tag')
          		  )
       		 ]
class ArticleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Article
		tags = ArticleTagSerializer(many=True)
		fields = ('id','title','contentUrl','points','tags')
		validators = [
            		UniqueValidator(queryset=Article.objects.all())
        	]

class TagUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = TagUser
		validators = [
           		 UniqueTogetherValidator(
          		      queryset=TagUser.objects.all(),
          		      fields=('id','tag', 'user')
          		  )
       		 ]

class GagUserSerializer(serializers.ModelSerializer):
	name = models.CharField(max_length=100,unique=True,validators = [
			UniqueValidator(queryset=gagUser.objects.all())
		]) 
	class Meta:
		model = gagUser
		tags = TagUserSerializer(many=True)
		fields = ('id','name','tags')


class VoteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Vote
		validators = [
           		 UniqueTogetherValidator(
          		      queryset=Vote.objects.all(),
          		      fields=('id','article', 'user')
          		  )
       		 ]

