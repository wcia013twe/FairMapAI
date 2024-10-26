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

