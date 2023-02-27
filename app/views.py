
from django.shortcuts import redirect,render
from django.contrib.auth import login,authenticate
from .forms import *
from .models import *
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required 
# Create your views here.
@login_required(login_url='login')
def home(request):
    this_user=request.user
    if(Player.objects.filter(user=this_user).exists()):
        player=Player.objects.get(user=this_user)
        return render(request,'thanks.html')

    

    if request.method == 'POST':
        questions=Ques.objects.all()
        score=0
        for i in range(questions.count()):
            print(request.POST.get('res-'+str(i)))
            if request.POST.get('res-'+str(i))==questions[i].ans:
                print("correct")
                score=score+1
            
        time= request.POST.get('timer')
        player= Player(user=this_user,score=score,time=time)
        
        player.save()

            
        return render(request,'thanks.html',{'score':score,'time':time})
    else:
        
        return render(request,'home.html',{'questions':Ques.objects.all()})
 
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
       if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
       return render(request,'login.html')
 