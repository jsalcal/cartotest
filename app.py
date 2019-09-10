# Custom sql functions
from sqlfunctions import *

# Simple Flask application
from flask import Flask, escape, request, json, jsonify

app = Flask(__name__)


# 127.0.0.1:5000/zipcode?code=28011
@app.route('/zipcode', methods=['GET', 'POST'])
def get_zipcode():
    """
    Given a zipcode as parameter, select all entities that belong to it
    """
    # Return a GeoJSON for the frontend to draw    
    try:
    	zcode = request.args.get('code')    
        return jsonify(get_zipcode_sql(zcode)), 200
    except Exception, e:
        return jsonify({'error':'Unable to process request {}'.format(e)}), 500      

if __name__ == "__main__":
    app.run(debug=True)