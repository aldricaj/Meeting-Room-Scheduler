from psycopg2 import connect
from dataclasses import dataclass
from .shared_models import *
import datetime

_conn = connect('dbname=meeting_scheduler_dev user=dev host=meeting-scheduler-dev.chzmyinhsoe1.us-east-2.rds.amazonaws.com password=Sherman01')

def run_query(query, parameters=None, return_class=None):
    result = None
    cursor = _conn.cursor()   
    cursor.execute(query, parameters)
    result = []
    try:
        for row in cursor:
            if return_class:
                result.append(return_class(*row))
            else:
                result.append(row)

        cursor.commit()
    finally:
        cursor.close()

    return result

