from django.shortcuts import render

# Create your views here.
def cal(request):
    c=''
    try:
        if request.method=="POST":
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            Opr=request.POST.get('Opr')
            if Opr=="+":
                c=n1+n2;
            elif Opr=="-":
                c=n1-n2;
            elif Opr=="*":
                c=n1*n2;
            elif Opr=="/":
                c=n1/n2;
    except:
        c="invalid opr....."
    print(c)      





    return render(request,'calculator.html',{'c':c})