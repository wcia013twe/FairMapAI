from django.shortcuts import render
from homepage.forms import QueryForm
from sodapy import Socrata
from homepage.api import drawMap, printTable

def index(request):
    return render(request, 'homepage/index.html', {})

def form(request):
    client = Socrata("data.ojp.usdoj.gov", 'MKr6oLp394fqNbl1acAjZSer0')
    form = QueryForm()
    data_table = None
    map_path = None

    if request.method == 'POST':
        form = QueryForm(request.POST)
        if form.is_valid():
            statefp = str(form.cleaned_data['statefp']).zfill(2)  # Format to 01 if single digit
            cd116fp = str(form.cleaned_data['cd116fp']).zfill(2)  # Format to 01 if single digit
            # Fetching data from Socrata API
            data = client.get("imsf-b5s7", statefp=statefp, cd116fp=cd116fp)
            state_data = client.get("imsf-b5s7", statefp=statefp)

            data_table = printTable(data)
            map_path = drawMap(state_data, cd116fp)

    # Render the template with the necessary context
    return render(request, 'homepage/form.html', {
        'form': form, 
        'data_table': data_table,
        'map_path': map_path})
