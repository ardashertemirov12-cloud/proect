from django.db import models



class Yangiliklar(models.Model):
    title = models.CharField(max_length=512)
    content = models.TextField()
    image = models.ImageField(upload_to='images/')
    author = models.CharField(max_length=120)


    def __str__(self):
        return self.title


class User (models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=120)
    number = models.CharField(max_length=12)
    image = models.ImageField(upload_to='images/')
    autobiography = models.CharField(max_length=500)
    date = models.DateField()

    def __str__(self):
        return self.title
















