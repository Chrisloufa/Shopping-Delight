from django.db import models


# Message information
class Message(models.Model):
    sender_name = models.CharField(max_length=80)
    sender_email = models.EmailField()
    subject = models.CharField(max_length=80)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-sent_at"]
