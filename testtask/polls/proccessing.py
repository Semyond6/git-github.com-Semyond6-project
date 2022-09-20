import csv
import io
from dadata import Dadata
from .models import Subjects, HistorySeartch
from testtask.settings import DADA_SECRET, DADA_TOKEN
from geopy import distance

def uploaded_file(file):
    csv_file = file.read().decode('utf-8')
    io_string = io.StringIO(csv_file)
    reader = csv.reader(io_string, delimiter=',')
    for row in reader:
        if row[0] != 'address':
            Subjects.objects.create(address=row[0], postal_code=row[1],
                                    country=row[2], federal_district=row[3],
                                    region_type=row[4], region=row[5],
                                    area_type=row[6], area=row[7],
                                    city_type=row[8], city=row[9],
                                    settlement_type=row[10],
                                    settlement=row[11],
                                    kladr_id=row[12],
                                    fias_id=row[13], fias_level=row[14],
                                    capital_marker=row[15],
                                    okato=row[16], oktmo=row[17],
                                    tax_office=row[18],
                                    timezone=row[19],
                                    geo_lat=row[20], geo_lon=row[21],
                                    population=row[22],
                                    foundation_year=row[23])

def update_history_seartch(address):
    HistorySeartch.objects.create(source=address['source'], result_seartch=address['result'], 
                                  postal_code=address['postal_code'], country=address['country'], 
                                  country_iso_code=address['country_iso_code'], federal_district=address['federal_district'],
                                  region_fias_id=address['region_fias_id'], region_kladr_id=address['region_kladr_id'],
                                  region_iso_code=address['region_iso_code'], region_with_type=address['region_with_type'],
                                  city_type=address['city_type'], city_type_full=address['city_type_full'],
                                  city=address['city'], settlement_type=address['settlement_type'],
                                  settlement=address['settlement'], street_type=address['street_type'],
                                  street=address['street'], house_type=address['house_type'],
                                  house=address['house'], kladr_id=address['kladr_id'],
                                  fias_id=address['fias_id'], fias_level=address['fias_level'],
                                  capital_marker=address['capital_marker'], okato=address['okato'],
                                  oktmo=address['oktmo'], tax_office=address['tax_office'],
                                  timezone=address['timezone'], geo_lat=address['geo_lat'],
                                  geo_lon=address['geo_lon'])
    last_entry = HistorySeartch.objects.latest('id')
    return last_entry

def address_verification(address_form, radius):
    dadata = Dadata(DADA_TOKEN, DADA_SECRET)
    dadata_address = dadata.clean(name="address", source=address_form)
    center_point = (float(dadata_address['geo_lat']), float(dadata_address['geo_lon']))
    last_entry = update_history_seartch(dadata_address)
    confirm_subjects = []
    confirm_subjects.append(last_entry)
    subjects = Subjects.objects.all()
    for subject in subjects:
        dis = distance.distance(center_point,
                                (subject.geo_lat, subject.geo_lon)).km
        if dis <= radius:
            confirm_subjects.append(subject)
    return confirm_subjects
