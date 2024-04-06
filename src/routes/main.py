from flask import request, jsonify, redirect
from flask import Blueprint
from src.services.main import ServicerCreateShortLink,ServiceGetStats,ServiceGetUrlFromShortCode
from src.library.db_connector.main import RepositoryShortURL
from src.library.db_connector.main import DBConnector
from src.library.db_connector.models import ShortURL
from src.library.logger.main import Logger

routes = Blueprint('routes', __name__)

USER = 'production'

@routes.route("/", methods=["GET"])
def liveness():
    return jsonify('I am a live!!')

@routes.route("/shorten", methods=["POST"])
def create_shortcode():
    Logger.emit('Starting shorten route')
    data = request.environ['data']
    url = data['url']
    if 'shortcode' in data:
        short_code = data['shortcode']
    else:
        short_code = None
    Logger.emit('Data from call got')
    service = ServicerCreateShortLink(url,RepositoryShortURL(DBConnector(USER,ShortURL)),short_code)
    Logger.emit('Running route')
    result = service.run()
    return jsonify({"shortcode":result}), 201
@routes.route("/<shortcode>", methods=["GET"])
def calc_square(shortcode):
    service = ServiceGetUrlFromShortCode(RepositoryShortURL(DBConnector(USER,ShortURL)),shortcode)
    result = service.run()
    return redirect(result, code=302)
@routes.route("/<shortcode>/stats", methods=["GET"])
def get_stats(shortcode):
    service = ServiceGetStats(RepositoryShortURL(DBConnector(USER,ShortURL)),shortcode)
    result = service.run()
    return jsonify(result), 200