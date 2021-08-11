from django.db import models
from django.contrib.auth.models import User


class Dayset(models.Model):
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.date}({self.user})"


class Task(models.Model):
    class State(models.TextChoices):
        ACTIVE = 'a', ('Active')
        COMPLETED = 'c', ('Completed')

    title = models.CharField(max_length=256) 
    details = models.TextField()
    creation_date = models.DateTimeField(auto_now=True)
    state = models.CharField(max_length=1, choices=State.choices, default=State.ACTIVE)
    dayset = models.ForeignKey(Dayset, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title