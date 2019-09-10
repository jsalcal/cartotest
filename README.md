Solution - Joan Sala Calero
Time Estimation - 4h30min

1) Install PostgresSQL 11 + PostGIS 2.5 extension

2) Enable PostGIS and create geoDB 'cartodb_test' with the SQL script createDB.sql 
Two tables
One of them contains a geometry column

3) Created pip virtualenv 'cartodb_test' with packages:

Click==7.0
Flask==1.1.1
itsdangerous==1.1.0
Jinja2==2.10.1
MarkupSafe==1.1.1
psycopg2==2.8.3
Shapely==1.6.4.post2
SQLAlchemy==1.3.8
Werkzeug==0.15.6

4) Insert the two csv into two different tables using the script insertDB_postal_codes.py and insertDB_paystats.py
- WKB geometry Multipolygon with EPSG 4326.
- Forced polygons into multipolygons for practical reasons.

5) Write simple Flask app to serve the REST requests
Note: On a production environment uwsgi is a better setup. 
This is just a test/stub, for now it can be run from the command line.

6) Implemented a sample endpoint with the following parameters:
http://127.0.0.1:5000/zipcode?code=28011

where code is the postal code and the reply is a GeoJSON containing the geometry and the statistics needed for the frontend as properties

{
  "coordinates": [
    [
      [
        [
          -3.73887017971504, 
          40.4340861521542
        ], 
        ...
        [
          -3.73887017971504, 
          40.4340861521542
        ]
      ]
    ]
  ], 
  "properties": {
    "25-34": {
      "female": 109806099.81921, 
      "male": 90043199.9641499
    }, 
    "35-44": {
      "female": 183468390.68848, 
      "male": 150459225.2312
    }, 
    "55-64": {
      "female": 124871434.61591, 
      "male": 99220436.47471
    }, 
    "<=24": {
      "female": 18811960.16982, 
      "male": 15188411.69719
    }, 
    ">=65": {
      "female": 89956301.1988299, 
      "male": 81590935.7506801
    }
  }, 
  "type": "MultiPolygon"
}
