"""
input = { 'Name': 'vaibhav',
          'Age': '30',
          'Relation': [{
              'Name': 'saumya',
              'Age': '30',
              'Relation': 'wife'
          },
          {
              'Name': 'Avyaan',
              'Age': '1',
              'Relation': 'Son'
          }
          ]
         }
"""
def relation(dict):
    for relative in input['Relations']:
        if relative['Relation'] == 'Son':
            return relative['Name']
            

input = { 'Name': 'vaibhav',
          'Age': '30',
          'Relations': [{
              'Name': 'saumya',
              'Age': '30',
              'Relation': 'wife'
          },
          {
              'Name': 'Avyaan',
              'Age': '1',
              'Relation': 'Son'
          }
          ]
         }
print(relation(input))