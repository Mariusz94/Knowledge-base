import datetime
import json
import uuid
import pandas as pd
from flask import jsonify
from models.db.postgresDB import PostgresDB
from models.services import utils


def get_articles(db: PostgresDB, article_id):
    try:
        result = db.get(table_name="article", id=article_id)
    except:
        return jsonify({'error': 'Could not get data from database'}), 400
    else:
        df = result.to_dict(orient='records')
        # df = df.astype({'created_at': 'int64', 'modified_at': 'int64'})
        return jsonify(df), 200


def create_article(db: PostgresDB, data):
    data['id'] = uuid.uuid4()
    data['created_at'] = datetime.datetime.now()
    data['modified_at'] = datetime.datetime.now()
    data['like_count'] = 0
    data['dislike_count'] = 0
    df = pd.DataFrame(data=data, columns=utils.article_columns, index=[0])
    try:
        db.create(table_name='article', df=df)
    except:
        return jsonify({'error': 'Could not create article in database'}), 400
    else:
        return df.to_dict(orient='records')[0], 200


def update_article(db: PostgresDB, article_id, data):
    data['modified_at'] = datetime.datetime.now()
    try:
        db.update(table_name='article', id=article_id, data=data)
        return jsonify({"article_id": article_id})
    except:
        return jsonify({'Could not update article'})
        raise Exception('Could not update article')


def delete_article(db: PostgresDB, article_id, article_table):
    try:
        db.delete(table_name='article', id=article_id, id_column=article_table.c.id)
        return jsonify({"article_id": article_id})
    except:
        return jsonify({'Could not delete box'})
        raise Exception('Could not delete box')


def get_categories(db: PostgresDB, category_id):
    try:
        result = db.get(table_name="category", id=category_id)
    except:
        return jsonify({'error': 'Could not get data from database'}), 400
    else:
        df = result.to_dict(orient='records')
        # df = df.astype({'created_at': 'int64', 'modified_at': 'int64'})
        return jsonify(df), 200


def create_category(db: PostgresDB, data):
    data['id'] = uuid.uuid4()
    data['created_at'] = datetime.datetime.now()
    data['modified_at'] = datetime.datetime.now()
    df = pd.DataFrame(data=data, columns=utils.category_columns, index=[0])
    try:
        db.create(table_name='category', df=df)
    except:
        return jsonify({'error': 'Could not create category in database'}), 400
    else:
        return df.to_dict(orient='records')[0], 200


def update_category(db: PostgresDB, category_id, data):
    data['modified_at'] = datetime.datetime.now()
    try:
        db.update(table_name='category', id=category_id, data=data)
        return jsonify({"category_id": category_id})
    except:
        return jsonify({'Could not update category'})
        raise Exception('Could not update category')

def delete_category(db: PostgresDB, category_id, category_table):
    try:
        db.delete(table_name='category', id=category_id, id_column=category_table.c.id)
        return jsonify({"category_id": category_id})
    except:
        return jsonify({'Could not delete box'})
        raise Exception('Could not delete box')
