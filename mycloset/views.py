from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.template import loader
from django.urls import reverse




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
    latest_owner_list = Owner.objects.order_by('-pub_date')[:5]
    template = loader.get_template('mycloset/index.html')
    context = {
        'latest_owner_list': latest_owner_list,
    }
    return render(request, 'mycloset/index.html', context)



@login_required
def detail(request, owner_id):
    '''
    purpose: shows owner details view
    author: miriam rozenbaum
    args: request -- The full HTTP request object
    returns: render detail view 
    '''
    owner = get_object_or_404(Owner, pk=owner_id)
    return render(request, 'mycloset/detail.html', {'owner': owner})



@login_required
def results(request, owner_id):
    owner = get_object_or_404(Owner, pk=owner_id)
    return render(request, 'mycloset/results.html', {'owner': owner})



@login_required
def like(request, owner_id):
    owner = get_object_or_404(Owner, pk=owner_id)
    try:
        selected_item = owner.item_set.get(pk=request.POST['item'])
    except (KeyError, Item.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'mycloset/detail.html', {
            'owner': owner,
            'error_message': "You didn't select an item.",
        })
    else:
        selected_item.item_likes += 1
        selected_item.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('mycloset:results', args=(owner.id,)))









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




@login_required
def owner_profile(request):
    '''
    purpose: shows owner_profile view, with owner profile details
    author: miriam rozenbaum
    args: request -- The full HTTP request object
    returns: render owner_profile view 
    '''
    template_name = 'mycloset/owner_profile.html'
    if request.method == 'GET':
        return render(request, template_name)

    if request.method == "POST":
        return render(request, template_name)



# @login_required
# def new_item(request, owner_id):
#     ''' adds a new item to a owners profile/closet '''
#     owner = Owner.objects.get(id=owner_id)
#     category = Category.objects.get(id=category_id)

#     if request.method != 'POST':
#         # no data submitted; create a blank form
#         form = ItemForm()

#     else:
#         # POST data submitted; process data
#         form = ItemForm(data=request.POST)
#         if form.is_valid():
#             new_item = form.save(commit=False)
#             new_item.owner = owner
#             new_item.save()
#             return HttpResponseRedirect(reverse('mycloset:item_results', args=[owner_id]))

#     context = {
#         'owner': owner,
#         'form': form}
#     return render(request, 'mycloset/new_item.html', context)


# @login_required
# def item_results(request, owner_id):
#     pass    

