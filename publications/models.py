import datetime
from django.db import models
from django.utils import timezone
from django import forms

class Publication(models.Model):
    pub_title = models.CharField('Título de anuncio', max_length = 200)
    pub_author = models.CharField('Su nombre', max_length = 60)
    pub_description = models.TextField('Descripción')
    pub_date = models.DateTimeField('Fecha de publicación')
    pub_image = models.ImageField('Imagen', null=True, blank=True, upload_to='images/')
    pub_image_title = forms.CharField(max_length=70)
    pub_tags = models.TextField('Tags')
    pub_objective = models.CharField('Busca u ofrece?', max_length = 50)

    def __str__(self):
        return self.pub_title

    def recent_publication(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days = 11))

    class Meta:
        verbose_name = 'Publication'
        verbose_name_plural = 'Publications'


class Comment(models.Model):
    publication = models.ForeignKey(Publication, on_delete = models.CASCADE)
    comment_author = models.CharField('Su nombre', max_length = 60)
    comment_text = models.CharField('Comentario', max_length = 200)

    def __str__(self):
        return self.comment_author

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

class Image(models.Model):
    pass
