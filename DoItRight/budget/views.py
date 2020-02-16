from django.shortcuts import render
from django.http import HttpResponse
from .models import Expense


def expense_item(request):
    list_expense = Expense.objects.all()
    context = {
        'list_expense': list_expense,
    }
    return render(request, 'budget/expenses.json', context)