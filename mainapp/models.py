from django.db import models
# from django_quill.fields import QuillField

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='images/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    # description = QuillField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    address = models.TextField(blank=True, null=True)

    class Meta: 
        ordering = ['updated_at', 'pk']
    
    def __str__(self):
        return self.title + " : "+ str(self.updated_at.date())