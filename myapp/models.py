from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
    image = models.ImageField(null=False, blank=True)
    image_name = models.CharField(max_length=50,null=False, blank=False)
    image_caption = models.TextField()
    image_date = models.DateTimeField(auto_now_add=True)
    image_likes = models.IntegerField(default=0,null=False, blank=False)
    image_comments = models.TextField(null=False, blank=False)
    image_profile= models.ForeignKey('Profile', on_delete=models.CASCADE,null=False, blank=False)

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()


class Profile(models.Model):
    profile_bio = models.TextField()
    profile_image = models.ImageField(null=False, blank=False)
    profile_name = models.CharField(max_length=50,null=False, blank=False)

    def __str__(self):
        return self.profile_name


