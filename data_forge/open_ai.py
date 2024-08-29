from .cache import cache
from openai import OpenAI
client = OpenAI()


def extract(data: str, json_extract_prompt: str) -> str:
    caller = 'extract-v1'
    key = data + json_extract_prompt
    cached_value = cache.get(caller, key)
    if cached_value:
        return cached_value
    print('Cache miss')

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": f"Data: {data}"},
            {"role": "user", "content": json_extract_prompt},
        ]
    )

    res = completion.choices[0].message.content
    if res == None:
        raise Exception("No response from the model.")

    cache.set(caller, key, res)
    return res
