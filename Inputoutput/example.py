dict = {
    'configs': [
        {
            'name': 'Main DB',
            'database_version': '1.9'
        },
        {
            'name': 'Backup DB',
            'settings': {
                'database_version': '1.8'
            }
        }
    ]
}

def find_key(dict, key_name):
    for k, v in dict.items:
        if isinstance(v, list):
        