from django.conf.urls import url
from . import views
from django.views.generic import ListView
from hms.models import *

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^hotels/', views.hotels_list, name='hotel_views'),
    url(r'^hotels/(?P<pk>\d+)$', ListView.as_view(model=Hotel, template_name='hms/hotel_list.html'))]
