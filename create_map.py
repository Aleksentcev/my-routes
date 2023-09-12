import os
import folium
import pandas as pd
from pathlib import Path

DIR_PATH = os.getcwd()
CSV_DIR = Path(DIR_PATH, 'csv_data/')
START_ROUTES_LOCATION = [55.90435, 37.85098]
M_IN_KM = 1000


def create_map_and_routes():
    route_map = folium.Map(
        location=START_ROUTES_LOCATION,
        zoom_start=12,
        tiles='OpenStreetMap',
        width=1920,
        height=1080
    )
    total_distance = 0
    for entry in os.scandir(CSV_DIR):
        if entry.is_file() and entry.name.endswith('.csv'):
            csv_file = os.path.join(CSV_DIR, entry)
            data_csv = pd.read_csv(csv_file)
            coordinates = [tuple(x) for x in data_csv[
                ['Latitude', 'Longitude']
            ].to_numpy()]
            distance_km = round(data_csv['Distance'].sum()/M_IN_KM, 2)
            popup_text = f"Дистанция: {distance_km} км"
            folium.PolyLine(
                coordinates, weight=6, popup=popup_text
            ).add_to(route_map)
            total_distance += distance_km
    folium.Marker(
        location=START_ROUTES_LOCATION,
        popup=f"Общая дистанция: {total_distance} км",
        icon=folium.Icon(
            color='blue', icon_color='white', icon='bicycle', prefix='fa'
        )).add_to(route_map)
    route_map.save('map.html')
    print('Карта и маршруты сгенерированы!')


if __name__ == '__main__':
    create_map_and_routes()
