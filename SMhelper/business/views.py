from django.shortcuts import render
from .models import CompanyPages
from .models import ReviewsBlocks
from .models import Contacts
from .forms import FormModalForm
from .forms import ReviewsBlockForm
from django.contrib.auth.hashers import make_password


def page(request, contentCompany=CompanyPages.objects.all(), nameuser=ReviewsBlocks.objects.all(), reviews=ReviewsBlocks.objects.all()):
    if request.method == 'POST':
        forms = FormModalForm(request.POST)
        if forms.is_valid():
            forms.save()
    forms = FormModalForm()
    if request.method == "POST":
        form = ReviewsBlockForm(request.POST)
        if form.is_valid():
            form.save()
    form = ReviewsBlockForm()
    return render(request, "business/page.html", {'contentCompany' : contentCompany, 'nameuser' : nameuser, 'reviews' : reviews, 'form' : form, 'forms' : forms})


def pageserv(request):
    errors = ''
    if request.method == 'POST':
        forms = FormModalForm(request.POST)
        if forms.is_valid():
            forms.save()
        else:
            errors = 'Форма была запонена неверно'
    forms = FormModalForm()
    return render(request, "business/pageserv.html", {'forms' : forms, 'errors' : errors})


def pagefaq(request):
    errors = ''
    if request.method == 'POST':
        forms = FormModalForm(request.POST)
        if forms.is_valid():
            forms.save()
        else:
            errors = 'Форма была запонена неверно'
    forms = FormModalForm()
    return render(request, "business/pagesfaq.html", {'forms' : forms, 'errors' : errors})


def basic(request):
    return render(request, 'business/basic.html')



