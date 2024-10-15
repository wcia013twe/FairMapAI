from django.shortcuts import render
from homepage.forms import QueryForm
import geopandas as gpd
from sodapy import Socrata
import matplotlib.pyplot as plt  # Import matplotlib for plotting
import shapely as shape

def index(request):
    return render(request, 'homepage/index.html', {})

def form(request):
    client = Socrata("data.ojp.usdoj.gov", 'MKr6oLp394fqNbl1acAjZSer0')
    form = QueryForm()
    gdf = None
    map_image = None  # Initialize variable to store map image path
    data = None

    if request.method == 'POST':
        form = QueryForm(request.POST)
        if form.is_valid():
            statefp = str(form.cleaned_data['statefp']).zfill(2)  # Format to 01 if single digit
            cd116fp = str(form.cleaned_data['cd116fp']).zfill(2)  # Format to 01 if single digit
            
            # Fetching data from Socrata API
            data = client.get("imsf-b5s7", statefp=statefp, cd116fp=cd116fp)

            # extract the GeoJSON from the data
            # # Step 2: Iterate through each feature (if there are multiple)
            # feature = data['features']
            #     # Step 3: Access the 'geometry' field
            # geometry = feature['geometry']
                
            # # Step 4: Extract the 'coordinates' from the 'geometry'
            # coordinates = geometry['coordinates']
            
            # # Print the extracted coordinates
            # print("Extracted Coordinates:", coordinates)

            # geometry=shape(the_geom)

            # # Step 4: Create a GeoDataFrame using the extracted geometry
            # gdf = gpd.GeoDataFrame({'geometry': [geometry]}, crs="EPSG:4326")

            # # Step 5: Plot the GeoDataFrame
            # fig, ax = plt.subplots()
            # gdf.plot(ax=ax, color='lightblue', edgecolor='black')


            # # Step 6: Save the plot as a PNG file
            # output_file = "geometry_plot.png"
            # plt.savefig(output_file, format='png', bbox_inches='tight')
                
            # plt.show()
            

    # Render the template with the necessary context
    return render(request, 'homepage/form.html', {'form': form, 'data': data})
