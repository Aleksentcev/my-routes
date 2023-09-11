import os
import folium
import pandas as pd
from pathlib import Path


dir_path = os.getcwd()
csv_dir = Path(dir_path, 'csv_data/')


route_map = folium.Map(
    location=[37.851013, 55.904415],
    zoom_start=13,
    tiles='OpenStreetMap',
    width=1024,
    height=600
)

for entry in os.scandir(csv_dir):
    if entry.is_file() and entry.name.endswith('.csv'):
        csv_file = os.path.join(csv_dir, entry)
        data_csv = pd.read_csv(csv_file)
        coordinates = [tuple(x) for x in data_csv[['Latitude', 'Longitude']].to_numpy()]
        folium.PolyLine(coordinates, weight=6).add_to(route_map)


route_map.save('map.html')
