
from django.http import JsonResponse
from places.models import Place
from django.shortcuts import render


def show_index(request):
    places = Place.objects.prefetch_related('images').all()
    descriptions = []
    context = {}
    for place in places:
        place_content = {
            'title': place.title,
            'imgs': [image.img.url for image in place.images.all()],
            'description_short': place.description_short,
            'description_long': place.description_long,
            'coordinates': {
                'lng': place.lng,
                'lat': place.lat
            }
        }
        descriptions.append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.lng, place.lat]
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.title,
                    "detailsUrl": "./static/places/moscow_legends.json"
                }
            }
        )
        places_description = {
            "type": "FeatureCollection",
            "features": descriptions
        }
        context['places_description'] = places_description
        print(context)

    return render(request, 'index.html', context=context)
