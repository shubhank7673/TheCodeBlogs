from django.db import models
from datetime import datetime,date
class posts(models.Model):
    title = models.TextField(max_length=50)
    content = models.TextField()
    date = models.CharField(max_length=40,default=date.today())
    slug = models.CharField(max_length=40)
    img_file = models.CharField(max_length=40)
    image_upl = models.FileField(upload_to='',blank=True)
    sub_heading = models.TextField()
    def __str__(self):
        return self.slug
    def get_absolute_url(self):
    	return reverse('model-detail-view', args=[str(self.id)])

class contact(models.Model):
    name = models.CharField(max_length=22)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    date = models.CharField(max_length=30)
    message = models.TextField()
