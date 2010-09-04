from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.utils import simplejson
from django.contrib.auth.decorators import login_required

from datetime import datetime

from grocheris.models import GroceryItem
from grocheris.forms import GroceryItemForm

@login_required
def index(request):
    return view_in_stock(request)

@login_required
def view_in_stock(request):
    items = GroceryItem.objects.filter(is_out=False)
    return render_to_response('grocheris/view_in_stock.html',
                              locals())

@login_required
def view_shopping_list(request):
    add_form = GroceryItemForm()
    items = GroceryItem.objects.filter(is_low=True)
    return render_to_response('grocheris/view_shopping_list.html',
                              locals())

@login_required
def add_item(request):
    if request.method == "POST":
        form = GroceryItemForm(request.POST)
        if form.is_valid():
            item = GroceryItem()
            item.name = request.POST['name']
            item.stock_date = datetime.now()
            item.is_out = True
            item.is_low = True
            if 'locations' in request.POST:
                item.locations = request.POST['locations']
            item.save()
            
            json = simplejson.dumps({ 'name' : item.name, 'id' : item.id })
            return HttpResponse(json, mimetype='application/json')
        else:
            return HttpResponse()
    else:
        return HttpResponse()

@login_required
def buy_item(request, item_id=None):
    if request.method == 'POST':
        item = GroceryItem.objects.get(pk=item_id)
        if item:
            item.is_low = False
            item.is_out = False
            item.stock_date = datetime.now()
            item.save()

            json = simplejson.dumps({ 'id' : item.id })
            return HttpResponse(json, mimetype='application/json')

    return HttpResponse(status=404)

@login_required
def low_item(request, item_id=None):
    item = GroceryItem.objects.get(pk=item_id)
    if item:
        item.is_low = True
        item.save()
        
        json = simplejson.dumps({ 'id' : item.id })
        return HttpResponse(json, mimetype='application/json')
    
    return HttpRespinse(status=404)

@login_required
def out_item(request, item_id=None):
    item = GroceryItem.objects.get(pk=item_id)
    if item:
        item.is_low = True
        item.is_out = True
        item.save()

        json = simplejson.dumps({ 'id' : item.id })
        return HttpResponse(json, mimetype='application/json')
    
    return HttpResponse(status=404)

"""
def view_item(request, item_id=None):
    pass

def tag_item(request, item_id=None):
    pass

def vote(request, item_id=None):
    pass
"""
