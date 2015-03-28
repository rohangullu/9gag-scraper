from django.contrib import admin
from api.models import Article

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
	pass	


admin.site.register(Article,ArticleAdmin)
