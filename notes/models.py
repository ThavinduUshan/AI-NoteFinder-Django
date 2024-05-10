from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.OneToOneField(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
