from flask import Flask, jsonify, request
from flask_cors import CORS
from integrate import integrate
import logging

app = Flask(__name__)
CORS(app)


@app.errorhandler(Exception)
def handle_exception(e):
    logging.critical(e, exc_info=True)
    return {'error': 'Something went wrong :('}, 500


@app.route("/integration", methods=["POST"])
def post_integration():
    func = request.json['func']
    lower_limit = float(request.json['lower_limit'])
    upper_limit = float(request.json['upper_limit'])

    try:
        result = integrate(func, lower_limit, upper_limit)
    except SyntaxError:
        return {
            'error': 'Bad syntax for function, lower limit or upper limit'
        }, 400

    return jsonify({
        'func': func,
        'lowerLimit': lower_limit,
        'upperLimit': upper_limit,
        'result': '{:.6f}'.format(result),
    }), 200
