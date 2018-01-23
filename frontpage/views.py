from django.shortcuts import render
from main.models import User
# Create your views here.


def index(request):
    terve = User.terve(request)
    context = {'terve' : terve}
    return render(request, 'frontpage/index.html', context)
