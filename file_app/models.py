from django.db import models

class File(models.Model):
    FRUIT = "fruit"
    LEAF = "leaf"
    TYPE_CHOICES = [(FRUIT, "Fruit"), (LEAF, "Leaf")]
    file = models.FileField(blank=False, null=False)
    type = models.CharField(
        max_length=5, choices=TYPE_CHOICES, default="fruit", null=False
    )
    name = models.CharField(max_length=20, default="none", null=False)
    timestamp = models.DateTimeField(auto_now_add=True)
