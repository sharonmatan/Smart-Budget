from django.shortcuts import render, redirect
from .models import Expense, Income, Goal
from .forms import ExpenseForm, IncomeForm, GoalForm
from . import forms
from django.db.models import Sum


def expense_item(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            clean = form.cleaned_data
            o = Goal()
            o.date = clean['date']
            o.amount = clean['amount']
            o.title = clean['title']
            o.category = clean['category']
            o.save()
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


def income_item(request):
    if request.method == "POST":
        form = IncomeForm(request.POST)
        if form.is_valid():
            clean = form.cleaned_data
            o = Income()
            o.date = clean['date']
            o.source = clean['source']
            o.amount = clean['amount']
            o.save()
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


def goal_item(request):
    if request.method == "POST":
        form = GoalForm(request.POST)
        if form.is_valid():
            clean = form.cleaned_data
            o = Goal()
            o.end_date = clean['end_date']
            o.amount = clean['amount']
            o.title = clean['title']
            o.save()
            return redirect('/goals/')
    else:
        form = GoalForm()
    sum_amount_expense = Expense.objects.aggregate(Sum('amount'))
    sum_amount_income = Income.objects.aggregate(Sum('amount'))
    # total = sum_amount_expense - sum_amount_income
    list_goals = Goal.objects.all()
    sum_amount_goal = Goal.objects.aggregate(Sum('amount'))

    # print(list_goals)
    # print("WTF")
    # print(type(list_goals[0]))
    # print(list_goals[0]['amount'])
    # games
    # new_list_goals = []
    # for record in list_goals:
    #     new_record = {}
    #     #for val in record:
    #         #new_record[]
    #     new_list_goals.append(new_record)

    percentage_list = []
    temp_sum_expense = sum_amount_expense['amount__sum']
    temp_sum_income = sum_amount_income['amount__sum']
    print(temp_sum_expense)
    print(temp_sum_income)
    temp_sum = temp_sum_income - temp_sum_expense
    for record in list_goals:
        if temp_sum >= record.amount:
            percentage_list.append(100)
            temp_sum = temp_sum - record.amount
        else:
            percentage_list.append(str(float(temp_sum / record.amount) * 100)[:4])
            temp_sum = 0

    # push percentage list into list goals
    for i in range(len(percentage_list)):
        list_goals[i].success_percentage = percentage_list[i]
        print(list_goals[i].success_percentage)

        # total_amount_left = sum_amount_income.amount__sum - sum_amount_expense.amount__sum
    context = {
        'sum_amount_expense': sum_amount_expense,
        'sum_amount_income': sum_amount_income,
        'list_goals': list_goals,
        'sum_amount_goal': sum_amount_goal,
        # 'total_amount_left': total_amount_left,
        'form': form
    }
    return render(request, 'budget/goals.html', context)