# -*- encoding: utf-8 -*-


# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm
from .models import PatientPerscription


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created successfully.'
            success = True

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})


def add(request):
    dic={}

    if request.method =="POST":
            uname = request.POST.get("uname")
            fname =request.POST.get("fname")
            lname = request.POST.get("lname")
            dob = request.POST.get("dob")
            gen = request.POST.get("gender")
            mail = request.POST.get("email")
            hospital = request.POST.get("hospital")
            dname = request.POST.get("dname")
            dd = request.POST.get("dd")
            df = request.POST.get("df")
            PrescriptionD = request.POST.get("PrescriptionD")
            PrescriptionDur = request.POST.get("PrescriptionDur")
            exdate = request.POST.get("exdate")
            mname =request.POST.get("mname")
            strength = request.POST.get("strength")
            instruction = request.POST.get("instruction")
            admit = request.POST.get("admit")
            admitdate = request.POST.get("admitdate")
            dischargeDate  = request.POST.get("dischargeDate")
            instruction1= request.POST.get("instruction1")
            Operation = request.POST.get("operation")
            operationDate = request.POST.get("operationDate")
            surgeon = request.POST.get("surgeon")
            operationDetails = request.POST.get("operationDetails")

            obj= PatientPerscription()
            stat = obj.addnewprescription(uname,fname,lname,dob,mail,gen,hospital,dname,dd,df,PrescriptionD,PrescriptionDur,exdate,mname,strength,instruction,admit,admitdate,dischargeDate,instruction1,Operation,operationDate,surgeon,operationDetails);
            dic=stat;

    return render(request, "addDetails.html/",dic)

def addDetails(request):
    return render(request, "addDetails.html")