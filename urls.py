from django.conf.urls.defaults import *

urlpatterns = patterns('',
                       (r'^$', 'grocheris.views.index'),
                       (r'^stock/$', 'grocheris.views.view_in_stock'),
                       (r'^shop/$', 'grocheris.views.view_shopping_list'),
                       (r'^add_item/$', 'grocheris.views.add_item'),
                       (r'^item/(?P<item_id>\d+)/$', 'grocheris.views.view_item'),
                       (r'^item/(?P<item_id>\d+)/buy/$', 'grocheris.views.buy_item'),
                       (r'^item/(?P<item_id>\d+)/low/$', 'grocheris.views.low_item'),
                       (r'^item/(?P<item_id>\d+)/out/$', 'grocheris.views.out_item'),
                       (r'^item/(?P<item_id>\d+)/tag/$', 'grocheris.views.tag_item'),
                       (r'^item/(?P<item_id>\d+)/vote/$', 'grocheris.views.vote'),
                       )

