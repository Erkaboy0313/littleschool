from django.urls import path
from .views import index,about_us,events, notfound,teachers,faq,news,contact,heads
urlpatterns = [
    path('',index,name='index'),
    path('about-us/',about_us,name='about_us'),
    path('envents/',events,name='events'),
    path('teachers/',teachers,name='teachers'),
    path('heads/',heads,name='heads'),
    path('faq/',faq,name='faq'),
    path('news/',news,name='news'),
    path('contact/',contact,name='contact'),
    path('page-not-found/',notfound,name='notfound'),
]