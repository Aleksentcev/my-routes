import os
import gpxpy
import numpy
import pandas as pd
import haversine as hs
from pathlib import Path


dir_path = os.getcwd()
gpx_dir = Path(dir_path, 'data/')
csv_dir = Path(dir_path, 'csv_data/')


def haversine_distance(lat1, lon1, lat2, lon2):
    distance = hs.haversine(
        point1=(lat1, lon1),
        point2=(lat2, lon2),
        unit=hs.Unit.METERS
    )
    return numpy.round(distance, 2)


def process_gpx_to_csv(file):
    with open(file, 'r') as gpx_file:
        gpx = gpxpy.parse(gpx_file)
    track = gpx.tracks[0]
    segment = track.segments[0]
    data = []
    for point_idx, point in enumerate(segment.points):
        data.append([
            point.longitude,
            point.latitude,
            point.elevation,
            point.time,
            segment.get_speed(point_idx)
        ])
        columns = ['Longitude', 'Latitude', 'Altitude', 'Time', 'Speed']
    gpx_df = pd.DataFrame(data, columns=columns)
    distances = [numpy.nan]
    for i in range(len(gpx_df)):
        if i == 0:
            continue
        else:
            distances.append(haversine_distance(
                lat1=gpx_df.iloc[i - 1]['Latitude'],
                lon1=gpx_df.iloc[i - 1]['Longitude'],
                lat2=gpx_df.iloc[i]['Latitude'],
                lon2=gpx_df.iloc[i]['Longitude']
            ))
    gpx_df['Distance'] = distances
    csv_file_name = os.path.basename(file).replace('.gpx', '.csv')
    csv_file_path = os.path.join(csv_dir, csv_file_name)
    gpx_df.to_csv(csv_file_path, index=False)
    print(f'Файл {file} успешно конвертирован в {csv_file_path}.')


def convert_all_gpx_files(path):
    for entry in os.scandir(gpx_dir):
        if entry.is_file() and entry.name.endswith('.gpx'):
            process_gpx_to_csv(entry)
    print('Конвертация завершена!')


convert_all_gpx_files(gpx_dir)
