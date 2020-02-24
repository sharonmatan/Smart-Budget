from django.db import models


class Expense(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=300)
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    category = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.pk} {self.date} {self.title} {self.amount} {self.category}"


class Income(models.Model):
    date = models.DateField()
    source = models.CharField(max_length=200)
    amount = models.DecimalField(decimal_places=2, max_digits=12)

    def __str__(self):
        return f"{self.pk} {self.date} {self.amount} {self.source}"


class Goal(models.Model):
    priority = models.IntegerField(default=10)
    end_date = models.DateField()
    title = models.CharField(max_length=200)
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    success_percentage = models.DecimalField(decimal_places=2, max_digits=12, null=True, blank=True, editable=False)

    def __str__(self):
        return f"{self.end_date} {self.title} {self.amount} {self.success_percentage} {self.priority}"
