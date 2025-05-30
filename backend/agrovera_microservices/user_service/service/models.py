from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=100)
    telephone = models.CharField(max_length=25, default='0000000000')
    email = models.EmailField(unique=True, default='name@gmail.com')

    AGRICULTURAL_ACTIVITY_CHOICES = [
        ('culture', 'Culture (céréales, légumes, etc.)'),
        ('elevage', 'Élevage (bovins, ovins, volailles...)'),
        ('apiculture', 'Apiculture (élevage d’abeilles)'),
        ('maraichage', 'Maraîchage (légumes et plantes comestibles)'),
        ('arboriculture', 'Arboriculture (arbres fruitiers, oliviers, etc.)'),
        ('autre', 'Autre'),
    ]
    activity_type = models.CharField(max_length=20, choices=AGRICULTURAL_ACTIVITY_CHOICES, default='culture')
    name = models.CharField(max_length=100)
    telephone = models.CharField(max_length=25, default='0000000000')
    email = models.EmailField(unique=True, default='name@gmail.com')

    AGRICULTURAL_ACTIVITY_CHOICES = [
        ('culture', 'Culture (céréales, légumes, etc.)'),
        ('elevage', 'Élevage (bovins, ovins, volailles...)'),
        ('apiculture', 'Apiculture (élevage d’abeilles)'),
        ('maraichage', 'Maraîchage (légumes et plantes comestibles)'),
        ('arboriculture', 'Arboriculture (arbres fruitiers, oliviers, etc.)'),
        ('autre', 'Autre'),
    ]
    activity_type = models.CharField(max_length=20, choices=AGRICULTURAL_ACTIVITY_CHOICES, default='culture')

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()