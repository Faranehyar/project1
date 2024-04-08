from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home (request) :
    #return HttpResponse('welcome to my website')
    return render(request,'home.html')

def all_products(request):
   # return HttpResponse('safheye mahsolat')
   return render(request,'products.html')

def ozviat_user(requsest):
    return HttpResponse('lotfan sabtenam konid')