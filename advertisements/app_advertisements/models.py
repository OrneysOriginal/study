from django.db import models

class Advertisements(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField("Заголовок", max_length=128)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    auction = models.BooleanField("Торг",help_text="Отметьте, если торг уместе")
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"id={self.id},title={self.title},price={self.price}"



# Create your models here.