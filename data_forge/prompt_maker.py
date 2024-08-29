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

if __name__ == "__main__":
    cols = [
        column("name", "string", "The name of the person."),
        column("age", "number", "The age of the person."),
        column("gender", "male | female", "The gender of the person."),
        column("alive", "true | false", "If the person is currently alive, according to the source."),
    ]

    print(make_json_extract_prompt(cols))
