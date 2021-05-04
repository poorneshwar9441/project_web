from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .models import Items,Test
import datetime
# Create your views here.

def home_page(request,id = 1):
    """
    Landing page(start_page)

    """
    return render(request,"index.html")


def sign_in(request):
    """
    /signin

    """
    name = request.POST['fname']
    password = request.POST['password']
    cpassword = request.POST['cpassword']


    if(cpassword == password):
        t = Test(name = name,password = password)
        t.save()
        nam = str(name)
        pas = str(password)
        return HttpResponseRedirect(f"/data/{nam}/{pas}")

    else:
        return HttpResponseRedirect('')

def login_render(request):
    """
    /login
    """
    return render(request,"base.html")


def login(request):

    """
    /loggingin

    """

    
    name = request.POST['fname']
    password = request.POST['password']

    print(name,password)

    t = Test.objects.all()

    for i in t:
        if((i.name == str(name)) and (i.password == str(password))):
            nam = str(name)
            pas = str(password)
            return HttpResponseRedirect(f"/data/{nam}/{pas}")
 
    return HttpResponseRedirect("/login")


def data_render(request,name,password):
    """
    /data
    """
    nam = str(name)
    pas = str(password)

    l = []
    it = Items.objects.all()
    for i in it:
        if((i.name == nam) and (i.password == pas)):
            l.append(i)

    return render(request,"data.html",{'items':l,'name':nam,'password':pas})


def add_todo(request,name,password):
    text = ''
    text = request.POST['item']

    n1 = str(name)
    n2 = str(password)

    if((text != None) and (len(text) != 0)):
        t = Items(name = n1,password = n2,text = str(text))
        t.save()

    return HttpResponseRedirect(f'/data/{n1}/{n2}')

def delete_todo(request,name,password,id):
    t = Items.objects.filter(id = id)
    t.delete()
    n = str(name)
    p = str(password)

    return HttpResponseRedirect(f'/data/{n}/{p}')