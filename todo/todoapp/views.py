
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db.models import Q
from todoapp.models import Task,Course
from todoapp.form import EmpRegister,CourseForm,RegisterForm
from django.views import View
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):

    #return HttpResponse('Hello Home Page')
    #return redirect('/contact')
    #return render(request,'home.html')
    #d={'id':15,'name':'ITvedant','rno':35}
    #return render(request,'home.html',d)
    print("Views is excuted")
    return HttpResponse("Hello from home....view executed")


def product(request):

    #data="Hello from Product"
    #return HttpResponse(data)
    return render(request,'product.html')

def contact(request):
    #data="<h1>Hello from Contact Page</h1>"
    #return HttpResponse(data)
    return render(request,'contact.html')


def evenodd(request,n):
        r=int(n)%2
        d={'res,':r}
        return render(request,'home.html',d)
        

def loop(request):
    d={
        'l':[10,20,30,40,50,60]
    }

    return render(request,'home.html',d)
        
def index(request):
    content={}
    #content['data']=Task.objects.all()
    #print(content['data'])
    user_id=request.user.id
    Q1=Q(is_deleted='N')
    Q2=Q(uid=user_id)
    content['data']=Task.objects.filter(Q1&Q2)
    return render(request,'index.html',content)


       
def about(request):

    return render(request,'about.html')

def create_task(request):

    if request.method=='POST':
        t=request.POST['t']
        det=request.POST['det']
        dt=request.POST['dt']
        user_id=request.user.id
        #print(t)
        #print(det)
        #print(dt)
        t1=Task.objects.create(title=t,detail=det,date=dt,uid=user_id,is_deleted='N')
        #print(t1)
        t1.save()
        return redirect('/')
    

    else:
     return render(request,'create_task.html')

def delete(request,rid):
    '''
    hard delete
    x=Task.objects.get(id=rid)
    x.delete()
    return redirect('/')
    '''

    x=Task.objects.filter(id=rid)
    x.update(is_deleted='Y')
    return redirect('/')

def edit(request,rid):

    if request.POST=='POST':
        ut=request.POST['t']
        udet=request.POST['det']
        udt=request.POST['dt']
        #print(ut)
        #print(udet)
        #print(udt)
        x=Task.objects.filter(id=rid)
        x.update(title=ut,detail=udet,date=udt)
        return redirect('/')

    else:
        content={}
        content['data']=Task.objects.filter(id=rid)
        return render(request,'editform.html',content)


def cdashboard(request):
    content={}
    #content['data']=Course.objects.all()
    #content['data']=Course.cobj.all() #changing default manager
    #content['data']=Course.ccustomobj.all() # custom class object
    #content['data']=Course.objects.filter(ccat="Developement")
    #content['data']=Course.objects.filter(ccat="Data Science")
    #>= django: columnname__gt=value or member__gt=value
    #content['data']=Course.objects.filter(cprice__gt=20000)
    #content['data']=Course.objects.filter(cprice__gte=20000)
    #content['data']=Course.objects.filter(cprice__lt=20000)
    #content['data']=Course.objects.filter(cprice__lte=20000)
    #content['data']=Course.objects.filter(ccat='Data Science',cprice__gte=20000)


    #Q1=Q(ccat='Data Science')
    #Q2=Q(cprice__gte=20000)


    '''
    Q1=Q(cdur=40)
    Q2=Q(cdur=50)
    Q3=Q(cdur=20)

    content['data']=Course.objects.filter(Q1|Q2|Q3)
    '''

    #Sorting order by
    #content['data']=Course.objects.order_by('cdur')
    #content['data']=Course.objects.order_by('-cdur')
    #content['data']=Course.objects.order_by('cprice')
    #content['data']=Course.objects.order_by('-cprice')


    #filter and sorting both together
    #content['data']=Course.objects.order_by('cprice').filter(ccat="Data Science")

    #content['data']=Course.ccustomobj.sortfeeshightolowdev()
    #content['data']=Course.ccustomobj.sortfeeslowtohighdev()
    #content['data']=Course.ccustomobj.sortfeeshightolowds()
    content['data']=Course.ccustomobj.sortfeeslowtohighds()

    return render(request,'dashboard.html',content)


def lowtohigh(request):
    content={}
    content['data']=Course.objects.order_by('cprice')
    return render(request,'dashboard.html',content)



def hightolow(request):
    content={}
    content['data']=Course.objects.order_by('-cprice')
    return render(request,'dashboard.html',content)

def asending(request):
    content={}
    content['data']=Course.objects.order_by('cdur')
    return render(request,'dashboard.html',content)



def desending(request):
    content={}
    content['data']=Course.objects.order_by('-cdur')
    return render(request,'dashboard.html',content)


def showform(request):

    fobj=EmpRegister()
    content={}
    content['Form']=fobj

    return render(request,'empregister.html',content)


def showmodelform(request):
    mfobj=CourseForm()
    content={}
    content['form']=mfobj

    return render(request,'createcourse.html',content)


class MyView(View):

    def get(self,request):

        return HttpResponse("Hello From MyView With Get Request")


    def post(self,request):
        cname=request.POST['course_name']
        cdur=request.POST['course_duration']
        ccat=request.POST['course_category']
        cfees=request.POST['course_fees']
        print(cname)
        print(cdur)
        print(ccat)
        print(cfees)

        return HttpResponse("Hello From MyView With Post Request")
'''
def register(request):

    if request.method=='POST':
        uname=request.POST['username']
        pass1=request.POST['password1']
        #print(uname)
        #print(pass1)
        u1=User(username=uname,password=pass1,is_staff=True,is_active=True)
        u1.save()
        return redirect('/register')

    else:
        fm=UserCreationForm()
        return render(request,'signup.html',{'form':fm})
        
        '''
'''
def register(request):

    if request.method=='POST':
       
       fm=UserCreationForm(request.POST)
       #print(fm)
       print(fm.is_valid())
       if fm.is_valid():
            fm.save()
            return redirect('/register')

    else:
        fm=UserCreationForm()
        return render(request,'signup.html',{'form':fm})

'''

def register(request):

    if request.method=='POST':
       
       fm=RegisterForm(request.POST)
       #print(fm)
       #print(fm.is_valid())
       if fm.is_valid():
            messages.success(request,'Account created Successfully,Please login!!!')
            fm.save()
            return redirect('/register')

    else:
        fm=RegisterForm()
        return render(request,'signup.html',{'form':fm})


def user_login(request):
    if request.method=="POST":
        fm=AuthenticationForm(request=request,data=request.POST)
        #print(fm)
        #print(fm.is_valid())
        if fm.is_valid():
            
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            #print(uname)
            #print(upass)
            u=authenticate(username=uname,password=upass)
            #print(u)
            if u:
                login(request,u)

                return redirect('/')

        #return HttpResponse('In Post Section')
        
    else:
        fm=AuthenticationForm()


        return render(request,'login.html',{'form':fm})

def user_logout(request):
    logout(request)

    return redirect('/login')

def setcookie(request):
    r=render(request,'setcookie.html')
    r.set_cookie('name','ITvedant')
    #r.set_cookie('name','EClass ITvedant',max_age=120)
    return r

def getcookie(request):
    #d=request.COOKIES['name']
    #d=request.COOKIES.get('name')
    d=request.COOKIES.get('name','Hello Guest')
    return render(request,'getcookie.html',{'data':d})

def setsession(request):
    request.session['user']="ITVEDANT USER"
    return render (request,'setsession.html')


def getsession(request):
    d=request.session['user']

    return render(request,'getsession.html',{'data':d})


def del_session(request):
    if 'user' in request.session:

        del request.session['user']
        return HttpResponse("session deleted!!!")


def getloggeduserid(request):
    user_id=request.user.id
    return render(request,'getsession.html',{'data':user_id})






