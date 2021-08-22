from django.db import models

# Create your models here.
class Personal(models.Model):
    image = models.ImageField(upload_to = "my_image/", blank= True, null = "True")
    upload = models.FileField(upload_to='media')
    title = models.CharField(max_length = 250)

    def __str__(self):
        return self.title

class Image(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to = "work_image/", blank= True, null = "True")

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try: 
            url =self.image.url
        except:
            url=''
        return self._foo

class MyInfo(models.Model):
    name = models.CharField(max_length = 250)
    address = models.CharField(max_length = 250)
    district = models.CharField(max_length = 250)
    province = models.CharField(max_length = 250)
    mobile_no = models.CharField(max_length = 250)
    email = models.CharField(max_length = 250)
    image = models.ImageField(upload_to = "about_image/", blank= True, null = "True")