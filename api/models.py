from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=30)
    price=models.FloatField()
    quantity=models.IntegerField()
    description=models.TextField(blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.title