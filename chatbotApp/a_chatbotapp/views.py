from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
import json
from .forms import ContactForm

# Views
AUTH_TOKEN = "JIRNO9328YR79IHFIJUOISDHFIW97FT89WOFYHIUSWGF"
def authenticate(token):
    if token == AUTH_TOKEN:
        return True
    else:
        return False
class AddView(View):
    def post(self, request,*args,**kwargs):
        if not authenticate(request.headers['Authorization']):
            return HttpResponse(status=403)
        num01 = float(request.POST['num01'])
        num02 = float(request.POST['num02'])
        return HttpResponse(num01+num02)

    def get(self, request):
        print(request.headers)
        if not authenticate(request.headers['Auth-Token']):
            return HttpResponse(status=403)
        num01 = float(json.loads(request.body)['num01'])
        num02 = float(json.loads(request.body)['num02'])

        print("Num01", num01)
        return HttpResponse(num01 + num02)

class SubView(View):
    def post(self, request, *args, **kwargs):
        if not authenticate(request.headers['Authentication'])


def home(request):
    return render(request, 'home.html')

def faq(request):
    return HttpResponse("FAQ")

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        phone = form.cleaned_data['phone']
        address = form.cleaned_data['address']
        print(name, email)
    form = ContactForm()
    return render(request,'form.html', {'form':form})