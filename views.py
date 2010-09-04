from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.utils import simplejson

from datetime import datetime

from grocheris.models import GroceryItem
from grocheris.forms import GroceryItemForm

def index(request):
    return view_in_stock(request)

def view_in_stock(request):
    items = GroceryItem.objects.filter(is_out=False)
    return render_to_response('grocheris/view_in_stock.html',
                              locals())

def view_shopping_list(request):
    add_form = GroceryItemForm()
    items = GroceryItem.objects.filter(is_low=True)
    return render_to_response('grocheris/view_shopping_list.html',
                              locals())

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
            
            json = simplejson.dumps({ 'name' : item.name })
            return HttpResponse(json, mimetype='application/json')
        else:
            return HttpResponse()
    else:
        return HttpResponse()
    

def view_item(request, item_id=None):
    pass

def tag_item(request, item_id=None):
    pass

def vote(request, item_id=None):
    pass
