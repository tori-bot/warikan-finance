from django.http import HttpResponse
from django.shortcuts import render,get_list_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import User,Profile,Account
from .forms import AccountForm, ProfileForm
# from .email import send_welcome_email

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    current_user = request.user
    user = User.objects.get(id=current_user.id)
    profile = Profile.get_profile_by_id(user.id)

    accounts= Account.objects.all()
    

    context = {
        'profile': profile,
        'user': user,
        'accounts': accounts,
    }
    return render(request,'home.html', context)

def profile_form(request, id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user=user)
    profile_form = ProfileForm()
    if request.method == 'POST':
        profile_form = ProfileForm(
            request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            profile_form.save()

            return redirect('home')
        else:
            return HttpResponse('Please fill the form correctly.')
    else:
        context = {
            'profile_form': profile_form,
            'user': user,
            'profile': profile
        }
        return render(request, 'profile_form.html', context)

def account_form(request, id):
    current_user = request.user
    user = User.objects.get(id=id)
    
    account_form = AccountForm()
    if request.method == 'POST':
        account_form = AccountForm(
            request.POST, request.FILES)
        if account_form.is_valid():
            account_form.save()

            return redirect('home')
        else:
            return HttpResponse('Please fill the form correctly.')
    else:
        context = {
            'account_form': account_form,
            'user': user
        }
        return render(request, 'account_form.html', context)