from django.db import models


class Expense(models.Model):
    date = models.DateField()
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    title = models.CharField(max_length=300)
    category = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.pk} {self.date} {self.title} {self.amount} {self.category}"


class Income(models.Model):
    date = models.DateField()
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    source = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.pk} {self.date} {self.amount} {self.source}"


class Goal(models.Model):
    end_date = models.DateField()
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    title = models.CharField(max_length=200)
    success_percentage = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.end_date} {self.title} {self.amount} {self.success_percentage}"