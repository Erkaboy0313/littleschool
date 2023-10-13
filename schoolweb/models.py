from django.db import models
from django.contrib.auth.models import User

class Staf(models.Model):
    TEACHER = 'Teacher'
    STUDENT = 'Student'

    USER_TYPE = [
        (TEACHER,'Teacher'),
        (STUDENT,'Student')
    ]

    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    first_name = models.CharField(max_length=100,null=True)
    last_name = models.CharField(max_length=100,null=True)
    user_type = models.CharField(max_length=10,choices=USER_TYPE,default=TEACHER,null=True)
    biography = models.TextField(null=True)
    experience = models.TextField(null=True)
    education = models.TextField(null=True)
    email = models.EmailField(max_length=100,null=True)
    number = models.CharField(max_length=20,null=True)
    image = models.ImageField(upload_to = 'Staff')
    position = models.CharField(max_length=100,null=True,blank=True)
    bio_video = models.URLField(null=True,blank=True)

    def __str__(self):
        return self.user.username

class Course(models.Model):
    image = models.ImageField(upload_to = 'Course')
    title = models.CharField(max_length=100)
    teacher = models.ManyToManyField(Staf,blank=True)
    description = models.TextField()
    help = models.TextField()
    cost = models.IntegerField(default=0)
    time = models.DateTimeField(auto_now_add=True)
    duration = models.CharField(max_length=100)
    def __str__(self):
        return self.title

    @property
    def month(self):
        return self.time.strftime('%b')

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
    image = models.ImageField(upload_to = 'events',null=True)

    @property
    def imageUrl(self):
        try:
            return self.image.url
        except:
            return ''

    @property
    def time(self):
        return self.start_time.strftime('%H:%M')+" - "+self.end_time.strftime('%H:%M')
    
    @property
    def day(self):
        return self.start_time.strftime('%d')

    @property
    def month(self):
        return self.start_time.strftime('%b')
    
    class Meta:
        ordering = ['start_time']

    def __str__(self):
        return self.topic

class News(models.Model):
    
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='News')
    time = models.DateTimeField(auto_now_add=True)
    @property
    def day(self):
        return self.time.strftime('%d')
    @property
    def month(self):
        return self.time.strftime('%b')
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    news = models.ForeignKey(News,on_delete=models.CASCADE)
    name = models.CharField(max_length=255,null=True)
    email = models.EmailField(max_length=255,null=True)
    body = models.TextField()

    def __str__(self):
        return self.name + ' ' + self.body[0:20]

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
    checked = models.BooleanField(default=False)
    def __str__(self):
        return self.opinion

class Statistics(models.Model):
    teachers = models.IntegerField(default=0)
    finishers = models.IntegerField(default=0)
    pupils = models.IntegerField(default=0)
    special_courses = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.teachers}-{self.finishers}-{self.pupils}-{self.special_courses}'