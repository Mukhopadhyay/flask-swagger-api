import warnings
warnings.filterwarnings('ignore')

import datetime
from flask import json, jsonify, request, Blueprint
from flask_cors import cross_origin
from utils.utils import read_from_pkl
from utils import serv_utils
import configs as cfg

serv_routes = Blueprint('server_routes', __name__)

def get_routes() -> Blueprint:
    return serv_routes

# Reading the dataframe
df = read_from_pkl([cfg.DATA_DIR, cfg.DATA_FILE])

@cross_origin
@serv_routes.route('/', methods=['GET', 'POST'])
def index():
    return jsonify({
        'MSG': 'Working',
        'METHOD': request.method,
        'Timestamp': serv_utils.get_timestamp()
    }), 200

@cross_origin
@serv_routes.route('/heroes/<name>', methods=['GET'])
def get_heroes(name):
    result = serv_utils.get_hero_details(df, name)
    try:
        return jsonify({
            'RESPONSE': result,
            'REQUEST': name,
            'Timestamp': serv_utils.get_timestamp()
        }), 200
    except Exception as err:
        return jsonify({
            'RESPONSE': str(err),
            'REQUEST': name,
            'Timestamp': serv_utils.get_timestamp()
        }), 400