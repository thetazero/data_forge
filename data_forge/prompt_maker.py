from typing import NamedTuple

class column(NamedTuple):
    name: str
    type: str
    description: str

def make_json_extract_prompt(cols: list[column]) -> str:
    json_joiner = ',\n'
    field_joiner = '.\n'
    return f"""Write answer in the form of a json object like this: {{
{json_joiner.join([f'    "{col.name}": "{col.type}"' for col in cols])}
}}

Do not include any other information. 
Note the following descriptions for each field:
{field_joiner.join([f"{col.name}: {col.description}" for col in cols])}
Rember not to include any other information in your answer.
    """
