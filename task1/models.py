from django.db import models

class Buyer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    balance = models.DecimalField(max_digits=9, decimal_places=2)
    age = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=50)
    cost = models.DecimalField(max_digits=9, decimal_places=2)
    size = models.DecimalField(max_digits=9, decimal_places=2)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games', default=None)
    def __str__(self):
        return self.title
class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title






# Create your models here.