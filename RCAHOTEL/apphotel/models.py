from django.db import models
from django.contrib import admin
from tinymce import models as tinymce_models
from PIL import Image

ESTADO_VISIBLE= [1,2]
# Create your models here.
class ManejadorPost(models.Manager):
	def get_query_set(self):
		default_queryset =super(ManejadorPost,self).get_query_set()
		return default_queryset.filter(status__in=ESTADO_VISIBLE)


class HotelrcaPost(models.Model):
	ESTADOS=((1,"Publicado"),(2,"Archivado"),(3,"Necesita Editarse"),(4,"Necesita Aprobacion"))
	status=models.IntegerField(choices=ESTADOS,default=4)
	objetos_panel=models.Manager()
	objects=ManejadorPost()
	title=models.CharField(max_length=150)	
	time=models.DateTimeField()
	body=tinymce_models.HTMLField()
	imagen=models.ImageField(upload_to='photos')	

class BlogPostAdmin(admin.ModelAdmin):
	list_display=('title','body','status')
	list_instances=True
	search_fields=['title']




admin.site.register(HotelrcaPost,BlogPostAdmin)