from sqlalchemy import create_engine
from shapely.wkb import dumps, loads
from shapely.geometry.multipolygon import MultiPolygon
import csv

# Connect to db
engine = create_engine("postgresql://postgres:jsa67267@localhost/cartodb_test", echo=False)
conn = engine.connect()

# Read csv, insert data to DB
header = None
with open('postal_codes.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    ll = 0
    
    for row in csv_reader:
        if ll == 0:
            header = row          
            ll += 1
        else:                  
            # Load wkb geometry
            gg = loads(row[0], hex=True)

            # Promote to multipolygon
            if gg.geom_type == 'Polygon':
            	gg = MultiPolygon([gg])
            
            sql='''INSERT INTO {t} ({columns}) VALUES (ST_GeomFromText('{v0}', 4326),{v1},{v2})'''.format(t='postal_codes', 
            	columns=','.join(header), 
            	v0=gg.wkt, v1=row[1], v2=row[2])
            conn.execute(sql)
            ll += 1

    print('''Inserted {} lines'''.format(ll))

