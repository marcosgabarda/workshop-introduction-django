from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', "coffees.views.coffees_list", name="coffees_list"),
    url(r'^coffees/(?P<coffee_id>\d+)/', "coffees.views.coffee_details", name="coffee_details"),
    url(r'^coffees/new/', "coffees.views.coffee_create", name="coffee_create"),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
