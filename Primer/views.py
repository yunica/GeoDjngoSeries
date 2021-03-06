from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from io import open
from Primer.models import DelitosMuni, Prueba, Tipicidad
import csv
from geopy import Nominatim
from datetime import date
from django.contrib.gis.geos import GEOSGeometry
import os
from django.conf import settings

path = os.path.join(settings.BASE_DIR, 'static/final.csv')


class index(TemplateView):
    template_name = 'Primer/index.html'


def sectores(request):
    obj = serialize('geojson', DelitosMuni.object.filter(referenciado=True))
    return HttpResponse(obj, content_type='json')


def mencionar(request):
    url = path
    with open(url) as csvarchivo:
        entrada = csv.reader(csvarchivo)
        # DELITO, DIRECCION, CANTIDAD, ZONA, SUB_ZONA, SUB_ZONA_1, SUB_ZONA_2, MES, SUBURB = next(entrada)
        next(entrada)
        geolocator = Nominatim()
        for i in entrada:
            idfalso, DELITO, DIRECCION, CANTIDAD, ZONA, SUB_ZONA, SUB_ZONA_1, SUB_ZONA_2, MES, SUBURB = i
            try:
                location = geolocator.geocode(str(DIRECCION + " , San Juan Bautista "), timeout=5)
            except Exception:
                print("Direccion no encontrada " + DIRECCION)

            # location = geolocator.geocode(str(DIRECCION + " , San Juan Bautista "), timeout=10)
            for j in range(0, int(CANTIDAD)):
                delitomuni = DelitosMuni(
                    idfalso=int(idfalso),
                    delito=str(DELITO),
                    direccion=str(DIRECCION),
                    cantidad=int(CANTIDAD),
                    zona=str(ZONA),
                    subzona=str(SUB_ZONA),
                    subzona1=str(SUB_ZONA_1),
                    subzona2=str(SUB_ZONA_2),
                    mes=date(year=2017, month=int(MES), day=2))

                if location:
                    delitomuni.lat = float(location.latitude)
                    delitomuni.lng = float(location.longitude)
                    delitomuni.punto = GEOSGeometry(
                        'POINT(%s %s), 4326' % (
                            float(location.longitude), float(location.latitude)))
                    delitomuni.nuevadireccion = str(location.address)
                    delitomuni.referenciado = True
                else:
                    delitomuni.referenciado = False

                delitomuni.save()

    return render(request, 'Primer/resultado.html',
                  {'muni': DelitosMuni.object.all(),
                   'sinrefe': DelitosMuni.object.filter(referenciado=False),
                   'conrefe': DelitosMuni.object.filter(referenciado=True)})


def prueba(request):
    for i in DelitosMuni.object.all():
        try:
            j = Tipicidad.objects.get(nombre__exact=i.delito)
        except Exception:
            tipo = Tipicidad(nombre=i.delito)
            j = tipo.save()

        i.idfalso = int(j.id)
        i.save()

    return render(request, 'Primer/resultado.html',
                  {'muni2': DelitosMuni.object.all().order_by(),
                   'tipo': Tipicidad.objects.all()})
