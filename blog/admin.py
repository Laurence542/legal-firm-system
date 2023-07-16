from django.contrib import admin
from .models import Post
from .models import approval
from .models import Appointment
from .models import ClientApplication
from .models import Message
from .models import LegalChat
from .models import Manager_signup
from .models import Lawyer_signup
from .models import Client_signup
from .models import Contact_us_info
from .import models


admin.site.register(Contact_us_info)
admin.site.register(Client_signup)
admin.site.register(Lawyer_signup)
admin.site.register(Post)
admin.site.register(models.Category)
admin.site.register(ClientApplication)
admin.site.register(approval)
admin.site.register(Appointment)
admin.site.register(Manager_signup)
admin.site.register(Message)
admin.site.register(LegalChat)



