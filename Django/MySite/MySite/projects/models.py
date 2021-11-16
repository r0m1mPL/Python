from django.db import models
from django.utils import timezone


class Project(models.Model):
    """Проекты"""
    title = models.CharField("Заголовок", max_length=160)
    short_description = models.CharField("Краткое описание", max_length=200)
    description = models.TextField("Описание")
    pub_date = models.DateTimeField(default=timezone.now)
    url = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"