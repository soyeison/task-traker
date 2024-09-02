import re

def validate_id(id):
    return bool(re.match(r'^\d+$', id))