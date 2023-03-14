from django.shortcuts import render,redirect,HttpResponseRedirect
from .models import Fruits,Contact
from django.contrib import messages
from .forms import ContactForm,creatuser,userlogin,FruitForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout

#admin view
def admin(request):
    if request.method=="POST":
        form = FruitForm(request.POST)
        if form.is_valid():
            n=form.cleaned_data['Name']
            nu=form.cleaned_data['about']
            
            con=Fruits(name=n,about=nu)
            con.save()
            messages.success(request,"We will call you........")
            return HttpResponseRedirect('super')
    else:
         fm= FruitForm()
    data=Fruits.objects.all()
    return render(request,"admin.html",{'form':fm,'data':data})

#user creating view
def createuser(request):
    if request.method =="POST":
            userfm=creatuser(request.POST)
            if userfm.is_valid():
                messages.success(request,"Account Created successfull........")
                userfm.save()
                return redirect('login')
    else:
        userfm=creatuser()
    return render(request,"sign.html",{'form':userfm})
#login views
def user_log(request):
    if request.method=="POST":
       
            fm=userlogin(request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass=fm.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    return redirect("home")
                else:
                    fm.add_error(None, "Invalid  username or password")

    else:
        fm=userlogin()
    return render(request,"login.html",{'form':fm})

#home view 
def home(request):
    
    return render(request,"index.html")
#contact views
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            n=form.cleaned_data['Name']
            nu=form.cleaned_data['Phonumber']
            e=form.cleaned_data['Email']
            m=form.cleaned_data['Message']
            con=Contact(name=n,number=nu,email=e,message=m)
            con.save()
            messages.success(request,"We will call you........")
            return HttpResponseRedirect('contact')
    else:
        form = ContactForm()
    
    contact_data = Contact.objects.all()
    return render(request, 'contact.html', {'form': form, 'contact_data': contact_data})
    
 #fruiets view             
def fruit(request):
    if request.method =="POST":
        userfm=FruitForm(request.POST)
        if userfm.is_valid():
                messages.success(request,"Account Created successfull........")
                userfm.save()
                return redirect('login')
    else:
        userfm=FruitForm()
    data=Fruits.objects.all()
    return render(request,"fruit.html", {'n':data,'form':userfm})
    
  #service view  
def service(request):
    data=Fruits.objects.all()
    return render(request,"service.html",{'n':data,})

#order view
def orders(request):
    data=Fruits.objects.all()
    return render(request,"orders.html",{'n':data,})
