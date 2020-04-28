# Download POIs

Python script to download POIs in a specified boundary from [OpenStreetMap](https://www.openstreetmap.org/).

First, create a Python 3 virtual environment and install dependencies:

    python3 -m venv env
    pip install -r requirements.txt

Then, activate the virtual environment:

    source ./env/bin/activate.fish

To download POIs from a specific region, supply a GeoJSON polygon as the command line argument:

    ./download_pois.py ./data/amsterdam-boundary.geojson \
    > ./data/amsterdam-pois.geojson

Use [`poi-geojson-simplifier`](https://github.com/aesthetics-of-exclusion/poi-geojson-simplifier) to simplify the resulting GeoJSON file and decrease the file size:

    ./download_pois.py ./data/amsterdam-boundary.geojson \
    | ../poi-geojson-simplifier/index.js \
    > ./data/amsterdam-pois.geojson

To download POIs for all cities in this repository, run:

    ./run.sh
