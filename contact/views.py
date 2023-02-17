""" Contact app views """
from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.


def contact(request):
    """View to return contact us page"""
    if request.method == 'POST':
        # Send contact form to Gmail Account
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        message_data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message,
        }
        message = '''
        From: {}
        New message: {}
        '''.format(message_data['email'], message_data['message'])

        send_mail(
            message_data['subject'], message, '', ['chris.mcgarry3@gmail.com'])

        messages.info(request, (
            f'Your message has been sent, we will contact you \
                via { email } as soon as possible.'))
        return render(request, 'home/index.html')

    return render(request, 'contact/contact.html')
