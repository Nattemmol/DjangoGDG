from django.shortcuts import get_object_or_404, redirect, render
from .models import Loan
from .forms import LoanForm

def loan_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
        loans = Loan.objects.filter(name__icontains=search_query)
    else:
        loans = Loan.objects.all()
    total_outstanding = sum(loan.amount for loan in loans)
    return render(request, 'loans/loan_list.html', {'loans': loans, 'total_outstanding': total_outstanding})


def loan_form(request, id=None):
    if id:
        loan = get_object_or_404(Loan, id=id)
    else:
        loan = None
    if request.method == 'POST':
        form = LoanForm(request.POST, instance=loan)
        if form.is_valid():
            form.save()
            return redirect('loan_list')
    else:
        form = LoanForm(instance=loan)
    return render(request, 'loans/loan_form.html', {'form': form})

def loan_delete(request, id):
    loan = get_object_or_404(Loan, id=id)
    if request.method == 'POST':
        loan.delete()
        return redirect('loan_list')
    return render(request, 'loans/loan_delete.html', {'loan': loan})

def home(request):
    return render(request, 'base.html')
