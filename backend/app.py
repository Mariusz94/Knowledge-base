import os
import logging
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_restful import Api, Resource, reqparse
from models.db.postgresDB import PostgresDB
from models.services.logger import get_module_logger
import models.services.flask_service as flask_service

load_dotenv()

app = Flask(__name__)

parser = reqparse.RequestParser()
parser.add_argument('keywords', type=list)

@app.route('/', methods=['GET'])
def hello_server():
    return jsonify({"info": "Server works"}), 200

@app.route('/articles', methods=['GET'])
def get_articles():
    article_id = request.args.get("article_id", None)
    return flask_service.get_articles(db=postgresDB, article_id=article_id)

#TODO: z parametrem
# @app.route('/articles', methods=['GET'])
# def get_articles():
#     keywords = parser.parse_args()
#     return keywords
#     #return flask_service.get_articles(db=postgresDB, keywords=keywords)


@app.route('/articles', methods=['POST'])
def create_article():
    data = request.json
    return flask_service.create_article(db=postgresDB, data=data)


@app.route('/articles/<article_id>', methods=['PUT'])
def update_article(article_id):
    data = request.json
    return flask_service.update_article(db=postgresDB, article_id=article_id, data=data)


@app.route('/articles/<article_id>', methods=['DELETE'])
def delete_article(article_id):
    return flask_service.delete_article(db=postgresDB, article_id=article_id,article_table=article_table)


@app.route('/categories', methods=['GET'])
def get_category():
    category_id = request.args.get("category_id", None)
    return flask_service.get_categories(db=postgresDB, category_id=category_id)


@app.route('/categories', methods=['POST'])
def create_categories():
    data = request.json
    return flask_service.create_category(db=postgresDB, data=data)


@app.route('/categories/<category_id>', methods=['PUT'])
def update_categories(category_id):
    data = request.json
    return flask_service.update_category(db=postgresDB, category_id=category_id, data=data)

@app.route('/categories/<category_id>', methods=['DELETE'])
def delete_categories(category_id):
    return flask_service.delete_category(db=postgresDB, category_id=category_id,category_table=category_table)

@app.route('/comments', methods=['GET'])
def get_comment():
    article_id = request.args.get("article_id", None)
    author=request.args.get("author", None)
    return flask_service.get_comments(db=postgresDB, article_id=article_id,author=author,comment_table=comment_table)


@app.route('/comments', methods=['POST'])
def create_comments():
    data = request.json
    return flask_service.create_comment(db=postgresDB, data=data)


@app.route('/comments/<comment_id>', methods=['PUT'])
def update_comments(comment_id):
    data = request.json
    return flask_service.update_comment(db=postgresDB, comment_id=comment_id, data=data)

@app.route('/comments/<comment_id>', methods=['DELETE'])
def delete_comments(comment_id):
    return flask_service.delete_comment(db=postgresDB, comment_id=comment_id,comment_table=comment_table)

if __name__ == "__main__":
    logger = get_module_logger(mod_name=__name__, log_path='./logs/app_logs.log', lvl=logging.DEBUG)
    postgresDB = PostgresDB(db_host=os.environ.get("DB_HOST"), db_port=os.environ.get("DB_PORT"),
                            db_user=os.environ.get("POSTGRES_USER"), db_password=os.environ.get("POSTGRES_PASSWORD"),
                            db_name=os.environ.get("POSTGRES_DB"))
    try:
        article_table = postgresDB.get_table('article')
        category_table = postgresDB.get_table('category')
        comment_table = postgresDB.get_table('comment')
        relation_category_article_table = postgresDB.get_table('relation_category_article')

        logger.info('Got tables')
        app.run(host='0.0.0.0', port=5000)
    except Exception as e:
        logger.exception(e)
        logger.exception('Error, could not get tables from database')
