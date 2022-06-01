import os
import logging
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS

from models.db.postgresDB import PostgresDB
from models.services.logger import get_module_logger
import models.services.flask_service as flask_service

load_dotenv()

app = Flask(__name__)

CORS(app, resources=r'/*')

@app.route('/', methods=['GET'])
def hello_server():
    return jsonify({"info" : "Server works"}), 200

@app.route('/articles', methods=['GET'])
def get_articles():
    id = request.args.get("id", None)
    return flask_service.get_articles(db=postgresDB, id=id)

@app.route('/articles', methods=['POST'])
def create_article():
    data = request.json
    return flask_service.create_article(db=postgresDB, data=data)

@app.route('/articles/<article_id>', methods=['DELETE'])
def delete_article(article_id):
    data = request.json
    return flask_service.update_article(db=postgresDB, id=article_id, data=data)

@app.route('/articles/<article_id>', methods=['DELETE'])
def delete_article(article_id):
    return flask_service.delete_article(db=postgresDB, id=article_id)


if __name__ == "__main__":
    logger = get_module_logger(mod_name=__name__, log_path='./logs/app_logs.log', lvl=logging.DEBUG)
    postgresDB = PostgresDB(db_host=os.environ.get("DB_HOST"), db_port=os.environ.get("DB_PORT"),
                            db_user=os.environ.get("DB_USER"), db_password=os.environ.get("DB_PASSWORD"),
                            db_name=os.environ.get("DB_NAME"))
    
    try:
        # TODO: get tables
        tablename_table = postgresDB.get_table('table_name')
        
        logger.info('Got tables')
        app.run(host='0.0.0.0', port=5000)
    except Exception as e:
        logger.exception(e)
        logger.exception('Error, could not get tables from database')
