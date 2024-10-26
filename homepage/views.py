from django.shortcuts import render
from homepage.forms import QueryForm

from sodapy import Socrata


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
            
            # function to draw map

    # Render the template with the necessary context
    return render(request, 'homepage/form.html', {'form': form, 'data': data})
