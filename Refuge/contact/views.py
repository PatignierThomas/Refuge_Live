from django.contrib import messages
from django.core.mail import get_connection, EmailMessage
from django.http import HttpResponseRedirect, HttpResponse, BadHeaderError
from django.shortcuts import render
from .forms import ContactFormForm


def nav(request):
    if request.method == 'POST':
        data = {
            "subject": request.POST.get("subject"),
            "message": request.POST.get("message"),
            "email": request.POST.get("email"),
            "name": request.POST.get("name"),
            "recipient_list": ["patignier.contact@gmail.com", ]
        }
        form = ContactFormForm(data)
        if form.is_valid():
            email_from = form.cleaned_data["email"]
            subject = form.cleaned_data["subject"], email_from
            message = form.cleaned_data['message']
            name = form.cleaned_data['name']
            try:
                with get_connection() as connection:
                    recipient_list = ["patignier.contact@gmail.com", ]
                    mail = EmailMessage(subject, message, email_from, recipient_list)
                    mail.send()
                    email_send = "Votre message a été envoyé avec succés."
                    messages.success(request, "Votre mail à bien été envoyé")
                    return HttpResponseRedirect("/nav-test/")
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
        else:
            erreur = form.errors
            return HttpResponseRedirect("/nav-test/")
            # return render(request, "main.html", {"erreur": erreur})
    return render(request, "main.html")

