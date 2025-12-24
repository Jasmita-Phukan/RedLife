from django.shortcuts import render, redirect
from .models import details, contactinfo
from .models import EmailIds
# Create your views here.

def about(request):
    if request.method == 'GET':
        email = request.GET.get('Mail')
        if email:
            EmailIds.objects.create(Email=email)
            return render(request, 'confirmation2.html')

    return render(request, 'about.html')
def aboutus(request):
    if request.method == 'GET':
        email = request.GET.get('Mail')
        if email:
            EmailIds.objects.create(Email=email)
            return render(request, 'confirmation2.html')
    return render(request, 'aboutus.html')
def blooddir(request):
    return render(request, 'blooddir.html')
def contact(request):
    if request.method == 'GET' and request.GET.get('first'):
        first = request.GET.get('first')
        last = request.GET.get('last')
        phone = request.GET.get('phone')
        Email = request.GET.get('Email')
        message = request.GET.get('message')

        contactinfo.objects.create(
            First_name=first,
            Last_name=last,
            phone=phone,
            Email=Email,
            message=message
        )
        return redirect('confirmation2')

    return render(request, 'contact.html')

def donateblood(request):
    return render(request, 'donateblood.html')
def confirmation2(request):
    return render(request, 'confirmation2.html')
from django.shortcuts import render, redirect
from .models import details

def submit_details(request):
    if request.method == 'GET' and request.GET.get('fname'):
        # Form is submitted
        form_data = {
            'blood_group': request.GET.get('bloodgroup'),
            'first_name': request.GET.get('fname'),
            'last_name': request.GET.get('lname'),
            'phone': request.GET.get('number'),
            'email': request.GET.get('email'),
            'country': request.GET.get('country'),
            'state': request.GET.get('state'),
            'city': request.GET.get('city'),
            'district': request.GET.get('district')
        }
        request.session['form_data'] = form_data
        return redirect('details2')
    return render(request, 'submit_details.html')


def details2(request):
    form_data = request.session.get('form_data')

    if not form_data:
        return redirect('submit_details')

    return render(request, 'details2.html', form_data)


def confirmation(request):
    otp = request.GET.get('otp', '')
    form_data = request.session.get('form_data')

    if otp == '123456' and form_data:
        # Save to database
        details.objects.create(
            blood_group=form_data['blood_group'],
            first_name=form_data['first_name'],
            last_name=form_data['last_name'],
            phone=form_data['phone'],
            email=form_data['email'],
            country=form_data['country'],
            state=form_data['state'],
            city=form_data['city'],
            district=form_data['district']
        )
        del request.session['form_data']

        return render(request, 'confirmation.html')

    return redirect('details2')
