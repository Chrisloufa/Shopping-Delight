from django import forms
from .models import Message


# Message details
class MessageForm(forms.ModelForm):
    """Rating and Review Form"""
    class Meta:
        """Form model and Fields"""
        model = Message
        fields = ['sender_name', 'sender_email', 'subject', 'message']
