"""
input = {
    'a': 1,
    'b': [2, 3, 4],
    'c': {'d': 5, 'e': 6}
}
# Expected output:
# {'a': 1, 'b_0': 2, 'b_1': 3, 'b_2': 4, 'c_d': 5, 'c_e': 6}
"""


def flatten(d, parent_key=''):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}_{k}" if parent_key else str(k)
        if isinstance(v, dict):
            items.extend(flatten(v, new_key).items())
        elif isinstance(v, list):
            for i, value in enumerate(v):
                items.extend(flatten({str(i):value}, new_key).items())
        else:
            items.append((new_key, v))
    return dict(items)

input = {
     'a': 1,
    'b': [2, 3, 4],
    'c': {'d': 5, 'e': 6}
}
print(flatten(input, parent_key=''))
        
