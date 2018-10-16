from django.conf.urls import url

from . import views


urlpatterns = [
    url(
        regex=r'^agricultores/$',
        view=views.list_agros,
        name='list'
    )
]