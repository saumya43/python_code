"""
input = {
    'a': {'b': {'c': 1, 'd': 2}, 'e': 3},
    'f': {'g': 4}
}
# Expected output (depth=1):
# {'a_b': {'c': 1, 'd': 2}, 'a_e': 3, 'f_g': 4}
"""
def flat_list(d, max_depth, curr_depth=0, parent_key=''):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}_{k}" if parent_key else k
        if isinstance(v, dict) and curr_depth < max_depth:
            items.extend(flat_list(v, max_depth, curr_depth+1, new_key).items())
        else:
            items.append((new_key, v))
    return dict(items)

input = {
    'a': {'b': {'c': 1, 'd': 2}, 'e': 3},
    'f': {'g': 4}
}
print(flat_list(input, 2, 0, parent_key=''))