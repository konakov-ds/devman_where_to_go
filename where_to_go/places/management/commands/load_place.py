import logging
import os

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from places.models import Image, Place

logging.basicConfig()
logger = logging.getLogger('place_logger')
logger.setLevel(logging.INFO)


class Command(BaseCommand):
    help = 'Загрузка с помощью json описания места'

    def add_arguments(self, parser):
        parser.add_argument('place', type=str)

    def handle(self, *args, **options):
        try:
            response = requests.get(options['place'])
            response.raise_for_status()

            place_info = response.json()
            place, _ = Place.objects.update_or_create(
                title=place_info['title'],
                defaults={
                    'description_short': place_info['description_short'],
                    'description_long': place_info['description_long'],
                    'lng': place_info['coordinates']['lng'],
                    'lat': place_info['coordinates']['lat'],
                }
            )
            for img_id, img in enumerate(place_info['imgs']):
                image, _ = Image.objects.get_or_create(
                    place=place,
                    img_id=img_id,
                    name=f'{place.title}_{img_id}'
                )
                img_response = requests.get(img)
                img_response.raise_for_status()

                img_content = ContentFile(img_response.content)
                image.img.save(

                    os.path.basename(img_response.url),
                    img_content,
                    save=True
                )
            logger.info('Место успешно внесено в базу данных')
        except requests.HTTPError:
            logger.warning('Проблемы при загрузке json файла')
