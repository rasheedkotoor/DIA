from django.shortcuts import render, get_object_or_404, redirect
from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
from .models import Account, PTA, STUDENT
from .forms import AccountForm

def index(request):
    return HttpResponse("Hello, You're at the account index.")


def accounts_ajax(request):
    accounts = Account.objects.all()
    data = serialize('json', accounts)
    return JsonResponse({'accounts': data}, safe=False)


def account_list(request, account_type=None):
    if account_type in [PTA, STUDENT]:
        accounts = Account.objects.filter(account_type=account_type)
    else:
        accounts = Account.objects.all()

    form = AccountForm(request.POST or None, account_type=account_type)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('account_list')
        else:
            print(form.errors)
            return redirect('account_list')
    else:
        context = {'accounts': accounts, 'form': form, 'account_type': account_type}
    return render(request, 'accounts.html', context)

def account_add(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account_list')
    else:
        form = AccountForm()
    return render(request, 'account_form.html', {'form': form})

def account_edit(request, pk):
    account = get_object_or_404(Account, pk=pk)
    if request.method == 'POST':
        form = AccountForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            return redirect('account_list')
    else:
        form = AccountForm(instance=account)
    return render(request, 'account_form.html', {'form': form})

def account_delete(request, pk):
    account = get_object_or_404(Account, pk=pk)
    if request.method == 'POST':
        account.delete()
        return redirect('account_list')
    return render(request, 'account_confirm_delete.html', {'account': account})
