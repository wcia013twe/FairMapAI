import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt  # Import matplotlib for plotting
from shapely.geometry import shape

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

    try:
        # Convert data to DataFrame
        data_df = pd.DataFrame.from_records(data)

        # Check if 'the_geom' column exists
        if "the_geom" not in data_df.columns:
            raise ValueError("The 'the_geom' column is missing from the data.")

        # Create GeoDataFrame using the 'the_geom' column
        gdf = gpd.GeoDataFrame(data_df, geometry=data_df["the_geom"].apply(shape))

        # Plot the map and save it as an image
        fig, ax = plt.subplots(1, 1, figsize=(5, 5))
        gdf.plot(ax=ax, color='blue', edgecolor='black')

        # Save the image to the static folder
        map_image_path = 'homepage/static/homepage/district_map.png'
        plt.savefig(map_image_path, bbox_inches='tight', pad_inches=1)
        plt.close(fig)  # Release memory

        # Return the relative path for template rendering
        return 'homepage/district_map.png'
   
    except Exception as e:
            print(f"Error drawing map: {e}")
            return None  # Return None if the map generation fails

