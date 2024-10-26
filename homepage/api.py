import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt  # Import matplotlib for plotting
import shapely as shape

def printTable(data):
    datat_df = None
    data_table = None

    # Convert the fetched data to a DataFrame and drop the geom
    datat_df = pd.DataFrame.from_records(data)
    df_without_the_geom = datat_df.drop(columns=["the_geom"], errors='ignore')

    #conver data frame to a HTML table
    data_table = df_without_the_geom.to_html(classes='table table-striped')

    return data_table

def drawMap(data):

    data_df = None

    # Convert the fetched data to a DataFrame and drop the geom
    data_df = pd.DataFrame.from_records(data)
    # Create a GeoDataFrame from the_geom
    gdf = gpd.GeoDataFrame(data_df, geometry=data_df["the_geom"].apply(shape))

    # Plot the map and save it as an image
    fig, ax = plt.subplots(1, 1, figsize=(10, 10))
    gdf.plot(ax=ax, color='blue', edgecolor='black')
    map_image_path = 'homepage/static/homepage/district_map.png'
    plt.savefig(map_image_path)
    plt.close(fig)  # Close the plot to release memory

    map_image = 'homepage/district_map.png'  # Relative path for template

