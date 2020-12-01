from django.db import models

class NewsModel(models.Model):
    """
    News models that might contain title, link, newsTag, image
    """

    title = models.CharField(max_length=255)
    link = models.TextField()
    newsTag = models.CharField(max_length=500)
    image = models.TextField()

    def __str__(self):
        return self.title