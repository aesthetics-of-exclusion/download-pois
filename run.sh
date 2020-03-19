#!/usr/bin/env bash

AMENITIES="-a bar -a biergarten -a cafe -a fast_food -a food_court -a ice_cream -a pub -a restaurant
  -a library -a toy_library -a bicycle_rental -a boat_rental -a car_rental -a car_wash -a fuel
  -a atm -a bank -a bureau_de_change -a clinic -a dentist -a doctors -a pharmacy -a social_facility
  -a veterinary -a arts_centre -a brothel -a casino -a cinema -a community_centre -a gambling
  -a nightclub -a planetarium -a social_centre -a stripclub -a studio -a swingersclub -a theattre
  -a childcare -a conference_centre -a crematorium -a internet_cafe -a marketplace -a monastery
  -a photo_booth -a place_of_worship -a post_depot -a post_office"
SHOPS=""

./download-pois.py $AMENITIES $SHOPS ./data/amsterdam-boundary.geojson | ../poi-geojson-simplifier/index.js > \
  ./data/amsterdam-pois.geojson
./download-pois.py $AMENITIES $SHOPS ./data/brooklyn-boundary.geojson | ../poi-geojson-simplifier/index.js > \
  ./data/brooklyn-pois.geojson
./download-pois.py $AMENITIES $SHOPS ./data/berlin-boundary.geojson | ../poi-geojson-simplifier/index.js > \
  ./data/berlin-pois.geojson
