from home.forms import UserForm, ProfileForm
from django.contrib.auth import authenticate,login
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, redirect
from django.template import RequestContext

# Create your views here.

def home(request):
    try: user = request.user
    except: pass

    if request.method == "POST" and "login-button" in request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
             if user.is_active:
                login(request, user)
                url = '/user-profile/' + str(user.username)
                return redirect(url)
        else:
            form = UserForm()
            messages.error(request, 'Your username or password was incorrect, please try again.')
            return render(request, 'home/home.html/', {'form': form})
    else:
        form = UserForm()

    return render(request, 'home/home.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home/home.html/')

def register(request):
    try: user=request.user
    except: pass

    if request.method == "POST":
        messages.success('Do something with this registration, web dev.')
    else:
        form = UserForm()
        profile_form = ProfileForm()
    return render(request, 'registration/register_form.html', {'form': form,
                                                          'profile_form': profile_form
                                                          })

def register_form(request):
    return render(request, 'registration/register_form.html')


def pricing(request):
    return render(request, 'pricing/pricing.html')

def how(request):
    return render(request, 'how/how.html')

def performance(request):
    return render(request, 'performance/performance.html')
