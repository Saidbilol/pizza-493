from django.db import models


class ScrollModel(models.Model):
    image = models.ImageField(upload_to="scrolls/")
    discount = models.PositiveIntegerField()
    title = models.CharField(max_length=50)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Scroll"
        verbose_name_plural = "Scrolls"


class GallaryModel(models.Model):
    image = models.ImageField(upload_to="gallary/")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Gallary"
        verbose_name_plural = "Gallries"


class MenuModel(models.Model):
    image = models.ImageField(upload_to="menu/")
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menus"
