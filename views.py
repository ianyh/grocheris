from django.shortcuts import render_to_response

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

def add_item_form(request):
    add_form = GroceryItemForm()
    return HttpResponse('<tr><td>' + add_form.as_table + '</td></tr>')

def view_item(request, item_id=None):
    pass

def tag_item(request, item_id=None):
    pass

def vote(request, item_id=None):
    pass
