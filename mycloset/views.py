from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone


from .models import Owner, Item, Category
from .forms import OwnerForm, ItemForm


# Create your views here.

def index(request):
    '''
    purpose: shows index view
    author: miriam rozenbaum
    args: request -- The full HTTP request object
    returns: render index view 
    '''
    template_name = 'mycloset/index.html'
    if request.method == 'GET':
        return render(request, template_name)

    if request.method == "POST":
        return render(request, template_name)



@login_required
def new_owner(request):
    ''' add a new owner profile '''
    if request.method != 'POST':
        #  no data submitted, create a blank profile form
        form = OwnerForm()
    else:
        # POST data submitted; process data
        form = OwnerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('mycloset:owner_success'))

    context = {'form': form}
    return render(request, 'mycloset/new_owner.html', context)        