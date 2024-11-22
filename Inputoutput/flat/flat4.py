"""
input = {
    1: {'a': 10},
    2: {'b': 20},
    3: {'c': 30}
}
# Expected output:
# {'1_a': 10, '2_b': 20, '3_c': 30}
"""
def flat_dict(d):
    flatten = {}
    for k , v in d.items():
        for k1, v1 in v.items():
            new_key = f"{k}_{k1}"
            flatten[new_key] = v1
    return flatten

input = {
    1: {'a': 10},
    2: {'b': 20},
    3: {'c': 30}
}
print(flat_dict(input))   

