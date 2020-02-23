from django.urls import path
from . import views

app_name = 'budget'
urlpatterns = [
    path('expenses/', views.expense_item, name='expenses'),
    path('incomes/', views.income_item, name='incomes'),
    path('goals/', views.goal_item, name='goals'),
]
