#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
import folium
from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    start_coords = (36.05, 120.40)
    folium_map = folium.Map(location=start_coords,zoom_start=13)
    return folium_map._repr_html_()

# if ‘__main__' == __name__:
#     app.run(debug=True)
