from dataclasses import dataclass
import datetime

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

def _to_snake_case(text):
    '''
        Convert Text from CamelCase to snake_case
    '''
    return ''.join([e if e.islower() else '_' + e.lower() for e in text])

def from_json(dic):
    '''
        Converts the passed dictionaries keys from snake case to camel case
        while preserving the values
    '''
    return dict(
      [(_to_snake_case(k), str(dic[k])) for k in dic.keys()])