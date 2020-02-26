from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'budget'
urlpatterns = [
    path('', views.Login.as_view() , name='login'),
    path('expenses/', views.expense_item, name='expenses'),
    path('incomes/', views.income_item, name='incomes'),
    path('goals/', views.goal_item, name='goals'),
    path('goals/', views.goal_item, name='goals_per_month'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
