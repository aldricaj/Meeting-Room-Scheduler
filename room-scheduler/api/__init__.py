from psycopg2 import connect
from dataclasses import dataclass
import datetime

_conn = connect('dbname=meeting_scheduler_dev user=dev host=meeting-scheduler-dev.chzmyinhsoe1.us-east-2.rds.amazonaws.com password=Sherman01')

def run_query(query, parameters=None, return_class=None):
    result = None
    cursor = _conn.cursor()   
    cursor.execute(query, parameters)
    result = []
    for row in cursor:
        if return_class:
            result.append(return_class(*row))
        else:
            result.append(row)
    cursor.close()

    return result



@dataclass
class Event:
    meeting_id:int
    start: datetime.datetime
    end: datetime.datetime
    title: str
    room_number: str
    owner_username: str

def _to_camel_case(text):
    '''
        Converts text from snake_case to camelCase
    '''
    text = text.split('_')
    return text[0] + ''.join([e.title() for e in text[1:]])

def to_json(dic):
    '''
        Converts the passed dictionaries keys from snake case to camel case
        while preserving the values
    '''
    return dict(
      [(_to_camel_case(k), str(dic[k])) for k in dic.keys()])
