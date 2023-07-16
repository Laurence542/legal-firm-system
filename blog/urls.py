from django.conf.urls.static import static
from django.conf import settings
from . import views
from.views import about
from.views import lawyer_index1
from.views import lawyer_clients
from.views import feature
from.views import application_appointments
from.views import dashboard_client
from.views import cliants_apply
from.views import dashboard_client
from django.urls import path
from .views import delete_application
from .views import applications_list
from .views import retrieve_data
from .views import chat_room
from .views import lawyerchart
from .views import add_service
from .views import cliant_notification
from .views import signup
from .views import lawyer_signup
from .views import lawyer_login
from .views import manager_view
from .views import clients_login
from .views import clients_signup
from .views import manager_login
from .views import manager_signup
from .views import logout_view
from .views import ContactUs
from .views import our_services
from .views import contact_views
from .views import manager_application_view




urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('about/',about, name = "about"),
    path('our_service/',our_services, name = "our_service"),
    path('contact_us/',ContactUs, name = "contact_us"),
    path('contact_view/',contact_views, name = "contact_view"),
    path('application_view/',manager_application_view, name = "application_view"),
    path('logout/', logout_view, name='logout'),
    path('managers_login/', manager_login, name='managers_login'),
    path('managers_signup/', manager_signup, name='managers_signup'),
    path('applications/', applications_list, name='applications_list'),
    path('client_logins/', clients_login, name='client_logins'),
    path('client_signups/', clients_signup, name='client_signups'),
    path('lawyer_index/',lawyer_index1, name = "lawyer_index"),
    path('lawyer_signups/',lawyer_signup, name = "lawyer_signups"),
    path('manager_views/',manager_view, name = "manager_view"),
    path('lawyer_logins/', lawyer_login, name='lawyer_logins'),
    path('add_services/',add_service, name = "add_services"),
    path('signups/',signup, name = "signups"),
    path('status_applications/',dashboard_client, name = "status_applications"),
    path('applications_appointment/',application_appointments, name = "applications_appointment"),
    path('retrieve-data/', retrieve_data, name='retrieve_data'),
    path('cliant_notif/', cliant_notification, name='cliant_notif'),
    path('applications/<int:application_id>/delete/', delete_application, name='delete_application'),
    path('lawyer_client/',lawyer_clients, name = "lawyer_client"),
    path('dashboard_client1/',dashboard_client, name = "dashboard_client1"),
    path('lawyerchat/',lawyerchart, name = "lawyerchat"),
    path('dashboard_client/', cliants_apply, name='dashboard_client'),
    path('feature/',feature, name = "feature"),
    path('chat/', chat_room, name='chat_room'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('category/<category>/', views.CatListView.as_view(), name='category'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
