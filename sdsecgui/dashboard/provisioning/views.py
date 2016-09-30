#_*_coding:utf-8_*_

from django.shortcuts import render


def provisioning(request):
    return render(request, 'provisioning/index.html', {})