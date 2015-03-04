from django.shortcuts import render

import json


def index(request):
    env = str(request.environ)
    print env
    return render(request, 'PsyMap/index.html')


