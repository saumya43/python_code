"""
nested_dict = {
    'A': 1,
    'B': {
        'C': 2,
        'D': {
            'E': 3,
            'F': 4
        }
    },
    'G': 5,
    'H': {
        'I': 6,
        'J': {
            'K': 7,
            'L': 8
        }
    }
}

# Question:

Given the nested dictionary above, write a Python function that flattens it into a single-level dictionary. 
The keys of the flattened dictionary should be the path to the value in the nested dictionary, with keys 
separated by underscores. For example, the value 3 should have the key 'B_D_E' in the flattened dictionary.

Your function should work for arbitrarily nested dictionaries. The function signature should be:

def flatten_dict(nested_dict: dict) -> dict:
    # Your code here

Example output for the given nested_dict:
{
    'A': 1,
    'B_C': 2,
    'B_D_E': 3,
    'B_D_F': 4,
    'G': 5,
    'H_I': 6,
    'H_J_K': 7,
    'H_J_L': 8
}

Implement this function and explain your approach.
"""



class Flatten:
    def __init__(self, nested_dict, prefix):
        self.nested_dict = nested_dict
        self.prefix = prefix
        self.flatten = {}
    
    def flatten_dict(self, nested_dict, prefix):
        for key, value in nested_dict.items():
            new_key = f"{prefix}_{key}" if prefix else key
            if isinstance(value, dict):
                self.flatten.update(self.flatten_dict(value, new_key))
                
            else:
                self.flatten[new_key] = value
        return self.flatten

        
if  __name__ == "__main__":
    nested_dict = {
        'A': 1,
        'B': {
            'C': 2,
            'D': {
                'E': 3,
                'F': 4
            }
        },
        'G': 5,
        'H': {
            'I': 6,
            'J': {
                'K': 7,
                'L': 8
            }
        }
        }

    flat = Flatten(nested_dict, prefix='')
    flat_dict = flat.flatten_dict(nested_dict, prefix='')
    print(flat_dict)
