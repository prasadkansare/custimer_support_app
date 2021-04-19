from django.shortcuts import render,redirect
import urllib.request
from enquiry.models import Enquiry
from .forms import FeedbackForm,ReviewForm
from .models import Feedback,Review
from django.contrib import messages
from customersupport.settings import DEFAULT_FROM_EMAIL, ALLOWED_HOSTS,admin_email
from django.core.mail import send_mail,EmailMessage
from django.template.loader import render_to_string, get_template
import time
import string,random
from django.utils import timezone
# from .task import sleepy

from celery import shared_task
from time import sleep


customer_email=''
customer_name=''
user_data_id=''

# @shared_task
# def sleepy():
#     sleep(10)
#     print("HELLOOOOOOOOOOO")
#     letters = string.ascii_letters
#     review_link = ''.join(random.choice(letters) for i in range(20))
#     save_link = Review.objects.create(link = review_link,feedback_id = user_data_id)

#     subject = "Customer Review"    
#     ctx = {
#         'root_url':ALLOWED_HOSTS[0],
#         'customer_name':customer_name,
#         'save_link':review_link
#     }
#     content = get_template('reviewemail.html').render(ctx)
#     mail=EmailMessage(
#             subject,
#             content,
#             DEFAULT_FROM_EMAIL,
#             [customer_email],
#         )
#     mail.content_subtype = "html"
#     mail.send()
#     return None

def feedback(request,id):
    print("id*******************",id)
    id = id

    data = Enquiry.objects.raw("select * from enquiry where id = %s",[id])
    for x in data:
        global customer_email
        global customer_name
        customer_email = x.email
        customer_name = x.name
    
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            global user_data_id
            user_data = Feedback.objects.create(feedback = request.POST.get('feedback'),enquiry_id = id)
            user_data_id = user_data.id
            print("user_data????????????????????????????????",user_data.id)
            subject = "Service Provider Enquiry"    
            ctx = {
                'root_url':ALLOWED_HOSTS[0],
                'customer_name':customer_name,
                'feedback':user_data.feedback
            }
            content = get_template('feedbackemail.html').render(ctx)
            mail=EmailMessage(
                    subject,
                    content,
                    DEFAULT_FROM_EMAIL,
                    [customer_email],
                )
            mail.content_subtype = "html"
            mail.send()

            messages.success(request, 'Feedback Submitted Successfully.')

            redirect('/feedback/'+str(id))

            # time.sleep(300)

            letters = string.ascii_letters
            review_link = ''.join(random.choice(letters) for i in range(20))
            save_link = Review.objects.create(link = review_link,feedback_id = user_data.id)

            subject = "Customer Review"    
            ctx = {
                'root_url':ALLOWED_HOSTS[0],
                'customer_name':customer_name,
                'save_link':review_link
            }
            content = get_template('reviewemail.html').render(ctx)
            mail=EmailMessage(
                    subject,
                    content,
                    DEFAULT_FROM_EMAIL,
                    [customer_email],
                )
            mail.content_subtype = "html"
            mail.send()
            # sleepy.delay()

            letters = string.ascii_letters
            review_link = ''.join(random.choice(letters) for i in range(20))
            save_link = Review.objects.create(link = review_link,feedback_id = user_data_id)

            subject = "Customer Review"    
            ctx = {
                'root_url':ALLOWED_HOSTS[0],
                'customer_name':customer_name,
                'save_link':review_link
            }
            content = get_template('reviewemail.html').render(ctx)
            mail=EmailMessage(
                    subject,
                    content,
                    DEFAULT_FROM_EMAIL,
                    [customer_email],
                )
            mail.content_subtype = "html"
            mail.send()

        else:
            return render(request, 'feedback.html',{'form': form,'user_data':data})

    else:
        form = FeedbackForm()
    return render(request,'feedback.html',{'user_data':data})


def review(request,link):
    data = Review.objects.raw("select * from review where link = %s",[link])
    for x in data:
        review_id = x.id
        print("review_id",review_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            Review.objects.filter(id = review_id).update(review = request.POST.get('review'))
            Review.objects.filter(id = review_id).update(deleted_at=timezone.now())
            return redirect('/submitted')
        else:
            return render(request, 'review.html',{'form': form,'data':data})
    else:
        form = ReviewForm()
    return render(request,'review.html',{'data':data})

def thankyou(request):
    return render(request,'thankyou.html')



    