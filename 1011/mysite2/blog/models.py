# django models fields
# https://docs.djangoproject.com/en/4.2/ref/models/fields/
# pip install pillow
# pillow는 이미지 관련 라이브러리입니다.
# 매우 많은 프레임웤이나 라이브러리가 이 라이브러리를 사용합니다.
# 이미지를 자르거나, 확대하거나, 축소하거나, 저장하거나 등이 사용됩니다.

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    contents = models.TextField()
    # main_image = models.ImageField(upload_to='blog/', blank=True, null=True) # upload_to='blog/' : blog 폴더 안에 저장
    main_image = models.ImageField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title