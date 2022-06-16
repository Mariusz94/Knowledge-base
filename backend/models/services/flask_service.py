import datetime
import json
import uuid
import pandas as pd
from flask import jsonify
from models.db.postgresDB import PostgresDB
from models.services import utils
from sqlalchemy import select, and_


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
        return jsonify({'Could not delete article'})
        raise Exception('Could not delete article')


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
        return jsonify({'Could not delete category'})
        raise Exception('Could not delete category')


def get_comments(db: PostgresDB, article_id, author, comment_table):
    if article_id is not None:
        query = select(comment_table.c.id,
                       comment_table.c.author,
                       comment_table.c.content,
                       comment_table.c.like_count,
                       comment_table.c.dislike_count,
                       comment_table.c.created_at,
                       comment_table.c.modified_at
                       ) \
            .where(comment_table.c.article_id == article_id)
    elif author is not None:
        query = select(comment_table.c.id,
                       comment_table.c.author,
                       comment_table.c.content,
                       comment_table.c.like_count,
                       comment_table.c.dislike_count,
                       comment_table.c.created_at,
                       comment_table.c.modified_at
                       ) \
            .where(comment_table.c.author == author)
    try:
        result = db.get_df_from_sql(query=query)
    except:
        return jsonify({'error': 'Could not get data from database'}), 400
    else:
        df = result.to_dict(orient='records')
        # df = df.astype({'created_at': 'int64', 'modified_at': 'int64'})
        return jsonify(df), 200


def create_comment(db: PostgresDB, data):
    data['id'] = uuid.uuid4()
    data['created_at'] = datetime.datetime.now()
    data['modified_at'] = datetime.datetime.now()
    data['like_count'] = 0
    data['dislike_count'] = 0
    df = pd.DataFrame(data=data, columns=utils.comment_columns, index=[0])
    try:
        db.create(table_name='comment', df=df)
    except:
        return jsonify({'error': 'Could not create comment in database'}), 400
    else:
        return df.to_dict(orient='records')[0], 200


def update_comment(db: PostgresDB, comment_id, data):
    data['modified_at'] = datetime.datetime.now()
    try:
        db.update(table_name='comment', id=comment_id, data=data)
        return jsonify({"comment_id": comment_id})
    except:
        return jsonify({'Could not update comment'})
        raise Exception('Could not update comment')


def delete_comment(db: PostgresDB, comment_id, comment_table):
    try:
        db.delete(table_name='comment', id=comment_id, id_column=comment_table.c.id)
        return jsonify({"comment_id": comment_id})
    except:
        return jsonify({'Could not delete comment'})
        raise Exception('Could not delete comment')
