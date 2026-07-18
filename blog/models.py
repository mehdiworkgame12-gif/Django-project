from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name= models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
class Post(models.Model):
    image=models.ImageField(upload_to='blog/',default='/blog/default.jpg')
    auhtor=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    category=models.ManyToManyField(Category)
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True)
    class Meta:
        ordering = ['-created_date']
        verbose_name= 'post'
        verbose_name_plural= 'posts'
    def __str__(self):
        return  ' {} - {}' .format(self.title,self.id)
from django.db import models
from django import forms
def get_absolute_url(self):
    return reversed('blog:single',kwargs={'pid':self.id})

