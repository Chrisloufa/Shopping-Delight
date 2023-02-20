"""Model for contact form"""
from django.db import models


# Message information
class Message(models.Model):
    """Details for message model"""
    sender_name = models.CharField(max_length=80)
    sender_email = models.EmailField()
    subject = models.CharField(max_length=80)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Time sesnt meta tag"""
        ordering = ["-sent_at"]
