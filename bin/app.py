import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask import abort
from flask.ext.pymongo import PyMongo
from ec2instancespricing import ec2instancespricing
import MongoJsonEncoder

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
mongo = PyMongo(app)
fileHandler = RotatingFileHandler('app.log')
fileHandler.doRollover()
fileHandler.setLevel(logging.INFO)
app.logger.addHandler(fileHandler)
log = logging.getLogger('werkzeug')
log.setLevel(logging.INFO)
log.addHandler(fileHandler)

#@app.route('/')
#def index():
#    db = mongo.db.ec2pricing
#    return MongoJsonEncoder.jsonify(db.reserved.find_one())

@app.route('/api/<string:type>', methods=['PUT'])
def update_db(type):
    if type not in ['ondemand', 'reserved']:
        abort(400)
    if type in 'reserved':
        prices = ec2instancespricing.get_ec2_reserved_instances_prices()
        if prices is None:
            abort(400)
        db = mongo.db.ec2pricing
        db.reserved.insert(prices)
        return MongoJsonEncoder.jsonify(prices)
    elif type in 'ondemand':
        prices = ec2instancespricing.get_ec2_ondemand_instances_prices()
        if prices is None:
            abort(400)
        db = mongo.db.ec2pricing
        db.ondemand.insert(prices)
        return MongoJsonEncoder.jsonify(prices)

@app.errorhandler(BaseException)
def internal_error(exception):
    app.logger.exception(exception)
    abort(500)

if __name__ == '__main__':
    app.run(debug=True)