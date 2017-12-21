from django.db import models
from django.core.files.storage import FileSystemStorage
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
    category = models.CharField(max_length=34)

    def __str__(self):
        return self.category

class Portfolio(models.Model):
    # images = models.
    portfolio_name = models.CharField(max_length=34)
    def __str__(self):
        return self.portfolio_name

class KidPicPost(models.Model):

    image = models.ImageField(upload_to='images/', width_field="width_field", height_field="height_field",)
    height_field = models.IntegerField(default=400)
    width_field = models.IntegerField(default=400)
    author = models.ForeignKey(User)
    create_date = models.DateTimeField(default=timezone.now,auto_created=True)
    title = models.CharField(max_length=34,blank=True)
    caption = models.TextField(max_length=500,blank=True)
    portfolio = models.ForeignKey(Portfolio)
    category = models.ForeignKey(Category,blank=True,null=True)

    def publish(self):

        self.pub_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title





