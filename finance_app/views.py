from django.http import HttpResponse
from django.shortcuts import render,get_list_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import User,Profile,Account,Bill
from .forms import AccountForm, BillForm, ProfileForm
from .requests import get_all_news,youtube_videos
# from .email import send_welcome_email

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    current_user = request.user
    user = User.objects.get(id=current_user.id)
    profile = Profile.get_profile_by_id(user.id)

    accounts= Account.objects.filter(user=user)
    bills=Bill.objects.filter(user=user)
    

    context = {
        'profile': profile,
        'user': user,
        'accounts': accounts,
        'bills': bills
    }
    return render(request,'home.html', context)

def about(request):
    return render(request,'about.html')

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
            account=Account.objects.create(
               name=account_form.cleaned_data.get('name'),
               category=account_form.cleaned_data.get('category'),
               amount=account_form.cleaned_data.get('amount'),
                description=account_form.cleaned_data.get('description'),
                user=user
           )
            account.save()

            return redirect('home')
        else:
            return HttpResponse('Please fill the form correctly.')
    else:
        context = {
            'account_form': account_form,
            'user': user
        }
        return render(request, 'account_form.html', context)

def bill_form(request, id):
    current_user = request.user
    user = User.objects.get(id=id)
    
    bill_form = BillForm()
    if request.method == 'POST':
        bill_form = BillForm(
            request.POST, request.FILES)
        if bill_form.is_valid():
            bill=Bill.objects.create(
               category=bill_form.cleaned_data.get('category'),
               name=bill_form.cleaned_data.get('name'),
               amount=bill_form.cleaned_data.get('amount'),
                description=bill_form.cleaned_data.get('description'),
                account=bill_form.cleaned_data.get('account'),
                due_date=bill_form.cleaned_data.get('due_date'),
                user=user
           )
            bill.save()

            return redirect('home')
        else:
            return HttpResponse('Please fill the form correctly.')
    else:
        context = {
            'bill_form': bill_form,
            'user': user
        }
        return render(request, 'bill_form.html', context)

def news(request):
    news=get_all_news()
    return render(request,'news.html',{'news': news})

def insights(request):
    videos=youtube_videos()
    return render(request,'insights.html',{'videos':videos})