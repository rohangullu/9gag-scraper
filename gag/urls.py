from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
from api import views
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gag.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^articles/$', views.ArticleList.as_view()),
    url(r'^articles/(?P<tag>[A-Za-z0-9]+)/$',views.ArticlesbyTag.as_view()),
   	url(r'^tags/$', views.TagList.as_view()),
    url(r'^gagusers/$', views.GagUserList.as_view()),
    url(r'^articletags/$', views.ArticleTagList.as_view()),
    url(r'^tagusers/$', views.TagUserList.as_view()),
    url(r'^votes/$', views.VoteList.as_view()),
    url(r'^articles/(?P<pk>[0-9]+)/$', views.ArticleDetail.as_view()),
    url(r'^tags/(?P<pk>[0-9]+)/$', views.TagDetail.as_view()),
    url(r'^gagusers/(?P<pk>[0-9]+)/$', views.GagUserDetail.as_view()),
    url(r'^articletags/(?P<pk>[0-9]+)/$', views.ArticleTagDetail.as_view()),
    url(r'^tagusers/(?P<pk>[0-9]+)/$', views.TagUserDetail.as_view()),
    url(r'^votes/(?P<pk>[0-9]+)/$', views.VoteDetail.as_view()),



) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
