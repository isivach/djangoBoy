from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255, verbose_name='Автор')

    class Meta():
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=255, verbose_name='Жанр')

    class Meta():
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def __str__(self):
        return self.name

class Track(models.Model):
    name = models.CharField(max_length=255, verbose_name='Песня')
    duration = models.DurationField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    class Meta():
        verbose_name = "Песня"
        verbose_name_plural = "Песни"

    def __str__(self):
        return self.name
