from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.template import loader



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

    # template_name = 'mycloset/index.html'
    # if request.method == 'GET':
    #     return render(request, template_name)

    # if request.method == "POST":
    #     return render(request, template_name)



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






def detail(request, owner_id):
    owner = get_object_or_404(Owner, pk=owner_id)
    return render(request, 'mycloset/detail.html', {'owner': owner})

def results(request, owner_id):
    response = "You're looking at the results of owner %s."
    return HttpResponse(response % owner_id)

def like(request, owner_id):
    return HttpResponse("You're liking on something %s." % owner_id)








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

