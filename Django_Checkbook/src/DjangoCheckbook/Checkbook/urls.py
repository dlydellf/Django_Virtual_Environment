from django.urls import path
from . import views

urlpatterns = [ # stores the routes/paths within the project; the WHEN what's in 'views/py' gets displayed
    path('', views.home, name='index'),
    path('create/', views.create_account, name='create'),
    path('<int.pk>/balance/', views.balance, name='balance'),
    path('transaction/', views.transaction, name='transaction'),
]