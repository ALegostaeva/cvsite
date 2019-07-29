from django.db import models


class Project(models.Model):
    project_title = models.TextField(max_length=100)
    project_id = models.IntegerField(primary_key=True)
    project_description = models.TextField(max_length=300)

    def __str__(self):
        return self.project_title

    class Meta:
        ordering = ['project_id']


class Image(models.Model):
    image_title = models.TextField(max_length=100)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, default=0)
    image = models.ImageField()

    def __str__(self):
        return self.image_title
