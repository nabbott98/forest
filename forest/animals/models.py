from django.db import models

# Create your models here.
class Animal(models.Model):
    type = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    age = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Meet {self.name} the {self.type} that is {self.color} and {self.age} years old."


#Example JSON
# {
#     "type": "Grizzly",
#     "name": "Nick",
#     "color": "Brown",
#     "age": 10
# }
