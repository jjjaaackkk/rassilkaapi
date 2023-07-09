from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

from core.stats import (
    get_stats_from_camps, get_stats_from_msgs
)
from core.models import (
    Campaign, Customer, MSG
)
from .pagination import paginate_items


def login_page(req):
    return render(req, "login.html")

def get_login(req):

    if req.method == 'POST':
        usr = req.POST.get('usr', '')
        passwd = req.POST.get('pass', '')

        user = authenticate(username=usr, password=passwd)

        if user:
            login(req, user)
            return redirect('/')
        
    data = {
        'error': 'Ошибка Авторизации!',
    }
    
    return render(req, 'login.html', data)

@login_required(login_url='/login')
def index(req):
    data = {
        'base': 'account',
    }
    return render(req, 'index.html', data)

@login_required(login_url='/login')
def get_panel(req):

    camps = Campaign.objects.all()
    camp_stats = get_stats_from_camps(camps)

    customers = Customer.objects.all()
    msgs = MSG.objects.all()
    msg_stats = get_stats_from_msgs(msgs)

    data = {
        'base': 'panel',
        'total_customers': customers.count(),
        'camps_stats': camp_stats,
        'msg': msg_stats,
        }

    return render(req, "index.html", data)

@login_required(login_url='/login')
def get_campaigns(req, page = 1):

    camps = Campaign.objects.all()
    camps = paginate_items(camps, page)

    data = {
        'base': 'campaigns',
        'camps': camps['items'],
        'prev_page': (page - 1),
        'current_page': page,
        'next_page': (page + 1),
        'last_page': camps['pages'],
    }

    return render(req, "index.html", data)

@login_required(login_url='/login')
def get_customers(req, page = 1):

    customers = Customer.objects.all()
    customers = paginate_items(customers, page)

    data = {
        'base': 'customers',
        'customers': customers['items'],
        'prev_page': (page - 1),
        'current_page': page,
        'next_page': (page + 1),
        'last_page': customers['pages'],
    }

    return render(req, "index.html", data)

@login_required(login_url='/login')
def get_messages(req):

    data = {
        'base': 'messages',
    }

    return render(req, "index.html", data)

@login_required(login_url='/login')
def get_settings(req):

    data = {
        'base': 'settings',
    }

    return render(req, "index.html", data)
    