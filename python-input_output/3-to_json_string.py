import json

def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).
    
    Args:
    my_obj: The object to be serialized to JSON.
    
    Returns:
    A string containing the JSON representation of the object.
    """
    return json.dumps(my_obj)
