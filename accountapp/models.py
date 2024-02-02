from django.db import models

# Create your models here.
class HelloWorld(models.Model):
  text = models.CharField(max_length=255, null=False)   # null=False라는 것은 그 칸이 비어 있으면 안된다는 뜻