import datetime
import json
import uuid

import pandas as pd
from flask import jsonify
from models.db.postgresDB import PostgresDB
from models.services import utils

from sqlalchemy import select, and_
from flask import send_file


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
def db_to_txt(db: PostgresDB,article_table,relation_category_article_table,category_table,comment_table):
    query = select(article_table.c.id,
                   article_table.c.title,
                   article_table.c.content,
                   article_table.c.author) \
        .join(relation_category_article_table, article_table.c.id == relation_category_article_table.c.article_id)
    try:
        article_data = db.get_df_from_sql(query=query)
        print('Response has been sent')
    except:
        print('Could not get data from database')
        raise Exception('Could not get data from database')
    articles_ids = article_data['id'].to_list()

    query = select(relation_category_article_table.c.article_id.label("id"),
                   category_table.c.id.label("CategoryId"),
                   category_table.c.name) \
        .where(relation_category_article_table.c.article_id.in_(articles_ids)) \
        .join(category_table, category_table.c.id == relation_category_article_table.c.category_id)
    try:
        category_data = db.get_df_from_sql(query=query)
        print('Response has been sent')
    except:
        print('Could not get data from database')
        raise Exception('Could not get data from database')
    article_data = article_data.to_dict(orient='records')
    for article in article_data: article['categories'] = []
    for index, row in category_data.iterrows():
        category = {
            "name": row['name'],
        }
        for article in article_data:
            if article['id'] == row['id']:
                article['categories'].append(category)
                break

    query = select(comment_table.c.article_id.label("id"),
                   comment_table.c.id.label("commentId"),
                   comment_table.c.author,
                   comment_table.c.content)
    try:
        comment_data = db.get_df_from_sql(query=query)
        print('Response has been sent')
    except:
        print('Could not get data from database')
        raise Exception('Could not get data from database')
    for article in article_data: article['comments'] = []

    for index, row in comment_data.iterrows():
        comment = {
            "author": row['author'],
            "content": row['content'],
        }
        for article in article_data:
            if article['id'] == row['id']:
                article['comments'].append(comment)
                break
    txt=article_representation(article_data)
    text_file = open("articles.txt", "w")
    text_file.write(txt)
    text_file.close()
    return send_file('articles.txt', as_attachment=True)
    # return jsonify(article_data), 200
def comment_representation(comments:[]):
    comment_str=""
    for comment in comments:
        comment_str=comment_str+comment['author']+":"+comment['content']+"#!@-@!#"
    return comment_str

def category_representation(categories:[]):
    category_str=""
    for category in categories:
        category_str=category_str+category['name']+"#!@-@!#"
    return category_str

def article_representation(articles:[]):
    article_str=""
    articles_str=""
    comments=""
    categories=""
    for article in articles:
        if article['categories']:
            categories = category_representation(article['categories'])
        if article['comments']:
            comments = comment_representation(article['comments'])
            article_str=f"{article['title']}\n{article['author']}\n{article['content']}\n{categories}\n{comments}\n@!#!@\n"
        else:
            article_str = f"{article['title']}\n{article['author']}\n{article['content']}\n{categories}\n@!#!@\n"
        articles_str=articles_str+article_str
    return articles_str
