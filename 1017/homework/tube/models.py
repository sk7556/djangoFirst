from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    head_video = models.ImageField(
        upload_to='tube/video/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(
        upload_to='tube/files/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title