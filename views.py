from django.shortcuts import render_to_response

from grocheris.models import GroceryItem

def index(request):
    return view_in_stock(request)

def view_in_stock(request):
    items = GroceryItem.objects.filter(in_out=False)
    return render_to_response('grocheris/view_in_stock.html',
                              locals())

def view_shopping_list(request):
    pass

def view_item(request, item_id=None):
    pass

def tag_item(request, item_id=None):
    pass

def vote(request, item_id=None):
    pass
