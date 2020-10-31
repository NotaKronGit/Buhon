from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Organization


# Create your views here.
@login_required(login_url='/login/')
def organization_menu(request):
    menu = {'items': {
        'Список организации': 'organization_list',
        'Список работников': 'employee_list',
        'Список должностей': 'reports',
        'На главную': '/'
    }
    }

    return render(request, 'mainmenu.html', menu)


@login_required(login_url='/login/')
def organization_list(request):
    organizations = Organization.objects.all()
    menu = {'items': {
        'Добавить организацию': 'organization_create',
        'Поиск организации': 'organization_filter',
        'Назад': '/organization',
    },
        'body_content': organizations
    }

    return render(request, 'organization_list.html', menu)
