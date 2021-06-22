from django.shortcuts import render, redirect
from .views import *
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.contrib.auth.models import Group
from django.conf import settings
from .forms import *
from .decorators import *


def homepage(request):
    return render(request, 'ebigay/homepage.html')


@login_required(login_url='/login')
def register_ayuda(request):
    if(request.method == 'POST'):
        form = AyudaApplicantForm(request.POST, request.FILES)
        if(form.is_valid()):
            form.save()
            ayudaapplicant = Group.objects.get(name='AyudaApplicantGroup')
            ayudaapplicant.user_set.add(request.user.id)
            return render(request, 'ebigay/message.html')
            # if(AyudaApplicant.objects.all().filter(user=request.user.id)):
            #     return HttpResponse('You have already subscribed')
            # else:
            #     form.save()
            #     ayudaapplicant = Group.objects.get(name='AyudaApplicantGroup')
            #     ayudaapplicant.user_set.add(request.user.id)
            #     return render(request,'ebigay/message.html')
        else:
            print(form.errors)

    form = AyudaApplicantForm({"user": request.user.id})
    data = {"form": form}

    return render(request, 'ebigay/register_ayuda.html', data)


def register_account(request):
    form = UserForm()

    if(request.method == 'POST'):
        form = UserForm(request.POST)
        if(form.is_valid()):
            subject = "Ebigay account creation"
            message = "<h1>Hello " + request.POST.get(
                'username')+", good day!</h1> <br><br>This is to inform you that you have recently created an account with ebigay."
            from_email = settings.EMAIL_HOST_USER
            recepient_list = [request.POST.get('email')]

            # send_mail(subject, message, from_email, recepient_list)
            email = EmailMessage(
                subject,
                message,
                from_email,
                recepient_list
            )

            email.content_subtype = 'html'
            email.send()
            form.save()
            messages.success(request, "Account was created for " +
                             form.cleaned_data.get("username"))

            return redirect('/login')

    data = {"form": form}
    return render(request, "ebigay/register_account.html", data)


@allowed_users(allowed_roles=['Driver'])
@login_required(login_url='/login')
def dropoff_list_delete(request, pk):
    applicant = AyudaApplicant.objects.get(id=pk)
    ayudaapplicantdelete = Group.objects.get(name='AyudaApplicantGroup')
    ayudaapplicantdelete.user_set.remove(applicant.user_id)
    ayudadropoffdelete = Group.objects.get(name='AyudaDropoffGroup')
    ayudadropoffdelete.user_set.remove(applicant.user_id)
    person = AyudaDropoff.objects.get(ayudaapplicant_id=pk)
    person.delete()
    aperson = AyudaApplicant.objects.get(id=pk)
    aperson.delete()
    return redirect('/dropoff-list')


@allowed_users(allowed_roles=['AyudaApplicantGroup'])
@login_required(login_url='/login')
def ayuda_list_delete(request):
    aperson = AyudaDropoff.objects.all().filter(user_id=request.user.id)
    aperson.delete()
    person = AyudaApplicant.objects.all().filter(user_id=request.user.id)
    person.delete()
    if(request.user.groups.filter(name='AyudaApplicantGroup')):
        ayudaapplicantdelete = Group.objects.get(name='AyudaApplicantGroup')
        ayudaapplicantdelete.user_set.remove(request.user.id)
    if(request.user.groups.filter(name='AyudaDropoffGroup')):
        ayudaapplicantdelete = Group.objects.get(name='AyudaDropoffGroup')
        ayudaapplicantdelete.user_set.remove(request.user.id)

    return redirect('/register-ayuda')


def login_page(request):
    if(request.method == "POST"):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            print("Login Success.")
            return redirect('/')
        else:
            print("Login Failed.")
            messages.error(request, "Incorrect password or username")

    return render(request, 'ebigay/login.html')


@login_required(login_url='/login')
def logout_page(request):
    logout(request)
    return redirect('/login')


@login_required(login_url='/login')
def ayuda_dropoff(request):
    if(request.method == 'POST'):
        citychoice = CityForm(request.POST)
        if(citychoice.is_valid()):
            the_city = citychoice.cleaned_data.get('city')
            eligible_people = AyudaApplicant.objects.all().filter(city_id=the_city)
            for person in eligible_people:

                eligible_person = AyudaDropoffForm(
                    {"ayudaapplicant": person, "user": person.user_id})
                if(eligible_person.is_valid()):
                    if(not AyudaDropoff.objects.all().filter(ayudaapplicant_id=person.id)):
                        ayudadropoff = Group.objects.get(
                            name='AyudaDropoffGroup')
                        ayudadropoff.user_set.add(person.user_id)
                        eligible_person.save()
                else:
                    print(eligible_person.errors)

    citychoice = CityForm()
    data = {"citychoice": citychoice}

    return render(request, 'ebigay/ayudadropoff.html', data)


@allowed_users(allowed_roles=['Driver'])
@login_required(login_url='/login')
def dropoff_list(request):
    people = AyudaDropoff.objects.all()
    data = {"people": people}

    return render(request, 'ebigay/dropofflist.html', data)


@allowed_users(allowed_roles=['AyudaApplicantGroup'])
@login_required(login_url='/login')
def ayuda_schedule(request):
    ayudaman = AyudaDropoff.objects.all().filter(user_id=request.user.id)
    if(ayudaman):
        return render(request, 'ebigay/ayudapositive.html')
    else:
        return render(request, 'ebigay/ayudanegative.html')


def mission_vision(request):
    return render(request, 'ebigay/missionvision.html')


def volounteer(request):
    return render(request, 'ebigay/volounteer.html')


def story(request):
    return render(request, 'ebigay/story.html')


def donate(request):
    return render(request, 'ebigay/donate.html')


def terms_of_service(request):
    return render(request, 'ebigay/termsofservice.html')
