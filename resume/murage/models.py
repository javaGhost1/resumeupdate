from pydoc import describe
from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    technologies = models.CharField(max_length=100)
    desc = models.TextField()

    image = models.ImageField(upload_to="images/", blank=True)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})
