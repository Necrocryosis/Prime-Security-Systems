from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Home(request):
    
    return render(request,'Crypto\html\page.html')

def generated(request):
    code = request.POST['sms_code']
    key = request.POST['p_key']
    code= int(code)
    

    key=list(map(int,key.split('-')))
    output=pow(code,key[0],key[1])
    print("output: ",output)

    param = {
    'otp' : output
    }


    return render(request,'Crypto\html\page2.html',param)

