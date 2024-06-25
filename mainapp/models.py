from django.db import models
from django_quill.fields import QuillField

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='images/', blank=True, null=True)
    # description = models.TextField(blank=True, null=True)
    description = QuillField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    address = models.TextField(blank=True, null=True)

    class Meta: 
        ordering = ['updated_at', 'pk']
    
    def __str__(self):
        return self.title + " : "+ str(self.updated_at.date())

LINK_CHOICES=(
    ('email', 'Email'),
    ('google-scholar', 'Google Scholar'),
    ('linkedin', 'LinkedIn'),
    ('github', 'Github'),
    ('facebook', 'Facebook'),
    ('twitter', 'Twitter'),
)
class Link(models.Model):
    media = models.CharField(max_length=20, choices=LINK_CHOICES, blank=True, null=True)
    link = models.CharField(max_length=200)

    def __str__(self):
        return self.media 


class Research(models.Model):
    title = models.CharField(max_length=100)
    description = QuillField(blank=True, null=True) # models.TextField()
    # description = models.TextField(blank=True, null=True) # models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title 

PUBLICATION_TYPE = (
    ('journal', 'Journal Article'),
    ('conference', 'Conference Proceedings'),
    ('book_chapter', 'Book Chapter'),
    ('book', 'Book'),
)
class Publication(models.Model):
    type = models.CharField(max_length=50, choices=PUBLICATION_TYPE)
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=500, blank=True, null=True)
    journal_name = models.CharField(max_length=200, blank=True, null=True)
    volume = models.CharField(max_length=10, blank=True, null=True)
    issue = models.CharField(max_length=10, blank=True, null=True)
    pages = models.CharField(max_length=10, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    doi = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)
    pdf_link = models.CharField(max_length=200, blank=True, null=True)
    cite = QuillField(blank=True, null=True) # models.TextField(blank=True, null=True)
    # cite = models.TextField(blank=True, null=True) # models.TextField(blank=True, null=True)
    comments = QuillField(blank=True, null=True)# models.TextField(blank=True, null=True)
    # comments = models.TextField(blank=True, null=True)# models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.journal_name +" : " +self.title
    
    class Meta: 
        ordering = ['-date', 'pk']

class Highlight(models.Model):
    date = models.DateField()
    description = QuillField(blank=True, null=True) # models.TextField()
    # description = models.TextField(blank=True, null=True) # models.TextField()

    def __str__(self):
        return str(self.date) 

class Experience(models.Model):
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    post = models.CharField(max_length=50)
    company = models.CharField(max_length=100)
    company_url = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.post + " : "+self.company
    

class Education(models.Model):
    degree = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    institute = models.CharField(max_length=100)
    institute_url = models.CharField(max_length=200, blank=True, null=True)

    class Meta: 
        ordering = ['-start_date', 'pk']

    def __str__(self):
        return self.degree
    
