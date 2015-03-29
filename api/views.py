from django.shortcuts import render
from api.models import Article,Tag,gagUser,ArticleTag,TagUser,Vote
from api.serializers import ArticleSerializer,TagSerializer,GagUserSerializer,ArticleTagSerializer,TagUserSerializer,VoteSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404



class ArticlesbyTag(APIView):
	def get_objects(self, tag):
		try:
			return [x.article for x in ArticleTag.objects.filter(tag=Tag.objects.get(text=tag))]
		except Tag.DoesNotExist:
			raise Http404

	def get(self, request, tag, format=None):
		articles = self.get_objects(tag)
		serializer = ArticleSerializer(articles,many=True)
		return Response(serializer.data)

class ArticleList(APIView):
	def get(self,request,format=None):
  		articles = Article.objects.all()
  		serializer = ArticleSerializer(articles,many=True)
  		return Response(serializer.data)

  	def post(self,request,format=None):
		serializer = ArticleSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TagList(APIView):
	def get(self,request,format=None):
  		tags = Tag.objects.all()
  		serializer = TagSerializer(tags,many=True)
  		return Response(serializer.data)

  	def post(self,request,format=None):
		serializer = TagSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  			
class GagUserList(APIView):
	def get(self,request,format=None):
  		users = gagUser.objects.all()
  		serializer = GagUserSerializer(users,many=True)
  		return Response(serializer.data)

  	def post(self,request,format=None):
		serializer = GagUserSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArticleTagList(APIView):
	def get(self,request,format=None):
  		artictags = ArticleTag.objects.all()
  		serializer = ArticleTagSerializer(artictags,many=True)
  		return Response(serializer.data)

  	def post(self,request,format=None):
		serializer = ArticleTagSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TagUserList(APIView):
	def get(self,request,format=None):
  		tagusers = TagUser.objects.all()
  		serializer = TagUserSerializer(tagusers,many=True)
  		return Response(serializer.data)

  	def post(self,request,format=None):
		serializer = TagUserSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VoteList(APIView):
	def get(self,request,format=None):
  		votes = Vote.objects.all()
  		serializer = VoteSerializer(votes,many=True)
  		return Response(serializer.data)

  	def post(self,request,format=None):
		serializer = VoteSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArticleDetail(APIView):
	def get_object(self, pk):
		try:
			return Article.objects.get(pk=pk)
		except Article.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		article = self.get_object(pk)
		serializer = ArticleSerializer(article)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		article = self.get_object(pk)
		serializer = ArticleSerializer(article, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		article = self.get_object(pk)
		article.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class TagDetail(APIView):
	def get_object(self, pk):
		try:
			return Tag.objects.get(pk=pk)
		except Tag.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		tag = self.get_object(pk)
		serializer = TagSerializer(tag)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		tag = self.get_object(pk)
		serializer = TagSerializer(article, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		tag = self.get_object(pk)
		tag.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class GagUserDetail(APIView):
	def get_object(self, pk):
		try:
			return gagUser.objects.get(pk=pk)
		except gagUser.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		gUser = self.get_object(pk)
		serializer = GagUserSerializer(gUser)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		gUser = self.get_object(pk)
		serializer = GagUserSerializer(article, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		gUser = self.get_object(pk)
		gUser.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class ArticleTagDetail(APIView):
	def get_object(self, pk):
		try:
			return ArticleTag.objects.get(pk=pk)
		except ArticleTag.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		articleTag = self.get_object(pk)
		serializer = ArticleTagSerializer(articleTag)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		articleTag = self.get_object(pk)
		serializer = ArticleTagSerializer(articleTag, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		articleTag = self.get_object(pk)
		articleTag.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class TagUserDetail(APIView):
	def get_object(self, pk):
		try:
			return TagUser.objects.get(pk=pk)
		except TagUser.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		tagUser = self.get_object(pk)
		serializer = TagUserSerializer(tagUser)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		tagUser = self.get_object(pk)
		serializer = TagUserSerializer(tagUser, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		tagUser = self.get_object(pk)
		tagUser.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class VoteDetail(APIView):
	def get_object(self, pk):
		try:
			return Vote.objects.get(pk=pk)
		except Vote.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		vote = self.get_object(pk)
		serializer = VoteSerializer(vote)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		vote = self.get_object(pk)
		serializer = VoteSerializer(vote, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		vote = self.get_object(pk)
		vote.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)







