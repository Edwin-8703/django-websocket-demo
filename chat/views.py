import os
from django.http import HttpResponse

def index(request):
    path = os.path.join(os.path.dirname(__file__), '..', 'templates', 'chat', 'index.html')
    with open(path) as f:
        return HttpResponse(f.read())