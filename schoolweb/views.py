from django.shortcuts import redirect, render
from .models import Staf,Course,Modul,Event,News,Comment,Faq,Opinion,Statistics
from django.contrib import messages
# Create your views here.

def notfound(request):
    return render(request,'404.html')

def index(request):
    course = Course.objects.all()
    statistics = Statistics.objects.all()[0]
    events = Event.objects.all()[0:3]
    news = News.objects.all().order_by('time')[:3]
    opinions = Opinion.objects.filter(checked = True).order_by('time')[:3]
    teachers = Staf.objects.filter(user_type = Staf.TEACHER)[:6]
    faq = Faq.objects.all()[:3]
    context = {
        'courses' : course,
        'statistics' : statistics,
        'events' : events,
        'news' : news,
        'opinions' : opinions,
        'faq' : faq,
        'teachers':teachers
    }
    return render(request,'index.html',context)

def course_details(request,id):
    try:
        course = Course.objects.get(id=id)
        courses = Course.objects.all().order_by('?')[:3]
        teachers = Staf.objects.filter(user_type = Staf.TEACHER)[:6]
        
        context = {
            'course':course,
            'courses':courses,
            'teachers':teachers
        }

        return render(request,'course-details.html',context=context)
    except:
        return redirect('notfound')

def about_us(request):
    teachers = Staf.objects.filter(user_type = Staf.TEACHER)
    events = Event.objects.all()
    statistics = Statistics.objects.all()[0]
    context = {
        'teachers':teachers,
        'events':events,
        'statistics':statistics
    }
    return render(request,'about.html',context)

def events(request):
    events = Event.objects.all()
    course = Course.objects.filter(cost = 0)
    return render(request,'event.html',{'events':events,'courses':course})

def event_details(request,id):
    try:
        event = Event.objects.get(id=id)
        more_events = Event.objects.all().order_by('?')[:3]
        context = {
            "event":event,
            "more_events":more_events
        }
        return render(request,'event-details.html',context)
    except:
        return redirect('notfound')

def teachers(request):
    teachers = Staf.objects.filter(user_type__in = [Staf.TEACHER,Staf.DIRECTOR])
    events = Event.objects.all()[:3]
    return render(request,'our-teacher.html',{'teachers':teachers,'events':events})

def heads(request):
    return render(request,'heads.html')

def staf_details(request,id):
    try:
        staf = Staf.objects.get(id=id)
        teachers = Staf.objects.all()
        return render(request,'teacher-profile.html',{'staf':staf,'teachers':teachers})
    except:
        return redirect('notfound')

def faq(request):
    faqs = Faq.objects.all()
    return render(request,'faq.html',{'faqs':faqs})

def news(request):
    news = News.objects.all().order_by('-id')
    course = Course.objects.all().order_by('-id')
    teachers = Staf.objects.filter(user_type=Staf.TEACHER)
    events = Event.objects.all().order_by('-id')
    return render(request,'blog.html',{'news':news,'teachers':teachers,'course':course,'events':events})

def news_details(request,id):
    try:
        news = News.objects.get(id=id)
        comments = Comment.objects.filter(news = news).order_by('-id')
        count = Comment.objects.all().count()
        return render(request,'blog-details.html',{'news':news,'comments':comments,'count':count})
    except:
        return redirect('notfound')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        last_name = request.POST.get('last_name')
        message = request.POST.get('message')
        Opinion.objects.create(first_name = name,last_name=last_name,opinion = message)
        messages.add_message(request,messages.SUCCESS,'Habaringiz Muvofiqiyatli yuborildi')
    return render(request,'contact-us.html')

def course(request):
    courses = Course.objects.all()
    events = Event.objects.all()[:3]
    context = {
        'courses':courses,
        'events':events
    }
    return render(request,'course.html',context)

def leave_comment(request,id):
    url = request.META.get('HTTP_REFERER')
    if request.method == "POST":
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')
            news = News.objects.get(id=id)
            Comment.objects.create(news=news,name=name,email=email,body=message)
            messages.add_message(request,messages.SUCCESS,'Izoh muvofiqiyatli yuborildi')
        except Exception as e:
            messages.add_message(request,messages.ERROR,f'Izoh qoldirishda muammolar yuzaga keldi qayta urinib ko\'ring {e}')
        return redirect(url)
