import json
from typing import Any

def parse_json(data: str) -> dict[str, Any]:
    try:
        data = data.removeprefix("```json\n")
        data = data.removesuffix("\n```")
        return json.loads(data)
    except Exception as e:
        return {"error": str(e), "data": data}
