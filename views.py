from django.shortcuts import render_to_response

from grocheris.models import GroceryItem

def index(request):
    pass

def view_in_stock(request):
    pass

def view_shopping_list(request):
    pass

def view_item(request, item_id=None):
    pass

def tag_item(request, item_id=None):
    pass

def vote(request, item_id=None):
    pass
