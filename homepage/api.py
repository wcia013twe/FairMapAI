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

def drawMap(state_data, target_id):

    try:
        # Convert the data into a DataFrame and create a GeoDataFrame
        state_df = pd.DataFrame.from_records(state_data)

        # Check if 'the_geom' column exists
        if "the_geom" not in state_df.columns:
            raise ValueError("The 'the_geom' column is missing from the data.")
        
        # Convert 'the_geom' column into geometries and create a GeoDataFrame
        state_df['geometry'] = state_df['the_geom'].apply(shape)
        state_gdf = gpd.GeoDataFrame(state_df, geometry='geometry')

        # Filter the target district using the provided ID (assuming 'cd116fp' is the column)
        target_district = state_gdf[state_gdf['cd116fp'] == target_id]

        # Plot the map
        fig, ax = plt.subplots(1, 1, figsize=(8, 8))

        # Plot all districts with light gray outlines
        state_gdf.boundary.plot(ax=ax, color='black', linewidth=0.5, alpha=0.3)

        # Highlight the specific district in red
        if not target_district.empty:
            target_district.plot(ax=ax, color='red', edgecolor='black', linewidth=1, alpha=0.7)
        else:
            print(f"No district found with ID '{target_id}'.")

        # Save the map to the static folder
        map_image_path = 'homepage/static/homepage/district_map.png'
        plt.savefig(map_image_path, bbox_inches='tight', pad_inches=1)
        plt.close(fig)  # Release memory

        # Return the relative path for template rendering
        return 'homepage/district_map.png'

    except Exception as e:
        print(f"Error drawing map: {e}")
        return None  # Return None if the map generation fails

