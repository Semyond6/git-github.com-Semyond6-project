from django.db import models
from django_admin_geomap import GeoItem

class Subjects(models.Model, GeoItem):

    address = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=50)
    country = models.CharField(max_length=255)
    federal_district = models.CharField(max_length=255)
    region_type = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    area_type = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    city_type = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    settlement_type = models.CharField(max_length=255)
    settlement = models.CharField(max_length=255)
    kladr_id = models.CharField(max_length=255)
    fias_id = models.CharField(max_length=255)
    fias_level = models.CharField(max_length=255)
    capital_marker = models.CharField(max_length=255)
    okato = models.CharField(max_length=255)
    oktmo = models.CharField(max_length=255)
    tax_office = models.CharField(max_length=255)
    timezone = models.CharField(max_length=50)
    geo_lat = models.DecimalField(max_digits=10, decimal_places=7)
    geo_lon = models.DecimalField(max_digits=10, decimal_places=7)
    population = models.CharField(max_length=50)
    foundation_year = models.CharField(max_length=255)
    
    @property
    def geomap_longitude(self):
        return '' if self.geo_lon is None else str(self.geo_lon)

    @property
    def geomap_latitude(self):
        return '' if self.geo_lat is None else str(self.geo_lat)
    
class HistorySeartch(models.Model, GeoItem):
    source = models.CharField(max_length=255)
    result_seartch = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    country_iso_code = models.CharField(max_length=255)
    federal_district = models.CharField(max_length=255)
    region_fias_id = models.CharField(max_length=255)
    region_kladr_id = models.CharField(max_length=255)
    region_iso_code = models.CharField(max_length=255)
    region_with_type = models.CharField(max_length=255)
    city_type = models.CharField(max_length=255)
    city_type_full = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    settlement_type = models.CharField(max_length=255)
    settlement = models.CharField(max_length=255)
    street_type = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    house_type = models.CharField(max_length=255)
    house = models.CharField(max_length=255)
    kladr_id = models.CharField(max_length=255)
    fias_id = models.CharField(max_length=255)
    fias_level = models.CharField(max_length=255)
    capital_marker = models.CharField(max_length=255)
    okato = models.CharField(max_length=255)
    oktmo = models.CharField(max_length=255)
    tax_office = models.CharField(max_length=255)
    timezone = models.CharField(max_length=255)
    geo_lat = models.DecimalField(max_digits=10, decimal_places=7)
    geo_lon = models.DecimalField(max_digits=10, decimal_places=7)

    @property
    def geomap_longitude(self):
        return '' if self.geo_lon is None else str(self.geo_lon)

    @property
    def geomap_latitude(self):
        return '' if self.geo_lat is None else str(self.geo_lat)    