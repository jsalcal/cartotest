from sqlalchemy import create_engine
import json

# Connect to db
engine = create_engine("postgresql://postgres:jsa67267@localhost/cartodb_test", echo=False)
conn = engine.connect()

def get_zipcode_sql(code):
    sql = '''SELECT ST_AsGeoJson(the_geom), code, id FROM postal_codes WHERE code = \'{cc}\''''.format(cc=code)
    res = conn.execute(sql)
    
    geoj = {}
    for r in res:
        geoj = json.loads(r[0])
        geoj['properties'] = { 
            '35-44' : {
                'female': get_age_group(code, '35-44', 'F'), 
                'male': get_age_group(code, '35-44', 'M')
            },
            '55-64' : {
                'female': get_age_group(code, '55-64', 'F'), 
                'male': get_age_group(code, '55-64', 'M')
            },
            '>=65' : {
                'female': get_age_group(code, '>=65', 'F'), 
                'male': get_age_group(code, '>=65', 'M')
            },
            '25-34' : {
                'female': get_age_group(code, '25-34', 'F'), 
                'male': get_age_group(code, '25-34', 'M')
            },
            '<=24' : {
                'female': get_age_group(code, '<=24', 'F'), 
                'male': get_age_group(code, '<=24', 'M')
            }
        }

    return geoj

def get_age_group(code, agegroup, gender):

    sql = '''SELECT SUM(amount) as total FROM paystats WHERE p_age = \'{aa}\' AND p_gender = \'{gg}\''''.format(
        aa=agegroup, gg=gender)
    res = conn.execute(sql)
    return res.fetchone()[0] # total
