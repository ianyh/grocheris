from django.conf.urls.defaults import *

urlpatterns = patterns('grocheris.views',
                       (r'^$', 'index'),
                       (r'^stock/$', 'view_in_stock'),
                       (r'^shop/$', 'view_shopping_list'),
                       (r'^add_item/$', 'views.add_item'),
#                       (r'^item/(?P<item_id>\d+)/$', 'view_item'),
                       (r'^item/(?P<item_id>\d+)/buy/$', 'buy_item'),
                       (r'^item/(?P<item_id>\d+)/low/$', 'low_item'),
                       (r'^item/(?P<item_id>\d+)/out/$', 'out_item'),
#                       (r'^item/(?P<item_id>\d+)/tag/$', 'tag_item'),
#                       (r'^item/(?P<item_id>\d+)/vote/$', 'vote'),
                       )

