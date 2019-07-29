from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm


def emailview(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender = form.cleaned_data['sender']
            message = form.cleaned_data['message']
            send_a_copy_to_myself = form.cleaned_data['send_a_copy_to_myself']

            recipients = ['mszlo@mail.ru']
            if send_a_copy_to_myself:
                recipients.append(sender)

            try:
                send_mail(subject, message, sender, recipients)
            except BadHeaderError:
                return HttpResponse('Something goes wrong. Please contact admin via e-mail(sashasbox.forjob@gmail.com)')
            return redirect('thanks')
    else:
        form = ContactForm()

    return render(request, "contacts/contactsEmail.html", {'form': form})


def successview(request):
    return HttpResponse('Success! Thank you for your message.')
