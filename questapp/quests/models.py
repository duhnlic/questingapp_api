from django.db import models

# Create your models here.
class Quest(models.Model):
    name = models.CharField(max_length=100)
    stat = models.CharField(max_length=100)
    total = models.CharField(max_length=100)

    def __str__(self):
        return {{self.name}}

class Strength(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="strength")
    strength = models.CharField(max_length=10)

    def __str__(self):
        return{f"{self.name.username}'s Strength: {self.strength}"}


class Endurance(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="endurance")
    endurance = models.CharField(max_length=10)

    def __str__(self):
        return{f"{self.name.username}'s Endurance: {self.endurance}"}

class Wisdom(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="wisdom")
    wisdom = models.CharField(max_length=10)

    def __str__(self):
        return{f"{self.name.username}'s Wisdom: {self.wisdom}"}



class User(models.Model):
    username = models.CharField(max_length=10)