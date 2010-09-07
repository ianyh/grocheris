from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.utils import simplejson
from django.contrib.auth.decorators import login_required

from datetime import datetime

from grocheris.models import GroceryItem, Location
from grocheris.forms import GroceryItemForm, LocationSelectionForm, TagForm

from tagging.models import Tag
from tagging.utils import parse_tag_input

def base_view(template, context):
    add_tag_form = TagForm()
    context.update(locals())
    return render_to_response(template,
                              context)

@login_required
def view_all(request):
    items = GroceryItem.objects.all()
    show_low = True
    show_out = True
    show_buy = True
    return base_view('grocheris/view_all.html',
                     locals())

@login_required
def view_in_stock(request):
    items = GroceryItem.objects.filter(is_out=False)
    show_low = True
    show_out = True
    return base_view('grocheris/view_in_stock.html',
                     locals())

@login_required
def view_shopping_list(request):
    gen_shopping_list_form = LocationSelectionForm()
    add_form = GroceryItemForm()
    items = GroceryItem.objects.filter(is_low=True)
    show_buy = True
    return base_view('grocheris/view_shopping_list.html',
                     locals())

@login_required
def generate_shopping_list(request):
    if request.method == 'POST':
        location_id = request.POST['locations']
        items = GroceryItem.objects.filter(locations__pk__contains=location_id)

        return render_to_response('grocheris/shopping_list.html',
                                  locals())
    return HttpResponse()

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

    raise Http404()

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

    raise Http404()

@login_required
def low_item(request, item_id=None):
    item = GroceryItem.objects.get(pk=item_id)
    if item:
        item.is_low = True
        item.save()
        
        json = simplejson.dumps({ 'id' : item.id })
        return HttpResponse(json, mimetype='application/json')
    
    raise Http404()

@login_required
def out_item(request, item_id=None):
    item = GroceryItem.objects.get(pk=item_id)
    if item:
        item.is_low = True
        item.is_out = True
        item.save()

        json = simplejson.dumps({ 'id' : item.id })
        return HttpResponse(json, mimetype='application/json')
    
    raise Http404()

@login_required
def delete_item(request, item_id=None):
    item = GroceryItem.objects.get(pk=item_id)
    if item:
        item.delete()
        json = simplejson.dumps({ 'id' : item_id })
        return HttpResponse(json, mimetype='application/json')

    raise Http404()

@login_required
def item_row_html(request, item_id=None):
    if request.method == "POST":
        item = GroceryItem.objects.get(pk=item_id)
        if item:
            show_buy = True
            html = render_to_string('grocheris/item_row.html',
                                    locals())
            json = simplejson.dumps({ 'html' : html })
            return HttpResponse(json, mimetype='application/json')

    raise Http404()

@login_required
def view_item(request, item_id=None):
    if request.method == "POST":
        item = GroceryItem.objects.get(pk=item_id)
        if item:
            show_buy = True
            invisible = True
            html = render_to_string('grocheris/item_row.html',
                                    locals())
            json = simplejson.dumps({ 'html' : html, 'id' : item.id })
            return HttpResponse(json, mimetype='application/json')

    raise Http404()

@login_required
def add_tag(request):
    if request.method == 'POST':
        item_id = request.POST['item_id']
        item = GroceryItem.objects.get(pk=item_id)
        if item:
            tags = parse_tag_input(request.POST['name'])
            [Tag.objects.add_tag(item, tag) for tag in tags]

            json = simplejson.dumps({ 'tags' : tags, 'id' : item_id })
            return HttpResponse(json, mimetype='application/json')

    raise Http404()

@login_required
def remove_tag(request, item_id=None, tag_name=None):
    if request.method == 'POST':
        item = GroceryItem.objects.get(pk=item_id)
        if item and tag_name:
            Tag.objects.remove_tag(item, tag_name)
            item.save()
            
            return HttpResponse()

    raise Http404()

@login_required
def view_tag(request, item_id=None, tag_name=None):
    if request.method == 'POST':
        item = GroceryItem.objects.get(pk=item_id)
        tag = tag_name

        html = render_to_string('grocheris/tag.html',
                                locals())
        json = simplejson.dumps({ 'html' : html, 'id' : item_id })
        return HttpResponse(json, mimetype='application/json')

    raise Http404()
