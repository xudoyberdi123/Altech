import ast
import json
from contextlib import closing

from django.db import connection

from base.utils.db import dictfetchone
from tg.models import default_log


def get_log(user_id):
    sql = 'select user_id, messages from tg_log where user_id=%s'
    with closing(connection.cursor()) as cursor:
        cursor.execute(sql, [user_id])
        data = dictfetchone(cursor)
        if data:
            result = ast.literal_eval(data.get('messages', {}))
        else:
            result = None

    return result


def create_log(user_id):
    data = {'state': 0}
    sql = f'''
        insert into tg_log (messages, user_id) 
        values ('{json.dumps(data)}', {user_id})
        '''

    with closing(connection.cursor()) as cursor:
        cursor.execute(sql)
        connection.commit()

    return get_log(user_id)


def change_log(user_id, log):
    sql = f'''
    update tg_log set messages='{json.dumps(log)}'
    where user_id=%s
    '''

    with closing(connection.cursor()) as cursor:
        cursor.execute(sql, [user_id])
        connection.commit()

    return get_log(user_id)


def clear_log(user_id):
    data = {'state': 1}
    sql = f'''
    update tg_log set messages='{json.dumps(data)}'
    where user_id=%s
    '''

    with closing(connection.cursor()) as cursor:
        cursor.execute(sql, [user_id])
        connection.commit()

    return get_log(user_id)


def get_user(user_id):
    sql = f'select user_id, menu_log from tg_user where user_id=%s'

    with closing(connection.cursor()) as cursor:
        cursor.execute(sql, [user_id])
        data = dictfetchone(cursor)
        if data:
            result = data
        else:
            result = None

    return result


def create_user(user_id):
    sql = f"""
    insert into tg_user (user_id)
    values ({user_id})
    """

    with closing(connection.cursor()) as cursor:
        cursor.execute(sql)
        connection.commit()

    return get_user(user_id)


def change_menu(user_id, menu):
    sql = """
        update tg_user
        set menu_log=%s
        where user_id=%s
    """

    with closing(connection.cursor()) as cursor:
        cursor.execute(sql, [menu, user_id])
        connection.commit()

    return get_user(user_id)
