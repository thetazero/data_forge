from openai import OpenAI
client = OpenAI()


def extract(data: str, json_extract_prompt: str) -> str:
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
    return res


if __name__ == "__main__":
    data = """Your organization is currently in ????. Your limits will automatically be increased once you move to the next usage tier based on the criteria outlined below. Visit our usage tiers documentation to learn more about the limits associated with each tier.
Current tier
Once the following criteria are met, you'll automatically move to the next tier:
At least $5 spent on the API since account creation.
View payment history
Buy credits
Next tier
Usage tier 1"""
    json_extract_prompt = "Rewrite your answer in the form of a json object like this: {\"tier\": \"tier\", \"confidence\": low|medium|high}, do not include any other information."

    print(extract(data, json_extract_prompt))
