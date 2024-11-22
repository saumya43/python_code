"""
company_data = {
    "company": {
        "name": "Acme Corporation",
        "founded": 2010,
        "active": True
    },
    "employees": [
        {
            "name": "John Smith",
            "position": "Developer",
            "skills": ["Python", "JavaScript", "Docker"],
            "contact": {
                "email": "john@acme.com",
                "phone": "555-0123"
            }
        },
        {
            "name": "Sarah Johnson",
            "position": "Designer",
            "skills": ["UI/UX", "Figma", "Photoshop"],
            "contact": {
                "email": "sarah@acme.com",
                "phone": "555-0124"
            }
        }
    ],
    "locations": {
        "headquarters": {
            "city": "San Francisco",
            "address": "123 Tech Street",
            "zip": "94105"
        },
        "branch_office": {
            "city": "New York",
            "address": "456 Park Avenue",
            "zip": "10022"
        }
    }
}
"""

company_info = []
def read_key(data, prefix):
    if isinstance(data, dict):
        for key, value in data.items():
            parent_key = f'{prefix}.{key}' if prefix else key
            if isinstance(value, dict):
                company_info.extend(read_key(value, parent_key).items())
            elif isinstance(value, list):
                for item in value:
                    company_info.extend(read_key(item, key).items())
            else:
                company_info[parent_key] = value
    # if isinstance(data, list):
    #     for items in list:
    #         parent_key = 
    
    return company_info


    # return company_info
        

if __name__ == "__main__":

    company_data = {
        "company": {
            "name": "Acme Corporation",
            "founded": 2010,
            "active": True
        },
    
        "employees": [
            {
                "name": "John Smith",
                "position": "Developer",
                "skills": ["Python", "JavaScript", "Docker"],
                "contact": {
                    "email": "john@acme.com",
                    "phone": "555-0123"
                }
            },
            {
                "name": "Sarah Johnson",
                "position": "Designer",
                "skills": ["UI/UX", "Figma", "Photoshop"],
                "contact": {
                    "email": "sarah@acme.com",
                    "phone": "555-0124"
                }
            }
        ]
    }
#     #     "locations": {
#     #         "headquarters": {
#     #             "city": "San Francisco",
#     #             "address": "123 Tech Street",
#     #             "zip": "94105"
#     #         },
#     #         "branch_office": {
#     #             "city": "New York",
#     #             "address": "456 Park Avenue",
#     #             "zip": "10022"
#     #         }
#     #     }
# # }
    print(read_key(company_data, prefix=""))
