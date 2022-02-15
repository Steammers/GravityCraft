from django.db import models


class Server(models.Model):
    name = models.CharField('Название сервера', max_length=255)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Сервер'
        verbose_name_plural = 'Серверы'
        ordering = ('name',)


class Mod(models.Model):
    name = models.CharField('Название мода', max_length=255)
    servers = models.ManyToManyField(Server, 'mods', verbose_name='Сервера на которых установлен')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Мод'
        verbose_name_plural = 'Моды'
        ordering = ('name',)


class Item(models.Model):
    name = models.CharField('Название предмета', max_length=255)
    image = models.ImageField('Изображение предмета', upload_to='items_img/', blank=True, null=True)
    mod = models.ForeignKey(Mod, models.PROTECT, 'items', verbose_name='Мод')
    server = models.ForeignKey(Server, models.PROTECT, 'items', verbose_name='Сервер')
    minimum_price = models.IntegerField('Стоимость')
    count = models.IntegerField('Количество', null=True)

    def __str__(self):
        return f'{self.name} / {self.minimum_price}'

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'
        ordering = ('server', 'mod', 'name',)
