#!/usr/bin/env python3

import argparse
import json
import pprint
from shapely.geometry import shape

from pois import create_poi_gdf

parser = argparse.ArgumentParser('Download POIs from OpenStreetMap')
parser.add_argument('input', help='GeoJSON file with polygon boundary')
parser.add_argument('-a', '--amenity', action='append',
                    dest='amenities', default=None,
                    help='OSM amenity tags to download (default is all)')
parser.add_argument('-s', '--shop', action='append',
                    dest='shops', default=None,
                    help='OSM shop tags to download (default is all)')

args = parser.parse_args()

with open(args.input) as fd:
    json_data = json.load(fd)

    polygon = shape(json_data)

    gdf = create_poi_gdf(polygon, shops=args.shops, amenities=args.amenities)

    geojson = json.loads(gdf.to_json())
    print(json.dumps(geojson, indent=4, sort_keys=True))
