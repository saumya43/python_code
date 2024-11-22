"""
input = [
    {'a': 1, 'b': 2},
    {'c': 3, 'd': 4}
]
# Expected output:
# {'0_a': 1, '0_b': 2, '1_c': 3, '1_d': 4}
"""
def list_dict(d):
    flatten = {}
    for i, dict in enumerate(d):
            for k, v in dict.items():
                new_key =f"{i}_{k}"
                flatten[new_key] = v
    return flatten

input = [
{'a': 1, 'b': 2},
{'c': 3, 'd': 4}
]
print(list_dict(input))

