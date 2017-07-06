from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.



def register(request):
    ''' register a new user '''
    if request.method != 'POST':
        # Display blank registration form.
        form = UserCreationForm()
    else:
        # Process completed form.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Log the user in and redirect them to the homepage.
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('mycloset:index'))
    context = {'form': form}
    return render(request, 'users/register.html', context)
