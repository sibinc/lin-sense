from app.core.config import cursor

def execute_query(query, params=None):
    cursor.execute(query, params)
    return cursor.fetchall()