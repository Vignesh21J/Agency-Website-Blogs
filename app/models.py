from django.db import models

from django.utils import timezone

# Create your models here.
class GeneralInfo(models.Model):
    company_name = models.CharField(max_length=255, default="Company")
    location = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    open_hours = models.CharField(max_length=100, blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    twitterX = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.company_name
    

class Service(models.Model):
    icon = models.CharField(max_length=20, blank=True, null=True)
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title
    

class Testimonial(models.Model):
    user_image = models.CharField(max_length=255, blank=True, null=True)
    
    stars_count = [
        (1, 'One'),
        (1.5, 'OnePointFive'),
        (2, 'Two'),
        (2.5, 'TwoPointFive'),
        (3, 'Three'),
        (3.5, 'ThreePointFive'),
        (4, 'Four'), 
        (4.5, 'FourPointFive'),
        (5, 'Five')
    ]

    rating_count = models.FloatField(choices = stars_count)
    username = models.CharField(max_length=50)
    user_job_title = models.CharField(max_length=50)
    review = models.TextField()

    def __str__(self):
        return f"{self.username} - {self.user_job_title}"
    

class FrequentlyAskQns(models.Model):
    question = models.CharField(max_length=250)
    answer = models.TextField()

    def __str__(self):
        return self.question
    

class ContactFormLog(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    action_time = models.DateTimeField(null = True, blank = True)
    is_success = models.BooleanField(default=False)
    is_error = models.BooleanField(default=False)

    error_message = models.TextField(null = True,  blank = True)

    def __str__(self):
        return self.email
    
    
class Author(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50, null = True, blank = True)
    country = models.CharField(max_length = 50)
    joined_date = models.DateTimeField(null = True, blank = True)

    def __str__(self):
        return self.first_name


class Blog(models.Model):
    blog_image = models.CharField(max_length=255, null = True, blank = True)
    category = models.CharField(max_length=55, null = True, blank = True)
    title = models.CharField(max_length=255)
    
    #author = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete = models.PROTECT, null = True, blank = True)

    created_at = models.DateTimeField(default = timezone.now)
    content = models.TextField(default = None, null = True, blank = True)

    def __str__(self):
        return self.title
