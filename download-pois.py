#!/usr/bin/env python3

import argparse
import json
import pprint
from shapely.geometry import shape

from pois import create_poi_gdf

parser = argparse.ArgumentParser()
parser.add_argument("input", help="GeoJSON file with polygon boundary")
args = parser.parse_args()

with open(args.input) as fd:
    json_data = json.load(fd)

    polygon = shape(json_data)

    # amenities = [
    #   'cafe',
    #   'pub',
    #   'bar',
    #   'restaurant'
    # ]

    # shops = [
    #   'convenience',
    #   'bakery',
    #   'coffee',
    #   'health_food',
    #   'supermarket',
    #   'clothes'
    # ]

    gdf = create_poi_gdf(polygon)

    geojson = json.loads(gdf.to_json())
    print(json.dumps(geojson, indent=4, sort_keys=True))
