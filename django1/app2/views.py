from django.shortcuts import render

def home(request):

    factorials = {}

  
    for n in range(1, 9):
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        factorials[n] = factorial


    return render(request, 'app2/index.html', {'factorials': factorials})
