from django.shortcuts import render
from .forms import InterestCalculationForm

def calculate_interest(request):
    if request.method == 'POST':
        form = InterestCalculationForm(request.POST)
        if form.is_valid():
            calculation = form.save()
            interest = calculation.calculate_interest()
            return render(request, 'result.html', {'interest': interest})
    else:
        form = InterestCalculationForm()
    return render(request, 'index.html', {'form': form})