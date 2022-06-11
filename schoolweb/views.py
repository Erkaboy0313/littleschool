from django.shortcuts import render
from .models import Staf,Course,Modul,Event,News,Comment,Faq,Opinion,Statistics
# Create your views here.

def notfound(request):
    return render(request,'404.html')

def index(request):
    course = Course.objects.all()
    statistics = Statistics.objects.all()[0]
    events = Event.objects.all()[0:10]
    news = News.objects.all().order_by('time')[:5]
    opinions = Opinion.objects.all().order_by('time')[:10]
    faq = Faq.objects.all()[:5]
    context = {
        'courses' : course,
        'statistics' : statistics,
        'events' : events,
        'news' : news,
        'opinions' : opinions,
        'faq' : faq,
    }
    return render(request,'index.html',context)

def about_us(request):
    teachers = Staf.objects.filter(user_type = Staf.TEACHER)
    events = Event.objects.all()
    return render(request,'about-us.html')

def events(request):
    events = Event.objects.all()
    return render(request,'event.html',{'events':events})

def teachers(request):
    teachers = Staf.objects.filter(user_type=Staf.TEACHER)
    return render(request,'our-teacher.html',{'teachers':teachers})

def heads(request):
    return render(request,'heads.html')

def faq(request):
    faqs = Faq.objects.all()
    return render(request,'faq.html',{'faqs':faqs})

def news(request):
    news = News.objects.all().order_by('-id')
    course = Course.objects.all().order_by('-id')
    teachers = Staf.objects.filter(user_type=Staf.TEACHER)
    events = Event.objects.all().order_by('-id')
    return render(request,'blog.html',{'news':news,'teachers':teachers,'course':course,'events':events})

def contact(request):
    return render(request,'contact-us.html')