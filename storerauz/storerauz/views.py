import re
from .forms import SendEmailForm
from django.contrib import messages
from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from smtplib import SMTPException
from django.utils.translation import activate, get_language, gettext_lazy as _


from django.core.mail import send_mail
from django.conf import settings



class HomeView(TemplateView):
    template_name = 'home.html'





def pricing_view(request):
    return render(request,'pricing.html')

def storera_view(request):
    return render(request,'storera.html')

def about_view(request):
    return render(request,'about.html')



def send_email_view(request):
    if request.method == "POST":
        form = SendEmailForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email   = form.cleaned_data['email']
            title   = form.cleaned_data['title']
            message = form.cleaned_data['message']
            try:
                send_mail(f'{name} | '+ title  , message, settings.EMAIL_HOST_USER, [email], fail_silently=False)
                messages.success(request, "Email sent successfully")
                return redirect('home_page')
            except SMTPException as error:
                messages.error(request, f"Error while sending email: {error}")
                return redirect('send_email_view')
        else:
            messages.error(request, f"Invalid form: {form.errors}")
            context = { 'form': form }
            return render(request, 'email_template.html', context)

    form = SendEmailForm()
    context = { 'form': form }
    return render(request, 'email_template.html', context)