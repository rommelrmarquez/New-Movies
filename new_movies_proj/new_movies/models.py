from django.db import models

class Movie(models.Model):
    '''

    '''

    title = models.CharField(max_length=128)
    img_src = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    rating = models.CharField(max_length=15)

    def __str__(self):
        return self.title
