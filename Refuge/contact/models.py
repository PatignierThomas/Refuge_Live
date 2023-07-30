from cms.models import CMSPlugin
from django.db import models


class ContactForm(CMSPlugin):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()



