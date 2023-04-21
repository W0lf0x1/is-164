from django.shortcuts import render
from django.http import HttpResponse
import random
def home(request):

    return render(request, 'home.html')

def password(request):
    caracters = list('qwertyuiopasdfghjklzxcvbnm')
    if request.GET.get('number'):
        caracters.extend(list('1234567890'))
    if request.GET.get('uppercase'):
        caracters.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))
    if request.GET.get('special'):
        caracters.extend(list('!@#$%^&*=-'))

    lenght = int(request.GET.get('legnt',10))

    thepassword = ''
    for x in range(lenght):
        thepassword += random.choice(caracters)

    return render(request, 'password.html', {'thepassword':thepassword})

    return render(request, 'password.html')

def about(request):
    return render(request, 'about.html')

