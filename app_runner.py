import os
import subprocess

from flask import Flask, render_template

is_convert_gpx_data_run = False
is_create_map_run = False

app = Flask(__name__, template_folder=os.getcwd())


@app.route('/')
def render_map():
    return render_template('map.html')


if __name__ == '__main__':
    if not is_convert_gpx_data_run:
        subprocess.call(['python', 'convert_gpx_data.py'])
        is_convert_gpx_data_run = True

    if not is_create_map_run:
        subprocess.call(['python', 'create_map.py'])
        is_create_map_run = True

    app.run(debug=True)
