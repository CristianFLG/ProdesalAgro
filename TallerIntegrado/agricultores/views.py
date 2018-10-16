from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import (
    Agricultores,
    Aguasgrises
)

def list_agros(request):
    agro = Agricultores.objects.all()
    aguas = Aguasgrises.objects.all()
    context = {

        'agro': agro,
        'aguas': aguas
    }
    return render(request, 'agricultores/list.html', context)