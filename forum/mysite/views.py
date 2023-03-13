import datetime

from django.shortcuts import render
from django.contrib.auth.models import User
from .models import *
from django.http import HttpResponse
from .forms import UserRegistrationForm, RequestCreate
from django.core.paginator import Paginator
from django.core.files.storage import FileSystemStorage
from django.views.generic.detail import DetailView


# Create your views here.


def index(request):
    reqs = Request.objects.all()  # fetching all post objects from database
    p = Paginator(reqs, 3)
    page_obj = p.page(1)
    return render(request, "index.html", context={'page_obj':page_obj})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'registration/login.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/registration.html', {'user_form': user_form})

def requestUser(request):
    if request.method == 'POST':
        request_form = RequestCreate(request.POST, request.FILES)
        if request_form.is_valid():
            new_request = request_form.save(commit=False)
            new_request.person_id = request.user.id
            print(new_request.img)
            new_request.save()
            # new_request['user'] = request_form.users()
            # new_request.id = User.objects.filter(id__exact = request.user.id)
            return render(request, 'index.html', {'new_request': new_request})
    else:
        request_form = RequestCreate()
    return render(request, 'request_create.html', {'request_form': request_form})

def get_request(request):
    requests = Request.objects.all
    return render(request, 'registration/user_room_admin.html', context={'requests':requests})


def show_orders(request):
    requests = Request.objects.all
    return render(request, 'my_orders.html', context={'requests':requests})
# class BaseUserSet(RequestCreate):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.queryset = User.objects.filter(id__exact=self.request.user.id)

# User.get(user=self.request.user.id)