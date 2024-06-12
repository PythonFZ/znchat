from flask import jsonify, Blueprint

main = Blueprint("main", __name__)


@main.route("/hello", methods=["GET"])
def hello():
    return jsonify(message="Hello, World!")
