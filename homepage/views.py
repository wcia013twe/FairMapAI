from django.shortcuts import render
from homepage.forms import QueryForm
import geopandas as gpd
from sodapy import Socrata
import matplotlib.pyplot as plt  # Import matplotlib for plotting

def index(request):
    return render(request, 'homepage/index.html', {})

def form(request):
    client = Socrata("data.ojp.usdoj.gov", 'MKr6oLp394fqNbl1acAjZSer0')
    form = QueryForm()
    gdf = None
    map_image = None  # Initialize variable to store map image path

    if request.method == 'POST':
        form = QueryForm(request.POST)
        if form.is_valid():
            statefp = str(form.cleaned_data['statefp']).zfill(2)  # Format to 01 if single digit
            cd116fp = str(form.cleaned_data['cd116fp']).zfill(2)  # Format to 01 if single digit
            
            # Fetching data from Socrata API
            data = client.get("imsf-b5s7", statefp=statefp, cd116fp=cd116fp, limit=50)

            # Convert results to GeoDataFrame
            if data and 'features' in data and len(data['features']) > 0:
                # Convert the full GeoJSON data to GeoDataFrame
                gdf = gpd.GeoDataFrame.from_features(data['features'])

                gdf.to_png("homepage/static/homepage/district_boundary.png")
                
                fig, ax = plt.subplots(figsize=(10, 10))
                gdf.plot(ax=ax)
                # map_image_path = "homepage/static/homepage/district_boundary.png"
                # plt.savefig(map_image_path)
                # map_image ='homepage/district_boundary.png'

    # Render the template with the necessary context
    return render(request, 'homepage/form.html', {'form': form, 'gdf': gdf, 'map_image': map_image})
