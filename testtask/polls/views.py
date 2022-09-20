from urllib import request
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import View

from .forms import UploadFileForm, AddressForm
from django_admin_geomap import geomap_context

from .models import Subjects
from .proccessing import uploaded_file, address_verification

def Home(request):
    return render(request, 'home.html')

class DownloadCSV(View):
    def get(self, request):
        csv_form = UploadFileForm()
        return render(request, 'download_csv.html',
                      {'csv_form': csv_form})

    def post(self, request):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/')
        else:
            form = UploadFileForm()
            return render(request, 'download_csv.html', {'form': form})
        
class SearchAddress(View):
    def get(self, request):
        address_form = AddressForm()
        return render(request, 'search_address.html',
                      {'addressandredius_form': address_form})
 
    def post(self, request):
        form = AddressForm(request.POST)
        if form.is_valid():
            address_list = address_verification(form.data['address'], int(form.data['radius']))
            return render(request, 'search_address.html', geomap_context(address_list))
        else:
            form = AddressForm()
            return render(request, 'search_address.html', {'form': form})