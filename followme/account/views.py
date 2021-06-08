from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def registration(request):
    data = {}
    if request.method() == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            data['form'] = form
            data['res'] = 'success'
            return render(request, 'templates/registration.html', data)
        else:
            form = UserCreationForm()
            data['form'] = form
            return render(request, 'pages/registration.html', data)
