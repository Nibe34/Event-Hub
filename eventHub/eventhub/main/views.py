from django.shortcuts import render
from events.models import Event
from main.utils import FilterManager

# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def main_page(request):
    events = Event.objects.all()
    events = FilterManager.apply_filters(events, request, ['name', 'location'])
    return render(request, 'main/index.html', {'events': events})