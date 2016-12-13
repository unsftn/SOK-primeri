from d3_primeri import prodavnica_view
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^ucitavanje/plugin/(?P<id>([a-z]+|[_])+)$', views.ucitavanje_plugin, name="ucitavanje_plugin"),
    url(r'^primer1$', views.primer1, name="primer1"),
    url(r'^primer2$', views.primer2, name="primer2"),
    url(r'^primer3$', views.primer3, name="primer3"),

    url(r'^primer4$', views.primer4, name="primer4"),


    url(r'^primer/prodavnica/force/layout$', prodavnica_view.foce_layout, name="prodavnica_force_layout"),
    url(r'^primer/prodavnica/tree/layout$', prodavnica_view.tree_layout, name="prodavnica_tree_layout"),

    url(r'^primer/pan/zoom$', views.primerPanZoom, name="primerPanZoom"),
]