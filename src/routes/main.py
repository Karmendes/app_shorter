from flask import jsonify
from flask import Blueprint

routes = Blueprint('routes', __name__)

@routes.route("/", methods=["GET"])
def liveness():
    return jsonify('I am a live!!')