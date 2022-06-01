from flask import jsonify
from models.db.postgresDB import PostgresDB


def get_articles(db: PostgresDB, article_id):
    try:
        result = db.get(table_name="article", id=article_id)
    except:
        return jsonify({'error': 'Could not get data from database'}), 400
    else:
        df = result.to_dict(orient='records')
        df = df.astype({'created_at': 'int64', 'modified_at': 'int64'})
        return jsonify(df), 200
    
def create_article(db: PostgresDB, data):
    pass

def update_article(db: PostgresDB, article_id, data):
    pass

def delete_article(db: PostgresDB, article_id):
    pass