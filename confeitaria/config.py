config_dict = {}

def get(key):
    return config_dict[key] if key in config_dict else None

def set(key, value):
    config_dict[key] = value

def clear():
    config_dict.clear()
