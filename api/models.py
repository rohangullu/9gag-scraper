from django.db import models
from rest_framework.validators import UniqueTogetherValidator,UniqueValidator

class Article(models.Model):
    title = models.CharField(max_length=1000)
    contentUrl = models.CharField(max_length=1000,unique=True)
    points = models.IntegerField()

class Tag(models.Model):
	text = models.CharField(max_length=50,unique=True)

class gagUser(models.Model):
	name = models.CharField(max_length=100,unique=True)

class ArticleTag(models.Model):
	article = models.ForeignKey(Article,related_name="tags")
	tag = models.ForeignKey(Tag)

	class Meta:
		unique_together = ('article','tag')

class TagUser(models.Model):
	user = models.ForeignKey(gagUser,related_name = "tags")
	tag = models.ForeignKey(Tag)

	class Meta:
		unique_together = ('user','tag')

class Vote(models.Model):
	article = models.ForeignKey(Article,related_name="votes")
	user = models.ForeignKey(gagUser,related_name="votes")
	votetype = models.IntegerField()

	class Meta:
		unique_together = ('article','user')


