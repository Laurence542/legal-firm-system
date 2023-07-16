from django.db import models 
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)  # Make the slug field blank=True
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    updated_on = models.DateTimeField(auto_now=True)
    body = models.TextField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:  # Generate the slug only if it is not already set
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
 
class Contact_us_info(models.Model):
    contact_namess = models.CharField(max_length=255)
    contact_emails = models.EmailField(max_length=255)
    contact_subjects = models.CharField(max_length=50000)
    contact_messages = models.CharField(max_length=5000)

    def __str__(self):
        return self.contact_namess

class Client_signup(models.Model):
    client_full_name = models.CharField(max_length=255)
    client_email = models.EmailField(max_length=255)
    client_password = models.CharField(max_length=255)

    def __str__(self):
        return self.client_full_name

class Lawyer_signup(models.Model):
    lawyer_full_name = models.CharField(max_length=255)
    lawyer_email = models.EmailField(max_length=255)
    lawyer_password = models.CharField(max_length=255)

    def __str__(self):
        return self.lawyer_full_name

class Manager_signup(models.Model):
    manager_full_name = models.CharField(max_length=255)
    manager_email = models.CharField(max_length=255)
    manager_password = models.CharField(max_length=255)

    def __str__(self):
        return self.manager_full_name

class ClientApplication(models.Model):
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField()
    case_details = models.TextField()
    case_category = models.CharField(max_length=50)
    appointment_date = models.DateField()
    document = models.FileField(upload_to='documents/', blank=True, null=True)
    approval_status = models.OneToOneField('approval', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.client_name)


class approval(models.Model):
    approval_status = models.CharField(max_length=10)

    def __str__(self):
        return str(self.approval_status)

    
class Appointment(models.Model):
    names = models.CharField(max_length=100)
    emails = models.EmailField()
    dates = models.DateField()
    pdfs = models.FileField(upload_to='pdfs/')
    messages = models.TextField()

    def __str__(self):
        return str(self.names)

class Message(models.Model):
    content = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return str(self.content)
    

class LegalChat(models.Model):
    content_legal = models.TextField(null=True, blank=True)
    timestamp_legal = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return str(self.content_legal)    

