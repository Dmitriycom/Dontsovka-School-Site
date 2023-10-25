from django.db import models 


class News(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    path = models.FileField('Путь в виде ссылки', default="default.jpeg")
    description = models.TextField('Описание')
    date = models.DateField("Дата создания", default="2023-01-01")


    def __str__(self) -> str:
        return self.title

