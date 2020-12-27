import warnings
warnings.filterwarnings('ignore')

from flask import jsonify, request, Blueprint
from flask_cors import cross_origin
from utils.utils import read_from_pkl
from utils import serv_utils
import configs as cfg

serv_routes = Blueprint('server_routes', __name__)

def get_routes() -> Blueprint:
    return serv_routes

# Reading the dataframe
df = read_from_pkl([
    cfg.PROJECT_SETTINGS.get('DATA_DIR'),
    cfg.PROJECT_SETTINGS.get('DATA_FILE')
])
# Reading the description
attrs_desc = read_from_pkl([
    cfg.PROJECT_SETTINGS.get('DATA_DIR'),
    cfg.PROJECT_SETTINGS.get('DESC_FILE')
])

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

@cross_origin
@serv_routes.route('/all', methods=['GET'])
def get_all():
    result = serv_utils.get_all_hero_details(df)
    return jsonify({
        'RESPONSE': result,
        'REQUEST': None,
        'Timestamp': serv_utils.get_timestamp()
    })

@cross_origin
@serv_routes.route('/all_names', methods=['GET'])
def get_all_names():
    result = serv_utils.get_all_hero_names(df)
    return jsonify({
        'RESPONSE': result,
        'REQUEST': None,
        'Timestamp': serv_utils.get_timestamp()
    })

@cross_origin
@serv_routes.route('/desc', methods=['GET'])
def get_desc():
    result = serv_utils.get_attr_desc(df, attrs_desc)
    return jsonify({
        'RESPONSE': result,
        'REQUEST': None,
        'Timestamp': serv_utils.get_timestamp()
    }), 200

@cross_origin
@serv_routes.route('/order/', methods=['POST'])
def order_by_attr():
    req = request.get_json()
    result = serv_utils.order_by_attr(df, req)
    return jsonify({
        'RESPONSE': result,
        'REQUEST': req,
        'Timestamp': serv_utils.get_timestamp()
    })