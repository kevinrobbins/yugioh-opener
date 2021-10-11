from django.db import models
from django.core.validators import MaxValueValidator


class CardSet(models.Model):
    name = models.CharField(max_length=128, unique=True)
    abbr = models.CharField(max_length=4)


class CardAttribute(models.Model):
    name = models.CharField(max_length=32, unique=True)


class CardType(models.Model):
    name = models.CharField(max_length=32, unique=True)


class Card(models.Model):
    name = models.CharField(max_length=128, unique=True)
    attribute = models.CharField(max_length=25)
    type = models.CharField(max_length=25)
    level = models.PositiveSmallIntegerField(validators=[MaxValueValidator(12)])
    text = models.TextField(max_length=1024)
    attack = models.PositiveSmallIntegerField()
    defense = models.PositiveSmallIntegerField()
    releases = models.ManyToManyField(to=CardSet, through='Release', related_name='cards')


class Release(models.Model):
    class Rarity(models.TextChoices):
        COMMON = 'COMMON', 'Common'
        RARE = 'RARE', 'Rare'
        SUPER_RARE = 'SUPER_RARE', 'Super Rare'
        ULTRA_RARE = 'ULTRA_RARE', 'Ultra Rare'
        SECRET_RARE = 'SECRET_RARE', 'Secret Rare'

    set = models.ForeignKey(to=CardSet, related_name='sets', on_delete=models.CASCADE)
    card = models.ForeignKey(to=Card, related_name='cards', on_delete=models.CASCADE)
    card_number = models.PositiveSmallIntegerField(validators=[MaxValueValidator(999)])
    rarity = models.CharField(choices=Rarity.choices, default=Rarity.COMMON, max_length=32)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['set_id', 'card_id'], name='unique card/set')
        ]
