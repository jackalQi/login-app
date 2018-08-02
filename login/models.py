from django.db import models

# Create your models here.


class User(models.Model):
    gender = (
        ("m", "male"),
        ("f", "female"),
    )

    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=1, choices=gender, default="f")
    create_date = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-create_date"]
