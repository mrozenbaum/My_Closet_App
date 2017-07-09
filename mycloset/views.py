from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.template import loader
from django.urls import reverse
from django.views import generic





from .models import Owner, Item, Category
from .forms import OwnerForm, ItemForm


# Create your views here.

class IndexView(generic.ListView):
    '''
    purpose: shows index view
    author: miriam rozenbaum
    args: request -- The full HTTP request object
    returns: render index view 
    '''
    template_name = 'mycloset/index.html'
    context_object_name = 'latest_owner_list'

    def get_queryset(self):
        """Return the last five published owners."""
        return Owner.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]



class DetailView(generic.DetailView):
    '''
    purpose: shows owner details view
    author: miriam rozenbaum
    args: request -- The full HTTP request object
    returns: render detail view 
    '''
    model = Owner
    template_name = 'mycloset/detail.html'

    def get_queryset(self):
        '''
        excludes any owners that have not been added yet
        '''
        return Owner.objects.filter(pub_date__lte=timezone.now())



class ResultsView(generic.DetailView):
    model = Owner
    template_name = 'mycloset/results.html'




@login_required
def ItemViewView(request, owner_id):
    owner = get_object_or_404(Owner, pk=owner_id)
    try:
        selected_item = owner.item_set.get(pk=request.POST['item'])
    except (KeyError, Item.DoesNotExist):
        # redisplay the Item form
        return render(request, 'mycloset/detail.html', {
            'owner': owner,
            'error_message': "You didnt select an Item.",
        })
    else:
        selected_item.item_likes += 1
        selected_item.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a user
        # hits the back button
    return HttpResponseRedirect(reverse('mycloset:results', args=(owner.id,)))



def single_item(request, item):
    ''' view single item '''
    all_items = Item.objects.all()
    selected_item = all_item(id=pk)
    context = {'selected_item': selected_item}
    return render(request, 'mycloset/results.html', context)    




@login_required
def new_owner(request):
    ''' add a new owner profile '''
    if request.method != 'POST':
        # no data submitted, create a blank profile form
        owner_form = OwnerForm()
    else:
        # POST data submitted; process data
        owner_form = OwnerForm(request.POST)
        if owner_form.is_valid():
            owner_form.save()
            return HttpResponseRedirect(reverse('mycloset:index'))

    context = {'owner_form': owner_form}
    return render(request, 'mycloset/new_owner.html', context) 




@login_required
def new_item(request, owner_id):
    ''' adds a new item for a selected owner '''
    owner = Owner.objects.get(id=owner_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        item_form = ItemForm()

    else:
        # POST data submitted; process data.
        item_form = ItemForm(data=request.POST)
        if item_form.is_valid():
            new_item = item_form.save(commit=False)
            new_item.owner = owner
            new_item.save()
            return HttpResponseRedirect(reverse('mycloset:results', args=[owner_id]))

    context = {'owner': owner, 'item_form': item_form}
    return render(request, 'mycloset/new_item.html', context)




@login_required
def edit_owner(request, owner_id):
    ''' edit an existing owner profile '''
    owner = Owner.objects.get(id=owner_id)

    if request.method != 'POST':
        # Initial request; pre-fill form with the current Owner info
        owner_form = OwnerForm(instance=owner)
    else:
        # POST data submitted; process data.
        owner_form = OwnerForm(instance=owner, data=request.POST)
        if owner_form.is_valid():
            owner_form.save()
            return HttpResponseRedirect(reverse('mycloset:detail', args=[owner.id]))
    context = {'owner': owner, 'owner_form': owner_form}
    return render(request, 'mycloset/edit_owner.html', context)




@login_required
def edit_item(request, item_id):
    ''' edit an existing item '''
    item = Item.objects.get(id=item_id)
    owner = item.owner

    if request.method != 'POST':
        # Initial request; pre-fill form with the current Item info
        item_form = ItemForm(instance=item)
    else:
        # POST data submitted; process data.
        item_form = ItemForm(instance=item, data=request.POST)
        if item_form.is_valid():
            item_form.save()
            return HttpResponseRedirect(reverse('mycloset:detail', args=[owner.id]))
    context = {'item': item, 'owner': owner, 'item_form': item_form}
    return render(request, 'mycloset/edit_item.html', context)





@login_required
def like(request, owner_id):
    owner = get_object_or_404(Owner, pk=owner_id)
    try:
        selected_item = owner.item_set.get(pk=request.POST['item'])
    except (KeyError, Item.DoesNotExist):
        # re-display the owner item form.
        return render(request, 'mycloset/detail.html', {
            'owner': owner,
            'error_message': "You didn't select an item.",
        })
    else:
        selected_item.item_likes += 1
        selected_item.save()
        # always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('mycloset:results', args=(owner.id,)))




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














