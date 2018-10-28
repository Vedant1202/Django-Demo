from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord
from first_app import forms

# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}

    # my_dict = {'INSERT_TEXT': 'This is views.py'}
    return render(request, 'first_app/index.html', context=date_dict)


def form(request):
    form  = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("VALIDATION SUCCESS!")
            print("The entered data is: ")
            print("Name: ", form.cleaned_data['name'])
            print("Email: ", form.cleaned_data['email'])
            print("Text: ", form.cleaned_data['text'])

    return render(request, 'first_app/form.html', {'form': form})


def first_app(request):
    return HttpResponse("This is the url of First app")
