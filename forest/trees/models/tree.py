from django.db import models

# Create your models here.
class Tree(models.Model):
    type = models.CharField(max_length=100)
    age = models.IntegerField()
    height = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"The {self.type} tree is {self.height} feet tall and {self.age} years old."

