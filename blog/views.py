from django.views import generic
from .models import Post
from django.shortcuts import render
from django.views.generic import ListView
from .models import Post, Category
from django.shortcuts import redirect
from .models import ClientApplication
from .models import approval
from .models import Appointment
from .models import Message
from .models import LegalChat
from .models import Contact_us_info
from django.contrib import messages
from .models import Lawyer_signup
from .models import Client_signup
from .models import Manager_signup
from django.contrib import messages
import re
from django.contrib.auth import logout



# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    
# application appointment
def application_appointments(request):
    if request.method == 'POST':
        name_appointment = request.POST.get('names')
        email_appointment = request.POST.get('emails')
        date_appointment = request.POST.get('dates')
        upload_appointment = request.FILES.get('pdfs')
        messages_appointment = request.POST.get('messages')

        insert_application = Appointment.objects.filter(names=name_appointment, emails=email_appointment, dates=date_appointment, pdfs=upload_appointment, messages=messages_appointment)
        if not insert_application:
            insert_application2 = Appointment(names=name_appointment, emails=email_appointment, dates=date_appointment, pdfs=upload_appointment, messages=messages_appointment)
            insert_application2.save()
            return render(request, 'Lawyer_dashboard/application_appointment.html', {'error_message': 'Your appointment is created successfully.'})
        else:
            return render(request, 'Lawyer_dashboard/application_appointment.html', {'error_message': 'Sorry, there was an issue processing your request. Please try again later.'})
        
    return render(request, 'Lawyer_dashboard/application_appointment.html')


# application appointment

def about(request):
    return render(request, "about.html")   


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


def home(request):
    return render(request, 'base.html')   


def lawyer_index1(request):
    data_count = ClientApplication.objects.count()
    service_count = Post.objects.count()
    return render(request, "Lawyer_dashboard/index_lawyer.html", {'data_count': data_count, 'service_count':service_count}) 


def lawyer_clients(request):
    if request.method == 'POST':
        application_id = request.POST.get('application_id')
        approval_status = request.POST.get('case_category')

        application = ClientApplication.objects.get(pk=application_id)
        if not application.approval_status:
            # If approval status doesn't exist, create a new approval object
            new_approval = approval.objects.create(approval_status=approval_status)
            application.approval_status = new_approval
        else:
            # Update the existing approval object
            application.approval_status.approval_status = approval_status

        application.approval_status.save()
        application.save()

        return render(request, "Lawyer_dashboard/index_lawyer.html", {'error_message': 'Client status is updated.'})

    applications = ClientApplication.objects.all()
    return render(request, "Lawyer_dashboard/cliants.html", {'applications': applications})


# chat start

def chat_room(request):
    messages = Message.objects.all()
    return render(request, 'chat/chat_room.html', {'messages': messages})



def retrieve_data(request):
    messages = Message.objects.all()
    if request.method == 'POST':
        content = request.POST.get('content')
        Message.objects.create(content=content)
    return render(request, 'cliant_dashboard/application_approval.html',  {'messages': messages})

def lawyerchart(request):
    messages = Message.objects.all()
    legal_chats = LegalChat.objects.all()

    if request.method == 'POST':
        contents = request.POST.get('content_legal')
        LegalChat.objects.create(content_legal=contents)
        
    return render(request, 'chat/chat_room.html', {'legal_chats': legal_chats, 'messages': messages})
  
    # end of chat



def dashboard_client(request):
    applications = ClientApplication.objects.all()
    return render(request, "cliant_dashboard/application_status.html", {'applications': applications})

def cliant_notification(request):
    appointments = Appointment.objects.all()
    return render(request, "cliant_dashboard/notification.html", {'appointments': appointments})


def add_service(request):
    if request.method == 'POST':
        title_add = request.POST.get('title')
        slug_add = request.POST.get('slug')
        body_add = request.POST.get('body')

        Post.objects.create(title=title_add,slug=slug_add,body=body_add)

        context = {'error_message': 'Service added sucessful'}

        return render(request, 'Lawyer_dashboard/services.html', context)

    return render(request, 'Lawyer_dashboard/services.html')


def cliants_apply(request):
    if request.method == 'POST':
        client_names = request.POST.get('client_name')
        client_emails = request.POST.get('client_email')
        case_detailss = request.POST.get('case_details')
        case_categorys = request.POST.get('case_category')
        appointment_dates = request.POST.get('appointment_date')
        documents = request.FILES.get('document')


        insert_informations = ClientApplication.objects.filter(client_name=client_names, client_email=client_emails, case_details=case_detailss, case_category=case_categorys, appointment_date=appointment_dates, document=documents)
        if insert_informations:
            return render(request, 'cliant_dashboard/apply_dashboard.html', {'error_message': 'Not sucessful please try agin.'})

        else:
            insert_information22 = ClientApplication(client_name=client_names, client_email=client_emails, case_details=case_detailss, case_category=case_categorys, appointment_date=appointment_dates, document=documents)
            insert_information22.save()
            return render(request, 'cliant_dashboard/apply_dashboard.html', {'error_message': 'You have applied sucessfully.'})

    return render(request, 'cliant_dashboard/apply_dashboard.html')



def delete_application(request, application_id):
    # Retrieve the application object
    application = ClientApplication.objects.get(id=application_id)

    # Delete the application object
    application.delete()

    # Redirect to the applications list page
    return redirect('applications_list')



def applications_list(request):
    applications = ClientApplication.objects.all()
    return render(request, 'cliant_dashboard/application_status.html', {'applications': applications})



class CatListView(ListView):
    template_name = 'category.html'
    context_object_name = 'catlist'

    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'],
            'posts': Post.objects.filter(category__name=self.kwargs['category']).filter(status='1')
        }
        return content



def category_list(request):
    category_list = Category.objects.exclude(name='default')
    context = {
        "category_list": category_list,
    }
    return context
    


def about(request):
    return render(request, 'about.html')    


def feature(request):
    return render(request, 'feature.html')     

def signup(request):
    return render(request, 'signup.html')

def lawyer_signup(request):
    if request.method == 'POST':
        lawyer_full_names = request.POST['lawyer_full_name']
        lawyer_emails = request.POST['lawyer_email']
        lawyer_passwords = request.POST['lawyer_password']

        # Create a new manager
        lawyer = Lawyer_signup.objects.create(lawyer_full_name=lawyer_full_names, lawyer_email=lawyer_emails, lawyer_password=lawyer_passwords)
        lawyer.save()
        # Display success message
        messages.success(request, 'You have successfully signed up!')

        return redirect('manager_view')

    return render(request, 'Lawyer_dashboard/lawyer_signup.html')


def lawyer_login(request):
    if request.method == 'POST':
       lawyer_emails = request.POST['lawyer_email']
       lawyer_passwords = request.POST['lawyer_password']

       manager_lawyers = Lawyer_signup.objects.filter(lawyer_email=lawyer_emails, lawyer_password=lawyer_passwords)
       if manager_lawyers:
            return render(request, 'manager/managerview.html', {'error_message': 'You have successfully logged in.'})
        
       else:
             return render(request, 'Lawyer_dashboard/lawyer_login.html', {'error_message': 'Invalid username or password. Please try again'})
    
    return render(request, 'Lawyer_dashboard/lawyer_login.html')

def manager_view(request):
    applications = ClientApplication.objects.all()
    return render(request, 'manager/managerview.html',{'applications': applications})


def clients_login(request):
    if request.method == 'POST':
       client_emailss = request.POST['client_email']
       client_passwordss = request.POST['client_password']

       manager_client = Client_signup.objects.filter(client_email=client_emailss, client_password= client_passwordss)
       if manager_client:
            return render(request, 'cliant_dashboard/apply_dashboard.html', {'error_message': 'You have successfully logged in.'})
        
       else:
             return render(request, 'cliant_dashboard/login_cliant.html', {'error_message': 'Invalid username or password. Please try again'})
    
    return render(request, 'cliant_dashboard/login_cliant.html')


def clients_signup(request):
    if request.method == 'POST':
        client_full_names = request.POST['client_full_name']
        client_emails = request.POST['client_email']
        client_passwords = request.POST['client_password']

        # Create a new manager
        clients = Client_signup.objects.create(client_full_name=client_full_names, client_email=client_emails, client_password=client_passwords)
        clients.save()
        # Display success message
        messages.success(request, 'You have successfully signed up!')

        return redirect('dashboard_client')
     
    return render(request, 'cliant_dashboard/signup_cliant.html')



def manager_login(request):
   if request.method == 'POST':
        manager_email = request.POST['manager_email']
        manager_password = request.POST['manager_password']

        manager_users = Manager_signup.objects.filter(manager_email=manager_email, manager_password=manager_password)
        if manager_users:
            return render(request, 'lawyer_dashboard/index_lawyer.html', {'error_message': 'You have successfully logged in.'})
        
        else:
             return render(request, 'manager/manager_login.html', {'error_message': 'Invalid username or password. Please try again'})
       
  
   return render(request, 'manager/manager_login.html')        




def manager_signup(request):
    if request.method == 'POST':
        full_name = request.POST['manager_full_name']
        email = request.POST['manager_email']
        password = request.POST['manager_password']

        # Create a new manager
        manager = Manager_signup.objects.create(manager_full_name=full_name, manager_email=email, manager_password=password)
        manager.save()
        # Display success message
        messages.success(request, 'You have successfully signed up!')

        return redirect('lawyer_index')
     
    return render(request, 'manager/manager_signup.html')

def logout_view(request):
    logout(request)
    return redirect('home')


def our_services(request):
    services_post = Post.objects.all()
    return render(request, 'services.html', {'services_post': services_post})



def ContactUs(request):
    if request.method == 'POST':
        contact_name = request.POST.get('contact_name')
        contact_email = request.POST.get('contact_email')
        contact_subject = request.POST.get('contact_subject')
        contact_message = request.POST.get('contact_message')

        # Server-side validation
        if not contact_name or not contact_email or not contact_subject or not contact_message:
            error_message = 'Please fill in all the fields.'
            return render(request, 'contactus.html', {'error_message': error_message})
        elif not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', contact_email):
            error_message = 'Please enter a valid email address.'
            return render(request, 'contactus.html', {'error_message': error_message})
        else:
            contact_info = Contact_us_info()
            contact_info.contact_namess = contact_name
            contact_info.contact_emails = contact_email
            contact_info.contact_subjects = contact_subject
            contact_info.contact_messages = contact_message
            contact_info.save()

            success_message = 'Your message has been sent successfully.'
            return render(request, 'contactus.html', {'success_message': success_message})

    return render(request, 'contactus.html')



def contact_views(request):
    view_all_contact = Contact_us_info.objects.all()
    return render(request, 'Lawyer_dashboard/contactus_view.html', {'view_all_contact': view_all_contact})



def manager_application_view (request):
    applications = ClientApplication.objects.all()
    return render(request, 'manager/application_review.html', {'applications': applications})

