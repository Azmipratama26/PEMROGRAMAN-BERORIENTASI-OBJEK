from django.shortcuts import render
from django.http import HttpResponse
import datetime

TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "Templates").'
)

def index(request):
    today = datetime.datetime.now().date()
    return render(request, "index.html", {"today" : today})