from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Movement
from .forms import MovementForm

def index(request):
    return HttpResponse("Hello, You're at the leave index.")


def leave_list(request, leave_type=None):
    if leave_type == 0:
        leaves = Movement.objects.filter(user__teacher__isnull=False)
    elif leave_type == 1:
        leaves = Movement.objects.filter(user__student__isnull=False)
    else:
        leaves = Movement.objects.all()

    form = MovementForm(request.POST or None, leave_type=leave_type)
    if request.method == 'POST':
        form = MovementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('leave_list')
        else:
            print(form.errors)
            return redirect('leave_list')
    else:
        context = {'leaves': leaves, 'form': form, 'leave_type': leave_type}
        return render(request, 'leaves.html', context)

def leave_add(request):
    print(request.method, "------------------")
    if request.method == 'POST':
        form = MovementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('leave_list')
    else:
        form = MovementForm()
    return render(request, 'leave_form.html', {'form': form})

def leave_edit(request, pk):
    leave = get_object_or_404(Movement, pk=pk)
    if request.method == 'POST':
        form = MovementForm(request.POST, instance=leave)
        if form.is_valid():
            form.save()
            return redirect('leave_list')
    else:
        form = MovementForm(instance=leave)
    return render(request, 'leave_form.html', {'form': form})

def leave_delete(request, pk):
    leave = get_object_or_404(Movement, pk=pk)
    if request.method == 'POST':
        leave.delete()
        return redirect('leave_list')
    return render(request, 'leave_confirm_delete.html', {'leave': leave})
