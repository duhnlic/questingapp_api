from django.db import models


class User(models.Model):
    username = models.CharField(max_length=10, default="username")

    def __str__(self):
        return self.username

class Quest(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="quest")
    stat = models.CharField(max_length=100, default="0")
    total = models.CharField(max_length=100, default="0")
    kind = models.CharField(max_length=100, default="questing")

    def __str__(self):
        return self.name

class Strength(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="strength")
    strength = models.CharField(max_length=10, default="0")

    def __str__(self):
        return self.strength


class Endurance(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="endurance")
    endurance = models.CharField(max_length=10, default="0")

    def __str__(self):
        return self.endurance

class Wisdom(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="wisdom")
    wisdom = models.CharField(max_length=10, default="0")

    def __str__(self):
        return{f"{self.name.username}'s Wisdom: {self.wisdom}"}


