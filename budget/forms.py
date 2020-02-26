from django import forms
from . import models
# from django.forms import DateInput


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = models.Expense
        fields = "__all__"


class IncomeForm(forms.ModelForm):
    class Meta:
        model = models.Income
        fields = "__all__"


class GoalForm(forms.ModelForm):
    class Meta:
        model = models.Goal
        fields = "__all__"

# class MyDateWidget(DateInput):
#     input_type = 'date'
