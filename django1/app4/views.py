from django.shortcuts import render


def home(request):
    factorial=1
    n1=5
    for i in range(1,n1+1,1):
        factorial=factorial*i
    return render(request,'app4/index.html',{'param1':factorial,'param2':n1})

