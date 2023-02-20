""" Contact app views """
from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
from .forms import MessageForm


# Contact view
def contact(request):
    """View to return contact us page"""

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            email_subject = f'New contact {form.cleaned_data["sender_email"]}: {form.cleaned_data["subject"]}'
            email_message = form.cleaned_data['message']
            send_mail(email_subject, email_message,
                      '', ['chris.mcgarry3@gmail.com'])
            # Redirect to success page here.
            messages.success(
                request, 'Contact request submitted successfully.')
            return render(request, 'contact/success.html')
        else:
            # Form is invalid. Render the form again with error messages.
            messages.error(request, 'Invalid form submission.')
            return render(request, 'contact/contact.html', {'form': form})
    else:
        form = MessageForm()

    return render(request, 'contact/contact.html', {'form': form})
