from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Expense, Income, Goal
from .forms import ExpenseForm, IncomeForm, GoalForm
from . import forms
from django.db.models import Sum
from django.urls import reverse


class Login(LoginView):
    form_class = AuthenticationForm

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(reverse('budget:expenses'))


def year_and_month(month, year):
    expenses = Expense.objects.all()
    incomes = Income.objects.all()
    goals = Goal.objects.order_by("priority")

    if year:
        expenses = expenses.filter(date__year=int(year))
        incomes = incomes.filter(date__year=int(year))
        goals = goals.filter(end_date__year=int(year))

    if month:
        expenses = expenses.filter(date__month=int(month))
        incomes = incomes.filter(date__month=int(month))
        goals = goals.filter(end_date__month=int(month))
    return expenses, incomes, goals


@login_required
def expense_item(request):
    if request.method == "POST":
        print(request.POST.get('action'))
        if request.POST.get('action') == 'delete':
            Expense.objects.get(id=int(request.POST['expense'])).delete()
            return redirect('/expenses/')
        form = ExpenseForm(request.POST)
        if form.is_valid():
            o = form.save()
            return redirect('/expenses/')
    else:
        form = ExpenseForm()
    list_expenses = Expense.objects.all()
    sum_amount_expense = Expense.objects.aggregate(Sum('amount'))
    context = {
        'list_expenses': list_expenses,
        'sum_amount_expense': sum_amount_expense,
        'form': form
    }
    return render(request, 'budget/expenses.html', context)


@login_required
def income_item(request):
    if request.method == "POST":
        print(request.POST.get('action'))
        if request.POST.get('action') == 'delete':
            Income.objects.get(id=int(request.POST['income'])).delete()
            return redirect('/incomes/')
        form = IncomeForm(request.POST)
        if form.is_valid():
            o = form.save()
            return redirect('/incomes/')
    else:
        form = IncomeForm()
    list_incomes = Income.objects.all()
    sum_amount_income = Income.objects.aggregate(Sum('amount'))
    context = {
        'list_incomes': list_incomes,
        'sum_amount_income': sum_amount_income,
        'form': form
    }
    return render(request, 'budget/incomes.html', context)


@login_required
def goal_item(request):
    if request.method == "POST":
        if request.POST.get('action') == 'delete':
            Goal.objects.get(id=int(request.POST['goal'])).delete()
        form = GoalForm(request.POST)
        if form.is_valid():
            o = form.save()
            return redirect('/goals/')
    else:
        form = GoalForm()
    year = request.GET.get('year')
    month = request.GET.get('month')
    expenses, incomes, goals = year_and_month(month, year)

    sum_amount_expense = expenses.aggregate(Sum('amount'))
    sum_amount_income = incomes.aggregate(Sum('amount'))
    sum_amount_goal = goals.aggregate(Sum('amount'))

    temp_sum_expense = sum_amount_expense['amount__sum'] or 0
    temp_sum_income = sum_amount_income['amount__sum'] or 0
    temp_sum = temp_sum_income - temp_sum_expense
    percentage_list = []

    for record in goals:
        if temp_sum >= record.amount:
            percentage_list.append(100)
            temp_sum = temp_sum - record.amount
        else:
            percentage_list.append(str(float(temp_sum / record.amount) * 100)[:4])
            temp_sum = 0

    for i in range(len(percentage_list)):
        goals[i].success_percentage = percentage_list[i]

    context = {
        'sum_amount_expense': sum_amount_expense,
        'sum_amount_income': sum_amount_income,
        'list_goals': goals,
        'sum_amount_goal': sum_amount_goal,
        'form': form,
    }
    return render(request, 'budget/goals.html', context)
