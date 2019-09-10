from sqlalchemy import create_engine
import csv

# Connect to db
engine = create_engine("postgresql://postgres:jsa67267@localhost/cartodb_test", echo=True)
conn = engine.connect()

# Read csv, insert data to DB
header = None

with open('paystats.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    ll = 0
    
    for row in csv_reader:
        if ll == 0:
            header = row          
            ll += 1
        else:      
            sql='''INSERT INTO {t} ({columns}) VALUES ({v0},{v1},{v2},{v3},{v4},{v5})'''.format(t='paystats', 
            	columns=','.join(header), 
            	v0=row[0], v1="'"+row[1]+"'", v2="'"+row[2]+"'", v3="'"+row[3]+"'", v4=row[4], v5=row[5])
            conn.execute(sql)
            ll += 1

    print('''Inserted {} lines'''.format(ll))
