from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=200)
    pokedex_id = models.PositiveIntegerField()
    height = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    type = models.CharField(max_length=100)
    secondary_type = models.CharField(max_length=100)
    hp = models.PositiveIntegerField()
    attack = models.PositiveIntegerField()
    defense = models.PositiveIntegerField()
    sp_atk = models.PositiveIntegerField()
    sp_def = models.PositiveIntegerField()
    speed = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Pokemon'
        verbose_name_plural = 'Pokemon'
        ordering = ('name',)