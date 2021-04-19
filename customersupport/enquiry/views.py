from django.shortcuts import render,redirect
from .models import Enquiry
from .forms import EnquiryForm
from django.contrib import messages
import time
# from django.contrib.sessions.models import Session
from customersupport.settings import DEFAULT_FROM_EMAIL, ALLOWED_HOSTS,admin_email
from django.core.mail import send_mail,EmailMessage
from django.template.loader import render_to_string, get_template

# Create your views here.
def enquiry(request):
    if request.method == "POST":
        print("request.method",request.method)
        form = EnquiryForm(request.POST)
        print("form",form)
        print("form.is_valid()",form.is_valid())
        if form.is_valid():
            user_data = Enquiry.objects.create(name=request.POST.get('name'), email=request.POST.get('email'),
                                            mobile=request.POST.get('mobile'),query = request.POST.get('query'))
            user_id = user_data.id
            user_name = user_data.name
            subject = "Customer Enquiry"    
            ctx = {
                'root_url':ALLOWED_HOSTS[0],
                'user_name':user_name,
                'user_id':user_id
            }
            content = get_template('enquiryemail.html').render(ctx)
            mail=EmailMessage(
                    subject,
                    content,
                    DEFAULT_FROM_EMAIL,
                    [admin_email],
                )
            mail.content_subtype = "html"
            mail.send()
            messages.success(request, 'Enquiry Submitted Successfully.')
            return redirect('/')
        else:
            print("Inelse")
            return render(request, 'enquiry.html',{'form': form})

    else:
        form = EnquiryForm()
    return render(request,'enquiry.html',{'form': form})
