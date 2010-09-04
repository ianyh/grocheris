from django.conf.urls.defaults import *

urlpatterns = patterns('grocheris.views',
                       (r'^$', 'index'),
                       url(r'^stock/$', 'view_in_stock', name='stock'),
                       url(r'^shop/$', 'view_shopping_list', name='shop'),
                       url(r'^add_item/$', 'add_item', name='add_item'),
                       url(r'^item/(?P<item_id>\d+)/buy/$', 'buy_item', name='buy'),
                       url(r'^item/(?P<item_id>\d+)/low/$', 'low_item', name='low'),
                       url(r'^item/(?P<item_id>\d+)/out/$', 'out_item', name='out'),
                       )

