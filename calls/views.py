from django.shortcuts import render, redirect
from django.utils import timezone
from django.utils.timezone import datetime, timedelta
from django.core.paginator import Paginator

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
@allowed_users(allowed_roles=['Admin', 'Supervisors'])
def home(request):

    today = timezone.now()
    time_threshold = today - timedelta(hours=2)

    calls = Call.objects.all().order_by('-datetime')[:8]
    calls_today_count = Call.objects.filter(datetime__date=today).count()
    calls_mtd_count = Call.objects.filter(datetime__year=today.year, datetime__month=today.month).count()
    calls_ytd_count = Call.objects.filter(datetime__year=today.year).count()

    walkins = Walkin.objects.all().order_by('-datetime')[:8]
    walkins_today_count = Walkin.objects.filter(datetime__date=today).count()
    walkins_mtd_count = Walkin.objects.filter(datetime__year=today.year, datetime__month=today.month).count()
    walkins_ytd_count = Walkin.objects.filter(datetime__year=today.year).count()

    todays_calls = Call.objects.all().filter(datetime__date=today)
    z_701 = todays_calls.filter(zone='701').count()
    z_705 = todays_calls.filter(zone='705').count()
    z_710 = todays_calls.filter(zone='710').count()
    z_720 = todays_calls.filter(zone='720').count()
    z_725 = todays_calls.filter(zone='725').count()
    z_730 = todays_calls.filter(zone='730').count()
    z_740 = todays_calls.filter(zone='740').count()
    z_745 = todays_calls.filter(zone='745').count()

    context = {
        'today': today,
        'time_threshold': time_threshold,
        'calls': calls,
        'walkins': walkins,
        'calls_today_count': calls_today_count,
        'calls_mtd_count': calls_mtd_count, 
        'calls_ytd_count': calls_ytd_count,
        'walkins_today_count': walkins_today_count, 
        'walkins_mtd_count': walkins_mtd_count,
        'walkins_ytd_count': walkins_ytd_count,
        'z_701': z_701,
        'z_705': z_705,
        'z_710': z_710,
        'z_720': z_720,
        'z_725': z_725,
        'z_730': z_730,
        'z_740': z_740,
        'z_745': z_745, 
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
            obj = form.save(commit=False)
            if obj.red == True:
                obj.upgrade_time = datetime.now().time()
            obj.save()
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


# - Downgrade Call
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin', 'Supervisors'])
def downgradeCall(request, pk):

    call = Call.objects.get(id=pk)
    form = DowngradeForm(instance=call)

    if request.method == 'POST':
        form = DowngradeForm(request.POST, instance=call)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form': form, 'call': call}
    return render(request, 'calls/downgrade_call.html', context)


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


# - Ambassador Sign in
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin', 'Supervisors'])
def ambassadorSignin(request):

    form = WalkinForm()

    if request.method == 'POST':
        form = WalkinForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sign-in Success!')
            
            return redirect('/ambassador_signin')
        
    context = {'form': form}
    return render(request, 'calls/ambassador_signin_form.html', context)


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


######### REPORTING #########
# - Reporting
@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin', 'Supervisors'])
def reporting(request):

    calls = Call.objects.all()
    z_701 = calls.filter(zone='701').count()
    z_705 = calls.filter(zone='705').count()
    z_710 = calls.filter(zone='710').count()
    z_720 = calls.filter(zone='720').count()
    z_725 = calls.filter(zone='725').count()
    z_730 = calls.filter(zone='730').count()
    z_740 = calls.filter(zone='740').count()
    z_745 = calls.filter(zone='745').count()

    yellows = calls.filter(upgrade_time=None)
    y_701 = yellows.filter(zone='701').count()
    y_705 = yellows.filter(zone='705').count()
    y_710 = yellows.filter(zone='710').count()
    y_720 = yellows.filter(zone='720').count()
    y_725 = yellows.filter(zone='725').count()
    y_730 = yellows.filter(zone='730').count()
    y_740 = yellows.filter(zone='740').count()
    y_745 = yellows.filter(zone='745').count()

    oranges = calls.exclude(upgrade_time=None)
    o_701 = oranges.filter(zone='701').count()
    o_705 = oranges.filter(zone='705').count()
    o_710 = oranges.filter(zone='710').count()
    o_720 = oranges.filter(zone='720').count()
    o_725 = oranges.filter(zone='725').count()
    o_730 = oranges.filter(zone='730').count()
    o_740 = oranges.filter(zone='740').count()
    o_745 = oranges.filter(zone='745').count()

    reds = calls.exclude(red=False)
    r_701 = reds.filter(zone='701').count()
    r_705 = reds.filter(zone='705').count()
    r_710 = reds.filter(zone='710').count()
    r_720 = reds.filter(zone='720').count()
    r_725 = reds.filter(zone='725').count()
    r_730 = reds.filter(zone='730').count()
    r_740 = reds.filter(zone='740').count()
    r_745 = reds.filter(zone='745').count()

    context = {
            'z_701': z_701,
            'z_705': z_705,
            'z_710': z_710,
            'z_720': z_720,
            'z_725': z_725,
            'z_730': z_730,
            'z_740': z_740,
            'z_745': z_745,
            'y_701': y_701,
            'y_705': y_705,
            'y_710': y_710,
            'y_720': y_720,
            'y_725': y_725,
            'y_730': y_730,
            'y_740': y_740,
            'y_745': y_745,
            'o_701': o_701,
            'o_705': o_705,
            'o_710': o_710,
            'o_720': o_720,
            'o_725': o_725,
            'o_730': o_730,
            'o_740': o_740,
            'o_745': o_745,
            'r_701': r_701,
            'r_705': r_705,
            'r_710': r_710,
            'r_720': r_720,
            'r_725': r_725,
            'r_730': r_730,
            'r_740': r_740,
            'r_745': r_745,
            }
    return render(request, 'calls/reporting.html', context)