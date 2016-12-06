from django.conf.urls import url

from . import views,artikli_view,prodavnica_view

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^kategorije$', views.lista_kategorija, name='lista_kategorija'),
    url(r'^artikli$', artikli_view.lista_artikala, name='lista_artikala'),
    url(r'^brisanje/artikla/(?P<id>[0-9]+)$', artikli_view.brisanje_artikla, name='brisanje_artikla'),
    url(r'^unos/artikla$', artikli_view.unos_artikla, name='unos_artikla'),
    url(r'^unos/artikla/(?P<id>[0-9]+)$', artikli_view.unos_artikla, name='unos_artikla_p'),
    url(r'^prodavnice', prodavnica_view.lista_prodavnica, name='lista_prodavnica'),
    url(r'^brisanje/prodavnice/(?P<id>[0-9]+)$', prodavnica_view.brisanje_prodavnice, name='brisanje_prodavnice'),
    url(r'^unos/prodavnice$', prodavnica_view.unos_prodavnice, name='unos_prodavnice'),
    url(r'^unos/prodavnice/(?P<id>[0-9]+)$', prodavnica_view.unos_prodavnice, name='unos_prodavnice_p'),
]