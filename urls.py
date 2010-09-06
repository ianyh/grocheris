from django.conf.urls.defaults import *

urlpatterns = patterns('grocheris.views',
                       url(r'^$', 'view_all', name="index"),
                       url(r'^stock/$', 'view_in_stock', name='stock'),
                       url(r'^shop/$', 'view_shopping_list', name='shop'),
                       
                       url(r'^add_item/$', 'add_item', name='add_item'),
                       url(r'^add_tag/$', 'add_tag', name='add_tag'),
                       
                       url(r'^item/(?P<item_id>\d+)/$', 'view_item', name='view_item'),
                       url(r'^item/(?P<item_id>\d+)/buy/$', 'buy_item', name='buy'),
                       url(r'^item/(?P<item_id>\d+)/low/$', 'low_item', name='low'),
                       url(r'^item/(?P<item_id>\d+)/out/$', 'out_item', name='out'),
                       url(r'^item/(?P<item_id>\d+)/delete/$', 'delete_item', name='delete'),
                       url(r'^item/(?P<item_id>\d+)/tag/(?P<tag_name>.+?)/remove/$', 'remove_tag', name='remove_tag'),
                       url(r'^item/(?P<item_id>\d+)/tag/(?P<tag_name>.+?)/$', 'view_tag', name='view_tag'),
                       )

