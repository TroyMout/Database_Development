# import pandas as pd
import requests
import json

# 1) SETUP Connection string

# Make function
def get_cat_facts(_amount):
    # Check documentation
    conn_str = f'https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount={_amount}'

    # 2) Call the API
    response = requests.get(conn_str)

    # 3) Parse the results
    response = json.loads(response.content)
    l_cat_fact = []
    for _fact in response:
        l_cat_fact.append(_fact['text'])

    return l_cat_fact

str_cat_facts = get_cat_facts(3)

print(str_cat_facts)
