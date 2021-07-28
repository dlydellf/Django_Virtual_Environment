from django.shortcuts import render, redirect, get_object_or_404
from .models import Account, Transaction
from .forms import AccountForm, TransactionForm


# Create your views here.
def home(request):
    form = TransactionForm(data=request.POST or None)
    if request.method == 'POST':
        pk = request.POST['account']
        return balance(request, pk)
    content = {'form': form}
    return render(request, 'checkbook/index.html', content)


def create_account(request):
    form = AccountForm(data=request.POST or None) # backfills the form with data from the request.POST
    if request.method == 'POST':
        if form.is_valid():
            form.save() # if the method was POST & all fields are valid, save the form
            return redirect('index') # return User to starting page
    content = {'form': form}
    return render(request, 'checkbook/CreateNewAccount.html', content) # return the form's data within the 'CreateNewAccount' page


def balance(request, pk):
    account = get_object_or_404(Account, pk = pk) # if account exists, get it (according to the pk)
    transactions = Transaction.Transactions.filter(account = pk) # filter ALL transactions according to the pk
    current_total = account.initial_deposit # before calculating deposits/withdrawals, assign account's current_balance to its initial deposit
    table_contents = {}
    for t in transactions: # begin updating current_total by transaction types:
        if t.type == 'Deposit':
            current_total += t.amount # ADD deposits to the current_total
            table_contents.update({t: current_total})
        else:
            current_total -= t.amount # SUBTRACT withdrawals from the current_total
            table_contents.update({t: current_total})
    content = {'account': account, 'table_contents': table_contents, 'balance' : current_total}
    return render(request, 'checkbook/BalanceSheet.html', content)


def transaction(request):
    form = TransactionForm(data=request.POST or None) # backfills the form with data from the request.POST
    if request.method == 'POST':
        if form.is_valid():
            form.save() # if the method was POST & all fields are valid, save the form
            pk = request.POST['account'] # pk == whichever account User sends via POST:
            form.save() # form is saved
            return balance(request, pk) # redirects User back to balance(), and eventually balanceSheet.html
    content = {'form': form}
    return render(request, 'checkbook/AddTransaction.html', content) # return the form's data within the 'CreateNewAccount' page
