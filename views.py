from django.shortcuts import render
from datetime import datetime
from home.models import Contact
from django.http import HttpResponse
import re
from django.template import RequestContext
from .models import InputForm
from .models import InputForm2
from .models import InputForm3
from .models import InputForm4
from .models import InputForm5
from .models import InputForm6
from .models import InputForm7
from .models import InputForm8
from .models import InputForm9
from home.compute import compute
from home.compute import compute2
from home.compute import compute3
from home.compute import compute4
from home.compute import compute5
from home.compute import compute6
from home.compute import compute7
from home.compute import compute8
from home.compute import compute9
from home.compute import compute10



import os

# Create your views here.
def index(request):
    return render(request, 'index.html')
   
def about(request):
    return render(request, 'about.html')
    
def subjects(request):
    return render(request, 'subjects.html')
    
def financial(request):
    return render(request, 'financial.html') 

def math(request):
    return render(request, 'math.html') 


# Create your views here.
def greetings(request):
    # var=request.GET['var']
    res=render(request,'basic calculator.html')
    return res

def basic_calculator(request):
    final_result=0
    values=''
    if request.method=="POST":
        values=request.POST['values'] #string having whole ques
        print(values)
        vals=re.findall(r"(\d+)",values) #extrect values
        operators=['+','x','÷','-','.','%']
        opr=[]
        for v in values:
            for o in operators:
                if v==o:
                    opr.append(o)
        print(opr)                      #extrect operators
        print(re.findall(r"(\d+)",values))

        for o in opr:
            if o=='.':
                i=opr.index(o)
                res=vals[i]+"."+vals[i+1]
                vals.remove(vals[i+1])
                opr.remove(opr[i])
                vals[i]=res
                print(vals)
                print(opr)
        for o in opr:
            if o=='%':
                i=opr.index(o)
                res=(float(vals[i])/100)*float(vals[i+1])
                vals.remove(vals[i+1])
                opr.remove(opr[i])
                vals[i]=res
                print(vals)
                print(opr)
        for o in opr:
            if o=='÷':
                i=opr.index(o)
                res=float(vals[i])/float(vals[i+1])
                vals.remove(vals[i+1])
                opr.remove(opr[i])
                vals[i]=str(res)
                print(vals)
                print(opr)
        for o in opr:
            if o=='x':
                i=opr.index(o)
                res=float(vals[i])*float(vals[i+1])
                vals.remove(vals[i+1])
                opr.remove(opr[i])
                vals[i]=str(res)
                print(vals)
                print(opr)
        for o in opr:
            if o=='+':
                i=opr.index(o)
                res=float(vals[i])+float(vals[i+1])
                vals.remove(vals[i+1])
                opr.remove(opr[i])
                vals[i]=str(res)
                print(vals)
                print(opr)
            if o=='-':
                i=opr.index(o)
                res=float(vals[i])-float(vals[i+1])
                vals.remove(vals[i+1])
                opr.remove(opr[i])
                vals[i]=str(res)
                print(vals)
                print(opr)

        # for o in opr:
        #     if o=='-':
        #         i=opr.index(o)
        #         res=int(vals[i])-int(vals[i+1])
        #         vals.remove(vals[i+1])
        #         opr.remove(opr[i])
        #         vals[i]=str(res)
        #         print(vals)
        #         print(opr)

        # print(opr)
        if len(opr)!=0:
            if opr[0]=='÷':
                result = float(vals[0])/float(vals[1])
            elif opr[0]=='x':
                result = float(vals[0])*float(vals[1])
            elif opr[0]=='+':
                result = float(vals[0])+float(vals[1])
            else :
                result = float(vals[0])-float(vals[1])
        else:
            result = float(vals[0])

        final_result=round(result,2)
        print(final_result)
        # result = int(vals[0])+int(vals[1])

        # i=0
        # res=int(vals[i])
        # for operator in values:
        #     if not operator.isdigit():
        #         # print(type(int(vals[1])))
        #         # print(value)
        #         if operator=='+':
        #             res=res+int(vals[i+1])
        #         i=i+1
    res=render(request,'basic calculator.html',{'result':final_result,'values':values})
    return res
  
    
def physics(request):
    return render(request, 'physics.html') 
  
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
    return render(request, 'contact.html')

def distance (request):
    os.chdir(os.path.dirname(__file__))
    result = None
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            form2 = form.save(commit=False)
            result = compute(float(form2.u) *form2.Uunit, float(form2.t)*form2.Tunit, float(form2.a)*form2.Aunit)
            
    else:
        form = InputForm()
    context = {'form': form,
             'result': result,
              }
    return render(request, 'distance.html', context)

def velocity(request):
    os.chdir(os.path.dirname(__file__))
    result = None
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            form2 = form.save(commit=False)
            result = compute(float(form2.u) *form2.Uunit, float(form2.t)*form2.Tunit, float(form2.a)*form2.Aunit)
            form3 =(form2.Uunit,form2.Tunit,form2.Aunit)   
    else:
        form = InputForm()
    context = {'form': form,
             'result': result,
             }
    return render(request, 'velocity.html', context)

def current(request):
    os.chdir(os.path.dirname(__file__))
    result = None
    if request.method == 'POST':
        form = InputForm2(request.POST)
        if form.is_valid():
            form2 = form.save(commit=False)
            result = compute3(float(form2.q)*form2.Qunit, float(form2.t)*form2.Tunit)
            
    else:
        form = InputForm2()
    context = {'form': form,
             'result': result,
             }
    return render(request, 'current.html', context)

def equation(request):
    os.chdir(os.path.dirname(__file__))
    result = None
    if request.method == 'POST':
        form = InputForm3(request.POST)
        if form.is_valid():
            form2 = form.save(commit=False)
            result = compute4(form2.u, form2.a, form2.s)
            
    else:
        form = InputForm3()
    context = {'form': form,
             'result': result,
             }
    return render(request, 'equation.html', context) 

def escapevelocity(request):
    os.chdir(os.path.dirname(__file__))
    result = None
    if request.method == 'POST':
        form = InputForm4(request.POST)
        if form.is_valid():
            form2 = form.save(commit=False)
            result = compute5(float(form2.m)*form2.Munit, float(form2.r)*form2.Runit)
            
    else:
        form = InputForm4()
    context = {'form': form,
             'result': result,
             }
    return render(request, 'escapevelocity.html', context)

def force(request):
    os.chdir(os.path.dirname(__file__))
    result = None
    if request.method == 'POST':
        form = InputForm5(request.POST)
        if form.is_valid():
            form2 = form.save(commit=False)
            result = compute6(float(form2.m)*form2.Munit, float(form2.a)*form2.Aunit)
            
    else:
        form = InputForm5()
    context = {'form': form,
             'result': result,
              }
    return render(request, 'force.html', context)

def gravitationforce(request):
    os.chdir(os.path.dirname(__file__))
    result = None
    if request.method == 'POST':
        form = InputForm6(request.POST)
        if form.is_valid():
            form2 = form.save(commit=False)
            result = compute7(float(form2.m1)*form2.M1unit, float(form2.m2)*form2.M2unit, float(form2.r)*form2.Runit)
            
    else:
        form = InputForm6()
    context = {'form': form,
             'result': result,
             }
    return render(request, 'gravitationforce.html', context)

def gravitationg(request):
    os.chdir(os.path.dirname(__file__))
    result = None
    if request.method == 'POST':
        form = InputForm7(request.POST)
        if form.is_valid():
            form2 = form.save(commit=False)
            result = compute8(float(form2.m)*form2.Munit, float(form2.r)*form2.Runit)
            
    else:
        form = InputForm7()
    context = {'form': form,
             'result': result,
             }
    return render(request, 'gravitationg.html', context)

def kineticenergy(request):
    os.chdir(os.path.dirname(__file__))
    result = None
    if request.method == 'POST':
        form = InputForm8(request.POST)
        if form.is_valid():
            form2 = form.save(commit=False)
            result = compute9(float(form2.m)*form2.munit, float(form2.v)*form2.vunit)
            
    else:
        form = InputForm8()
    context = {'form': form,
             'result': result,
             }
    return render(request, 'kineticenergy.html', context) 

def potentialenergy(request):
    os.chdir(os.path.dirname(__file__))
    result = None
    if request.method == 'POST':
        form = InputForm9(request.POST)
        if form.is_valid():
            form2 = form.save(commit=False)
            result = compute10(float(form2.m)*form2.Munit, float(form2.h)*form2.Hunit)
            
    else:
        form = InputForm9()
    context = {'form': form,
             'result': result,
             }
    return render(request, 'potentialenergy.html', context)

  
