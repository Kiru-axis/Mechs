from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .forms import SignUpForm,UpdateUserForm, UpdateUserProfileForm,RatingsForm,CommentForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse,HttpResponse
from .models import Mechanic,Rating,Comment
from django.core.mail import send_mail
from django.utils import timezone
# Create your views here.

# signup
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})



# main view function
@login_required(login_url='login')
def index(request):

    context = {
       "mechanic":Mechanic.objects.all()
   }
    return render(request, 'okoa/index.html',context)

# test Profile


# profile function
@login_required(login_url='login')
def profile(request, username):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        user_form = UpdateUserForm(instance=request.user)
        prof_form = UpdateUserProfileForm(instance=request.user.profile)
    params = {
        'user_form': user_form,
        'prof_form': prof_form,

    }
    return render(request, 'okoa/profile.html', params)

# user update profile function
@login_required(login_url='login')
def mechanic(request,pk):
    mechanic = Mechanic.objects.get(id=pk)
    ratings = Rating.objects.filter(user=request.user, mechanic=mechanic).first()
    rating_status = None
    if ratings is None:
        rating_status = False
    else:
        rating_status = True
    if request.method == 'POST':
        form = RatingsForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = request.user
            rate.mechanic = mechanic
            print(rate.user)
            print(rate.mechanic)
            rate.save()
            mech_ratings = Rating.objects.filter(mechanic=mechanic)

            communication_ratings = [c.communication for c in mech_ratings]
            communication_average = sum(communication_ratings) / len(communication_ratings)

            punctuality_ratings = [pu.punctuality for pu in mech_ratings]
            punctuality_average = sum(punctuality_ratings) / len(punctuality_ratings)

            workrate_ratings = [wr.workrate for wr in mech_ratings]
            workrate_average = sum(workrate_ratings) / len(workrate_ratings)

            score = (communication_average + punctuality_average + workrate_average) / 3
            print(score)
            rate.communication_average = round(communication_average, 2)
            rate.punctuality_average = round(punctuality_average, 2)
            rate.workrate_average = round(workrate_average, 2)
            rate.score = round(score, 2)
            rate.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = RatingsForm()
    params = {
        'mechanic': mechanic,
        'rating_form': form,
        'rating_status': rating_status

    }
    return render(request, 'okoa/mechanic.html', params)

@login_required(login_url='login')
def services(request):

    context = {
       "mechanic":Mechanic.objects.all()
   }
    return render(request, 'okoa/services.html',context)


@login_required(login_url='login')
def add_comment(request,pk):
    mech = Mechanic.objects.get(id=pk)
    form = CommentForm(instance=mech)
    if request.method == 'POST':
        form = CommentForm(request.POST,instance=mech)
        if form.is_valid():
            name = request.user.profile
            body = form.cleaned_data['body']
            c=Comment(mechanic=mech,commenter=name,body=body,created = timezone.now)
            c.save()
            return redirect('index')
        else:
            print("invalid form")
    else:
        form =CommentForm()
    
    context = {
        'form':form,
        }
    return render(request, 'okoa/add_comments.html',context)


@login_required(login_url='login')
def contact(request):
    if request.method == 'POST':
        message_name = request.POST.get('message-name',False) 
        message_email = request.POST.get('message-email',False) 
        message = request.POST.get('message',False) 

        send_mail(
            message_name,
            message,
            message_email,
            ["peter.kiru@student.moringaschool.com"]
        ) 

        return render(request, 'okoa/contact.html',{"message_name": message_name})
    else:
        return render(request, 'okoa/contact.html',{})


# userr profile
