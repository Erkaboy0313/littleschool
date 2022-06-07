from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render

class Staf(models.Model):
    TEACHER = 'Teacher'
    STUDENT = 'Student'
    DIRECTOR = 'Director'
    SOMEONE = 'Someone'

    USER_TYPE = [
        (TEACHER,'Teacher'),
        (STUDENT,'Student'),
        (DIRECTOR,'Director'),
        (SOMEONE,'Someone'),
    ]

    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    first_name = models.CharField(max_length=100,null=True)
    last_name = models.CharField(max_length=100,null=True)
    user_type = models.CharField(max_length=10,choices=USER_TYPE,default=SOMEONE,null=True)
    biography = models.TextField(null=True)
    experience = models.TextField(null=True)
    education = models.TextField(null=True)
    email = models.EmailField(max_length=100,null=True)
    number = models.CharField(max_length=20,null=True)
    image = models.ImageField(upload_to = 'Staff')

    def __str__(self):
        return self.user.username

class Course(models.Model):
    image = models.ImageField(upload_to = 'Course')
    title = models.CharField(max_length=100)
    teacher = models.ForeignKey(Staf,on_delete=models.SET_NULL,null=True)
    description = models.TextField()
    help = models.TextField()

    def __str__(self):
        return self.title

class Modul(models.Model):
    name = models.CharField(max_length=255)
    course = models.ForeignKey(Course,on_delete=models.SET_NULL,null= True)

    def __str__(self):
        return f'{self.name} - {self.course.title}'

class Event(models.Model):
    topic = models.CharField(max_length=100)
    description = models.TextField()
    aim = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    place = models.CharField(max_length=255)
    cost = models.IntegerField(default=0)
    audience = models.IntegerField(default=1)

    @property
    def time(self):
        return self.start_time.strftime('%I:%M')+" - "+self.end_time.strftime('%I:%M')
    
    @property
    def day(self):
        return self.start_time.strftime('%D')
    @property
    def month(self):
        return self.start_time.strftime('%b')

    def __str__(self):
        return self.topic

class News(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='News')
    time = models.DateTimeField(auto_now_add=True)
    @property
    def day(self):
        return self.time.strftime('%D')
    @property
    def month(self):
        return self.time.strftime('%b')
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    news = models.ForeignKey(News,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.user.username + self.body[0:20]

class Faq(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question

class Opinion(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    opinion = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.opinion

class Statistics(models.Model):
    teachers = models.IntegerField(default=0)
    finishers = models.IntegerField(default=0)
    pupils = models.IntegerField(default=0)
    special_courses = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.teachers}-{self.finishers}-{self.pupils}-{self.special_courses}'