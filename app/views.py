from django.http import HttpResponse
from django.shortcuts import render

Hyderabad=["SR Nagar","Amerpet","Panjagutta","SanayathNagar","MehadhiPatnam","HytechCity","Madhapur","Jublihills"]
Bangalore=["Marthali","Tinfactory","BTM"]
Chennai=["a","b","c"]
from datetime import *

# Create your views here.
from app.models import *

def Register(request):
    return render(request,"RegistrationPage.html")


def Registerdetails(request):
    f_name=request.POST.get("t1")
    l_name=request.POST.get("t2")
    fa_name=request.POST.get("t3")
    cno=request.POST.get("t4")
    email=request.POST.get("t5")
    add=request.POST.get("t6")
    u_name=request.POST.get("t7")
    u_pass=request.POST.get("t8")
    r1=Reservation(f_name=f_name,l_name=l_name,fa_name=fa_name,cno=cno,email=email,add=add,u_name=u_name,u_pass=u_pass)
    r1.save()
    return render(request,"Schdule.html",{"msg":"Registration Completed Successfully"})


def login(request):

        return render(request,"PassengerLogin.html")



def logindetails(request):
    username = request.POST.get("u1")
    print(username)
    password = request.POST.get("u2")
    print(password)
    res = Reservation.objects.filter(u_name=username, u_pass=password)
    if not res:
        return render(request,"Home.html")
    else:
        return render(request, "Schdule.html")


def searchabhi(request):
    f_city=request.POST.get("c1")
    t_city=request.POST.get("c2")
    j_date=request.POST.get("c3")
    if f_city=="Hyderabad":
        return render(request,"Abhi.html",{"city":Hyderabad})
    elif f_city=="Bangalore":
        return render(request,"Abhi.html",{"city":Bangalore})
    else:
        return render(request,"Abhi.html",{"city":Chennai})
def searchprasad(request):
    f_city=request.POST.get("c1")
    t_city=request.POST.get("c2")
    j_date=request.POST.get("c3")
    if f_city=="Hyderabad":
        return render(request,"Prasad.html",{"city":Hyderabad})
    elif f_city=="Bangalore":
        return render(request,"Prasad.html",{"city":Bangalore})
    else:
        return render(request,"Prasad.html",{"city":Chennai})
def searchbabu(request):
    f_city=request.POST.get("c1")
    t_city=request.POST.get("c2")
    j_date=request.POST.get("c3")
    if f_city=="Hyderabad":
        return render(request,"Babu.html",{"city":Hyderabad})
    elif f_city=="Bangalore":
        return render(request,"Babu.html",{"city":Bangalore})
    else:
        return render(request,"Babu.html",{"city":Chennai})
def searchjagan(request):
    f_city=request.POST.get("c1")
    t_city=request.POST.get("c2")
    j_date=request.POST.get("c3")
    if f_city=="Hyderabad":
        return render(request,"Jagan.html",{"city":Hyderabad})
    elif f_city=="Bangalore":
        return render(request,"Jagan.html",{"city":Bangalore})
    else:
        return render(request,"Jagan.html",{"city":Chennai})

def searchtown(request):
    res=request.POST.get("b1")
    return render(request,"BusDetails.html",{"bus":res})


def pay(request):
    return render(request,"Payment.html")
def paydetails(request):
    name=request.POST.get("n1")
    c_no=request.POST.get("n2")
    cvv=request.POST.get("n3")
    amount=request.POST.get("n4")
    des=request.POST.get("n5")
    p1=payment(name=name,c_no=c_no,cvv=cvv,amount=amount,des=des)
    p1.save()
    return render(request,"Payment.html",{"msg":"Your Ticket Booked Successfully"})



def upper(request):
    return render(request,"Upper.html")


def lower(request):
    return render(request,"Lower.html")


def gentsseats(request):
    return render(request,"gents.html")


def ladiesseats(request):
    return render(request,"ladies.html")


