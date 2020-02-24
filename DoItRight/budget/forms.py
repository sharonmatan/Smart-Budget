from django import forms
from django.forms import DateInput
from . import models


class ExpenseForm(forms.Form):
    date = forms.DateField()
    title = forms.CharField(max_length=300)
    amount = forms.DecimalField(decimal_places=2, max_digits=12)
    category = forms.CharField(max_length=200)


class IncomeForm(forms.Form):
    date = forms.DateField()
    source = forms.CharField(max_length=200)
    amount = forms.DecimalField(decimal_places=2, max_digits=12)


class MyDateWidget(DateInput):
    input_type = 'date'


class GoalForm(forms.ModelForm):
    class Meta:
        model = models.Goal
        fields = "__all__"