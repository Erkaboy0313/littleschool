from django.urls import path
from .views import course,leave_comment,index,about_us,events, notfound,teachers,faq,news,contact,heads, news_details,course_details,staf_details,event_details
urlpatterns = [
    path('',index,name='index'),
    path('about-us/',about_us,name='about_us'),
    path('envents/',events,name='events'),
    path('teachers/',teachers,name='teachers'),
    path('heads/',heads,name='heads'),
    path('faq/',faq,name='faq'),
    path('news/',news,name='news'),
    path('contact/',contact,name='contact'),
    path('course/',course,name='course'),
    path('leave_comment/<int:id>',leave_comment,name='leave_comment'),
    path('page-not-found/',notfound,name='notfound'),

    #--------------- Detatils page ----------------
    
    path('news-detatils/<int:id>/',news_details,name='news_details'),
    path('course-detatils/<int:id>/',course_details,name='course_details'),
    path('staf-detatils/<int:id>/',staf_details,name='staf_details'),
    path('event-detatils/<int:id>/',event_details,name='event_details'),
    
]