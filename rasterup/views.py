from django.shortcuts import render, HttpResponse
from .models import FilesUpload
from localtileserver import get_folium_tile_layer
from localtileserver import TileClient
from folium import Map
import folium
import glob
# import ee
# import datetime as dt
import os


def home(request):
    return render(request,'index.html')


# Create your views here.
def upload(request):
    if request.method == "POST":
        file2 = request.FILES["file"]
        document = FilesUpload.objects.create(file = file2)
        document.save()
        return HttpResponse("File is saved")
    return render(request, "upload.html")

def visual(request):
    # First, create a tile server from local raster file
    #data='media/odm_orthophoto.tif'
    # Create ipyleaflet tile layer from that server
    # m=folium.Map(location=[0,0], zoom_start = 10, max_zoom = 19)
    list_of_files = glob.glob('media/*.tif') # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    tile_client = TileClient(latest_file)
    t = get_folium_tile_layer(tile_client,name = 'image', max_zoom=24, show_loading=True)
    m = Map(location=tile_client.center(), maxNativeZoom = 19, max_zoom = 25)
    m.add_child(t)
    folium.TileLayer('openstreetmap').add_to(m)
    folium.TileLayer('stamenterrain').add_to(m)
    folium.LayerControl().add_to(m)
    mymap = m._repr_html_()
    context = {
    'mymap':mymap
    }
    return render(request, "viewing.html", context)
