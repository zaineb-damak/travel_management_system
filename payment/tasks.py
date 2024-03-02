from celery import shared_task
from django.core.mail import send_mail
from tms import settings

@shared_task
def send_email(user_email,user_name, booking_id, package_id, package_name, price):
    mail_subject = 'payment successful'
    message = f''' Dear {user_name},

    Thank you for completing your booking. here are the trip details:
    Booking ID: {booking_id}
    Package ID : {package_id}
    Package Name: {package_name}
    Total Paid: {price}

    We look forward to seeing you!
    
    TMS
    '''
    to_email = user_email

    send_mail(
        subject = mail_subject,
        message = message,
        email_from = settings.EMAIL_HOST_USER,  
        recipient_list=[to_email],
        fail_silently=True   
    )