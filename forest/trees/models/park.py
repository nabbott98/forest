from django.db import models
from .tree import Tree

# Create your models here.
class Park(models.Model):
    name = models.CharField(max_length=100)
    size = models.IntegerField()

    tree = models.ForeignKey(
        Tree,
        on_delete=models.CASCADE,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"The {self.type} tree is {self.height} feet tall and {self.age} years old."

