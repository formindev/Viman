from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    item_type = models.ForeignKey(
        "Item_type", 
        on_delete=models.SET_NULL, 
        null=True,
    )
    path = models.FileField(upload_to='video/')
    cover = models.ImageField()

    def __str__(self):
        return self.name

class Item_type(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name