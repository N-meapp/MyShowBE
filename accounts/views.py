from django.shortcuts import render
from . models import *
from .utils import haversine
from django.http import Http404
# Create your views here.
def index(request):
    city_id = request.GET.get('city')
    cities = City.objects.all()

    # If a city is selected, filter theatres by that city
    if city_id:
        try:
            selected_city = City.objects.get(id=city_id)
            theatres = Theatre.objects.filter(city=selected_city)
        except City.DoesNotExist:
            raise Http404("City not found")
    else:
        theatres = Theatre.objects.all()  # Show all theatres if no city is selected

    return render(request, 'index.html', {
        'theatres': theatres,
        'cities': cities,
        'selected_city': city_id
    })
    # return render(request, 'index.html',{'city':city})

def nearest_theatre(request):
    # Get latitude and longitude from the query parameters
    user_lat = float(request.GET.get('lat'))  # Get latitude from query parameter
    user_lon = float(request.GET.get('lon'))  # Get longitude from query parameter

    theatres = Theatre.objects.all()

    # Initialize variables to track the nearest theatre
    nearest_theatre = None
    shortest_distance = float('inf')

    for theatre in theatres:
        # Calculate the distance to each theatre
        distance = haversine(user_lat, user_lon, theatre.latitude, theatre.longitude)
        
        # Update the nearest theatre if this one is closer
        if distance < shortest_distance:
            shortest_distance = distance
            nearest_theatre = theatre

    return render(request, 'index.html', {
        'nearest_theatre': nearest_theatre,
        'distance': shortest_distance
    })
