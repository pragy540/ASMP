from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
#from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
import math
import random
from django.contrib.auth.models import User
from .models import Mentor, Profile
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth import login, authenticate
import csv


class Meta:
    model = User
    fields = ('username', 'first_name', 'last_name', 'email', 'password')


def csv_profile(request):
    response = HttpResponse(content_type = 'text/csv')
    writer = csv.writer(response)
    writer.writerow(['user','otp', 'password', 'fullname', 'rollno', 'department', 'degree', 'contactno', 'personalEmail', 'sop', 'linkedin', 'experience', 'goal', 'obstacle', 'pref_1', 'pref_2', 'pref_3', 'pref_4', 'pref_5'])
    for profile in Profile.objects.all().values_list('user','otp', 'password', 'fullname', 'rollno', 'department', 'degree', 'contactno', 'personalEmail', 'sop', 'linkedin', 'experience', 'goal', 'obstacle', 'pref_1', 'pref_2', 'pref_3', 'pref_4', 'pref_5'):
        writer.writerow(profile)
    response['Content-Disposition'] = 'attachment; filename="profiles.csv"'
    return response

def csv_mentor(request):
    response = HttpResponse(content_type = 'text/csv')
    writer = csv.writer(response)
    writer.writerow(['id','mentor_id','gender', 'year', 'department', 'degree', 'city', 'country', 'designation', 'company', 'discp', 'interest', 'maxmentees', 'score'])
    for mentor in Mentor.objects.all().values_list('id','mentor_id','gender', 'year', 'department', 'degree', 'city', 'country', 'designation', 'company', 'discp', 'interest', 'maxmentees', 'score'):
        writer.writerow(mentor)
    response['Content-Disposition'] = 'attachment; filename="mentor.csv"'
    return response

def csv_users(request):
    response = HttpResponse(content_type = 'text/csv')
    writer = csv.writer(response)
    writer.writerow(['id','username','email'])
    for user in User.objects.all().values_list('id','username','email'):
        writer.writerow(user)
    response['Content-Disposition'] = 'attachment; filename="users.csv"'
    return response



def index(request):
    return render(request, "land.html")


def profile(request):
    context = {
        'mentors_analytics': Mentor.objects.filter(interest = "Analytics"),
        'mentors_core': Mentor.objects.filter(interest = "Core engineering"),
        'mentors_ci': Mentor.objects.filter(interest = "Civil Services/Govt. of India"),
        'mentors_design': Mentor.objects.filter(interest = "Design"),
        'mentors_fin': Mentor.objects.filter(interest = "Finance"),
        'mentors_it': Mentor.objects.filter(interest = "IT"),
        'mentors_manc': Mentor.objects.filter(interest = "Management consulting"),
        'mentors_man': Mentor.objects.filter(interest = "Management"),
        'mentors_other': Mentor.objects.filter(interest = "Other"),
        'mentors_re': Mentor.objects.filter(interest = "Research"),
        'mentors_strat': Mentor.objects.filter(interest = "Strategy consulting"),
    }
    return render(request, "mentorlist.html", context)


def login1(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.filter(email=email).first()
        if user is None:
            context = {'message': 'User not found', 'class': 'danger'}
            return render(request, 'login_ritwik.html', context)
        requested_profile = Profile.objects.filter(user=user).first()
        if password == requested_profile.password:
            login(request, user)
            context = {'email': email}
            return redirect('profile')
        context = {'message': 'Incorrect Password', 'class': 'danger'}
        return render(request, 'login_ritwik.html', context)
    return render(request, 'login_ritwik.html')


def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        rollno = request.POST.get('rollno')
        department = request.POST.get('department')
        degree = request.POST.get('degree')
        contact = request.POST.get('contact')
        password = request.POST.get('password')
        check_user = User.objects.filter(email=email).first()
        if not email.split('@')[1]=='iitb.ac.in':
            context = {'message': 'Please login using your LDAP ID', 'class':'danger'}
            return render(request, 'register.html', context)
        if check_user:
            context = {'message': 'User already exists', 'class': 'danger'}
            return render(request, 'register.html', context)

        #user = User(email=email, username=name)
        # user.save()
        #otp = str(random.randint(1000, 9999))
        #profile = Profile(user=user, mobile=mobile, otp=otp)
        # profile.save()
        #email_success, mobile_success = send_otp(email, mobile, otp)
        otp = generateOTP()
        request.session['email'] = email
        request.session['name'] = name
        request.session['rollno'] = rollno
        request.session['department'] = department
        request.session['degree'] = degree
        request.session['contact'] = contact
        request.session['password'] = password
        request.session['otp'] = otp
        send_otp(email, otp)
        return redirect('otp')

        # if not email_success and not mobile_success:
        #context = {'message': 'OTP failed to generate', 'class': 'danger'}
        # return render(request, 'regiser.html', context)
        # return redirect('otp')
    return render(request, 'register.html')


def generateOTP():
    # digits = "0123456789"
    # OTP = ""
    OTP = "2907"
    # for i in range(4):
    #     OTP += digits[math.floor(random.random() * 10)]
    return OTP


def send_otp(email, otp_generated):
    subject = "OTP request"
    message = 'Hi, your otp is ' + str(otp_generated)
    # email_from = ('pragyaptl131996@gmail.com', 'SARC IIT Bombay')
    email_from = 'pragya.sarc@gmail.com'
    recipient = [email, ]
    # print(message)
    send_mail(subject, message, email_from, recipient, fail_silently=True)
    return None


def otp(request):
    #mobile = request.session['mobile']
    email = request.session['email']
    otp_to_check = request.session['otp']
    name = request.session['name']
    rollno = request.session['rollno']
    department = request.session['department']
    degree = request.session['degree']
    contact = request.session['contact']
    password = request.session['password']
    context = {'email': email}
    # print(otp_to_check)
    if request.method == 'POST':
        otp = request.POST.get('otp')
        if otp == otp_to_check:
            user = User(email=email, username=email)
            profile = Profile(user=user, password=password, fullname=name, rollno=rollno, department=department, degree=degree, contactno=contact)
            user.save()
            profile.save()
            return redirect('login')
        else:
            print('Wrong')
            context = {'message': 'Wrong OTP',
                       'class': 'danger', 'email': email}
            return render(request, 'otp.html', context)
    return render(request, 'otp.html')


def favourite_add(request, id):

    mentor = get_object_or_404(Mentor, id=id)
    if mentor.favourites.filter(id=request.user.id).exists():
        mentor.favourites.remove(request.user)
    else:
        mentor.favourites.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

    # def favourite_add(request, id):
    #     mentor = get_object_or_404(Mentor, id=id)
    #     if mentor.favourites.filter(id=request.user.id).exists():
    #         mentor.favourites.remove(request.user)
    #         Preference.objects.filter(mentor_id=id, user=request.user).delete()
    #     else:
    #         mentor.favourites.add(request.user)
    #     return HttpResponseRedirect(request.META['HTTP_REFERER'])


def maxscore(max_mentees):
    if max_mentees == 1:
        return 5.0
    elif max_mentees == 2:
        return 9.0
    elif max_mentees == 3:
        return 12.0
    elif max_mentees == 4:
        return 15.0


def favourite_list(request):

    new = Mentor.objects.all().filter(
        favourites=request.user)
    ids = new.values_list('pk', flat=True)
    for i in ids:
        mentor_update = Mentor.objects.get(id=i)
        mentor_update.maxscore = maxscore(mentor_update.maxmentees)
        if float(mentor_update.score) > mentor_update.maxscore:
            mentor_update.available = False
        mentor_update.save()
    return render(request, 'wishlist.html', {'new': new})


def returnScore(pref):

    if pref == 1:
        return 2
    elif pref == 2:
        return 1.5
    elif pref == 3:
        return 1
    elif pref == 4:
        return 0.8
    elif pref == 5:
        return 0.6


def update(request):
    # email = request.session['email']
    new = Mentor.objects.all().filter(
        favourites=request.user)
    ids = new.values_list('pk', flat=True)
    error_msg = None
    c = 0
    profile = Profile.objects.get(user=request.user)
    if (not profile.fullname or not profile.rollno or not profile.department or not profile.degree or not profile.contactno):
        error_msg = "Enter complete personal information"
    elif (not profile.sop):
        error_msg = "Enter SOP"
    elif (profile.pref_1 != None):
        error_msg = "You have already submitted your preferences. You are not allowed to do it again."
    for i in ids:
        preference = request.POST[str(i) + " preference"]
        if (preference != "0"):
            c = c+1
            for j in ids:
                if (j == i):
                    continue
                else:
                    pref_temp = request.POST[str(j) + " preference"]
                    if (pref_temp == preference):
                        error_msg = "Unique Preference required"
                    else:
                        continue

        else:
            continue
    if (c > 0):
        for i in ids:
            preference = request.POST[str(i) + " preference"]
            p = int(preference)
            if (p != 0):
                if p in range(1, c+1):
                    continue
                else:
                    error_msg = "Enter preferences in order"
            else:
                continue
    else:
        error_msg = "Enter atleast one preference"

    if not error_msg:
        for i in ids:
            preference = request.POST[str(i) + " preference"]
            mentor = Mentor.objects.get(id=request.POST[str(i)])
            if (preference != "0"):
                if (preference == "1"):
                    profile.pref_1 = mentor.id
                elif (preference == "2"):
                    profile.pref_2 = mentor.id
                elif (preference == "3"):
                    profile.pref_3 = mentor.id
                elif (preference == "4"):
                    profile.pref_4 = mentor.id
                elif (preference == "5"):
                    profile.pref_5 = mentor.id
                profile.save()
                mentor.score = mentor.score + returnScore(int(preference))
                mentor.save()
            else:
                continue
        return render(request, 'finish.html')
    else:
        return render(request, 'wishlist.html', {'error': error_msg, 'new': new})

# @login_required
# def profile(request):
#     if request.method == 'POST':
#         u_form = UserUpdateForm(request.POST, instance=request.register)
#         p_form = ProfileUpdateForm(request.POST,
#                                    request.FILES,
#                                    instance=request.register.profile)
#         if u_form.is_valid() and p_form.is_valid():
#             u_form.save()
#             p_form.save()
#             messages.success(request, f'Your account has been updated!')
#             return redirect('profile')

#     else:
#         u_form = UserUpdateForm(instance=request.register)
#         p_form = ProfileUpdateForm(instance=request.register.profile)

#     context = {
#         'u_form': u_form,
#         'p_form': p_form
#     }

#     return render(request, 'register/profile.html', context)

    # def favourite_add(request, id):
    #     mentor = get_object_or_404(Mentor, id=id)
    #     if mentor.favourites.filter(id=request.user.id).exists():
    #         mentor.favourites.remove(request.user)
    #         Preference.objects.filter(mentor_id=id, user=request.user).delete()
    #     else:
    #         mentor.favourites.add(request.user)
    #     return HttpResponseRedirect(request.META['HTTP_REFERER'])


def test(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'personal_info.html', {'profile': profile})

def logout_view(request):
    logout(request)
    return render(request, 'land.html')


def personal_info_add(request):
    profile = Profile.objects.get(user=request.user)
    # profile.fullname = request.POST['Field1']
    # profile.rollno = request.POST['Field2']
    # profile.department = request.POST['Field3']
    # profile.degree = request.POST['Field4']
    profile.personalEmail = request.POST['Field11']
    profile.linkedin = request.POST['Field10']
    profile.sop = request.POST['Field6']
    profile.experience = request.POST['Field7']
    # profile.goal = request.POST['Field8']
    profile.obstacle = request.POST['Field9']
    profile.save()
    return render(request, 'personal_info.html', {'profile': profile})
