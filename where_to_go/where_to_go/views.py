from django.http import JsonResponse
from django.urls import reverse
from places.models import Place
from django.shortcuts import get_object_or_404, render


def create_json_for_place(request, place_id):
    place = get_object_or_404(Place, id=place_id)
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
    return JsonResponse(
        data=place_content,
        json_dumps_params={
            'indent': 2,
            'ensure_ascii': False
        },
    )


def show_index(request):
    places = Place.objects.prefetch_related('images').all()
    descriptions = []
    context = {}
    for place in places:
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
                    "detailsUrl": reverse('show_place', args=[place.id])
                }
            }
        )
        places_description = {
            "type": "FeatureCollection",
            "features": descriptions
        }
        context['places_description'] = places_description

    return render(request, 'index.html', context=context)
