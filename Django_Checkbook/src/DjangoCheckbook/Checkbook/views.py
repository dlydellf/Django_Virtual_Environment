from django.shortcuts import render, redirect
from .forms import AccountForm, TransactionForm


# Create your views here.
def home(request):
    return render(request, 'checkbook/index.html')


def create_account(request):
    form = AccountForm(data=request.POST or None) # backfills the form with data from the request.POST
    if request.method == 'POST':
        if form.is_valid():
            form.save() # if the method was POST & all fields are valid, save the form
            return redirect('index') # return User to starting page
    content = {'form': form}
    return render(request, 'checkbook/CreateNewAccount.html', content) # return the form's data within the 'CreateNewAccount' page


def balance(request):
    return render(request, 'checkbook/BalanceSheet.html')


def transaction(request):
    form = TransactionForm(data=request.POST or None) # backfills the form with data from the request.POST
    if request.method == 'POST':
        if form.is_valid():
            form.save() # if the method was POST & all fields are valid, save the form
            return redirect('index') # return User to starting page
    content = {'form': form}
    return render(request, 'checkbook/AddTransaction.html', content) # return the form's data within the 'CreateNewAccount' page
