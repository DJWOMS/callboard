from django.db import models


class Photo(models.Model):
    """Фото"""
    name = models.CharField("Имя", max_length=50)
    #TODO: для image генерить путь (user, date)
    #TODO: создавать миниатюры, ограничить вес фото и размер
    image = models.ImageField("Фото", upload_to="gallery/")
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    slug = models.SlugField("url", max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"


class Gallery(models.Model):
    """Галерея"""
    name = models.CharField("Имя", max_length=50)
    photos = models.ManyToManyField(Photo, verbose_name="Фотографии")
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    slug = models.SlugField("url", max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Галерея"
        verbose_name_plural = "Галереи"
