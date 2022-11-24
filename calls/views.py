from django.shortcuts import render, redirect
from django.utils.timezone import datetime
from django.core.paginator import Paginator

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from .models import *
from .forms import *
from .filters import *
from .decorators import *


######### Register/Login ############
# - Register
@unauthenticated_user
def registerPage(request):

    form = CreateUserForm()

    if request.method == 'POST': 

        form = CreateUserForm(request.POST)  

        if form.is_valid():

            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='Supervisors')
            user.groups.add(group)

            messages.success(request, 'Account was created for ' + username)

            return redirect('login')
        
    context = {'form': form}
    return render(request, 'calls/register.html', context)

# - Login
@unauthenticated_user
def loginPage(request):
        
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')

    context = {}
    return render(request, 'calls/login.html', context)

# - Logout
def logoutUser(request):

    logout(request)

    return redirect('login')

# - User
def userPage(request):

    context = {}

    return render(request, 'calls/user.html', context)

######### Dashboard ############\
@login_required(login_url='login')
@admin_only
def home(request):

    today = datetime.today().date()

    calls = Call.objects.all().order_by('-datetime')[:9]
    calls_today_count = Call.objects.filter(datetime__date=today).count()
    calls_mtd_count = Call.objects.filter(datetime__year=today.year, datetime__month=today.month).count()
    calls_ytd_count = Call.objects.filter(datetime__year=today.year).count()

    walkins = Walkin.objects.all().order_by('-datetime')[:7]
    walkins_today_count = Walkin.objects.filter(datetime__date=today).count()
    walkins_mtd_count = Walkin.objects.filter(datetime__year=today.year, datetime__month=today.month).count()
    walkins_ytd_count = Walkin.objects.filter(datetime__year=today.year).count()

    context = {
        'today': today,
        'calls': calls,
        'walkins': walkins,
        'calls_today_count': calls_today_count,
        'calls_mtd_count': calls_mtd_count, 
        'calls_ytd_count': calls_ytd_count,
        'walkins_today_count': walkins_today_count, 
        'walkins_mtd_count': walkins_mtd_count,
        'walkins_ytd_count': walkins_ytd_count, 
        }
    return render(request, 'calls/dashboard.html', context)

######### RESPONDERS #########
# - All Responders
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin', 'Supervisors'])
def allResponders(request):
    
    responders = Responder.objects.all().order_by('firstname').values()

    # Search Filter
    responderFilter = ResponderFilter(request.GET, queryset=responders)
    responders = responderFilter.qs
    # Pagination
    paginator = Paginator(responders, 10)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)

    context = {
            'responders': responders, 
            'responderFilter': responderFilter, 
            'page_obj': page_obj,
            }
    return render(request, 'calls/all_responders.html', context)

# - New Responder
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin', 'Supervisors'])
def newResponder(request):

    form = ResponderForm()

    if request.method == 'POST':
        form = ResponderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/responders')

    context = {'form': form}
    return render(request, 'calls/responder_form.html', context)

# - Update Responder
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin', 'Supervisors'])
def updateResponder(request, pk):

    responder = Responder.objects.get(id=pk)
    form = ResponderForm(instance=responder)

    if request.method == 'POST':
        form = ResponderForm(request.POST, instance=responder)
        if form.is_valid():
            form.save()
            return redirect('/responders')
    
    context = {'form': form}
    return render(request, 'calls/responder_form.html', context)

######### CALLS #########
# - All Calls
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin', 'Supervisors'])
def allCalls(request):

    calls = Call.objects.all().order_by('-datetime').values()
    # Search Filter
    callFilter = CallFilter(request.GET, queryset=calls)
    calls = callFilter.qs
    # Pagination
    paginator = Paginator(calls, 10)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)

    context = {
            'calls': calls, 
            'callFilter': callFilter, 
            'page_obj': page_obj,
            }
    return render(request, 'calls/all_calls.html', context)

# - New Call
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin', 'Supervisors'])
def newCall(request):

    form = CallForm()

    if request.method == 'POST':
        form = CallForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'calls/call_form.html', context)

# - On Scene
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin', 'Supervisors'])
def onScene(request, pk):

    call = Call.objects.get(id=pk)
    
    if request.method == "POST":
        call.on_scene_time = datetime.now().time()
        call.save()
        return redirect('/')
    
    context = {'item': call}
    return render(request, 'calls/on_scene.html', context)

# - Upgrade Call
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin', 'Supervisors'])
def upgradeCall(request, pk):

    call = Call.objects.get(id=pk)
    form = UpgradeForm(instance=call)

    if request.method == 'POST':
        form = UpgradeForm(request.POST, instance=call)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form': form}
    return render(request, 'calls/upgrade_call.html', context)

# - Cancel
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin', 'Supervisors'])
def cancelCall(request, pk):

    call = Call.objects.get(id=pk)
    
    if request.method == "POST":
        call.cancel_time = datetime.now().time()
        call.save()
        return redirect('/')
    
    context = {'item': call}
    return render(request, 'calls/cancel.html', context)

######### WALKINS #########
# - All Walkins
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin', 'Supervisors'])
def allWalkins(request):

    walkins = Walkin.objects.all().order_by('-datetime').values()
    # Search Filter
    walkinFilter = WalkinFilter(request.GET, queryset=walkins)
    walkins = walkinFilter.qs
    # Pagination
    paginator = Paginator(walkins, 10)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)

    context = {
            'walkins': walkins, 
            'walkinFilter': walkinFilter, 
            'page_obj': page_obj,
            }
    return render(request, 'calls/all_walkins.html', context)

# - New Walkin
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin', 'Supervisors'])
def newWalkin(request):

    form = WalkinForm()

    if request.method == 'POST':
        form = WalkinForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'calls/walkin_form.html', context)

# - Walkin
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin', 'Supervisors'])
def walkins(request, pk):

    walkin = Walkin.objects.get(id=pk)
    visits = Walkin.objects.filter(firstname=walkin.firstname, lastname=walkin.lastname).order_by('-datetime').values()
    total_visits = visits.count()

    context = {
            'walkin': walkin, 
            'visits': visits, 
            'total_visits': total_visits,
            }
    return render(request, 'calls/walkins.html', context)

# - Walkin Notes
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin', 'Supervisors'])
def walkinNotes(request, pk):

    walkin = Walkin.objects.get(id=pk)
    form = WalkinNotesForm(instance=walkin)

    if request.method == 'POST':
        form = WalkinNotesForm(request.POST, instance=walkin)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form': form}
    return render(request, 'calls/walkin_notes.html', context)
