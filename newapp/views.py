from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import RegistrationForm

def success(request):
    return render(request, 'success.html')

# Create your views here.
def getresults(request):
    props = {"goal": "2025"}
    return render(request, 'first.html', context=props)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')  # Or redirect to a success URL
        else:
            # Return form with validation errors
            return render(request, "registration/form_with_errors.html", {"form": form})    
    else:
        form = RegistrationForm()  # ✅ This line was over-indented before
        return render(request, 'registrationpage.html', {'form': form})

def dashboard_view(request):
    return render(request, 'dashboard.html')
