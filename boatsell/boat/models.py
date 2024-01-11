from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Owner(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя')
    email = models.EmailField(verbose_name='Почта', unique=True)

    def __str__(self):
        return f'{self.name} ({self.email})'

    class Meta:
        verbose_name = 'Владелец'
        verbose_name_plural = 'Владельцы'


class Boat(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    year = models.PositiveSmallIntegerField(**NULLABLE, verbose_name='Год выпуска')
    price = models.IntegerField(**NULLABLE, verbose_name='Цена')
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, **NULLABLE, verbose_name='Владелец')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Лодка'
        verbose_name_plural = 'Лодки'


class BoatHistory(models.Model):
    boat = models.ForeignKey(Boat, on_delete=models.CASCADE, verbose_name='Лодка')
    owner = models.ForeignKey(Owner, on_delete=models.SET_NULL, verbose_name='Владелец', **NULLABLE)

    start_year = models.PositiveSmallIntegerField(verbose_name='Владел с', **NULLABLE)
    stop_year = models.PositiveSmallIntegerField(verbose_name='Владел по', **NULLABLE)

    def __str__(self):
        return f'{self.boat} {self.start_year}-{self.stop_year}'

    class Meta:
        verbose_name = 'История'
        verbose_name_plural = 'История'

