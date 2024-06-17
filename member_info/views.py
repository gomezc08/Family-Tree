from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.conf import settings
from .forms import MemberInfoForm
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def member_info_view(request):
    if request.method == 'POST':
        form = MemberInfoForm(request.POST, request.FILES)
        if form.is_valid():
            # Prepare email content
            subject = "New Member Info Submitted"
            message = (
                f"First Name: {form.cleaned_data['FirstName']}\n"
                f"Last Name: {form.cleaned_data['LastName']}\n"
                f"Birthday: {form.cleaned_data['Birthday']}\n"
                f"Nickname: {form.cleaned_data.get('Nickname')}\n"
                f"Year Died: {form.cleaned_data.get('YearDied')}\n"
                f"Gender: {form.cleaned_data.get('Gender')}\n"
                f"Pronouns: {form.cleaned_data.get('Pronouns')}\n"
                f"Email: {form.cleaned_data.get('Email')}\n"
                f"Cell: {form.cleaned_data.get('Cell')}\n"
                f"City Born: {form.cleaned_data.get('CityBorn')}\n"
                f"State Born: {form.cleaned_data.get('StateBorn')}\n"
                f"Country Born: {form.cleaned_data.get('CountryBorn')}\n"
                f"City Current: {form.cleaned_data.get('CityCurrent')}\n"
                f"State Current: {form.cleaned_data.get('StateCurrent')}\n"
                f"Country Current: {form.cleaned_data.get('CountryCurrent')}\n"
            )
            from_email = settings.EMAIL_HOST_USER
            recipient_list = ['avgomez1@msn.com']  # Replace with the recipient's email

            # Create email
            email = EmailMessage(subject, message, from_email, recipient_list)

            # Attach the photo if provided
            if 'Photo' in request.FILES:
                photo = request.FILES['Photo']
                img = MIMEImage(photo.read())
                img.add_header('Content-ID', '<photo>')
                email.attach(img)

            # Send email
            email.send(fail_silently=False)

            return redirect('form_success')
    else:
        form = MemberInfoForm()
    
    return render(request, 'member_info/index.html', {'form': form})

def form_success_view(request):
    return render(request, 'member_info/form_success.html')
