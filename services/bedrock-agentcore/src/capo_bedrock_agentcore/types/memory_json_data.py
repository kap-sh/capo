"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#MemoryJsonData``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.memory_json_data_content


class MemoryJsonData(TypedDict, closed=True):
    content: (
        "capo_bedrock_agentcore.types.memory_json_data_content.MemoryJsonDataContent"
    )
    """<p>The JSON content of the payload. Accepts any JSON value, including objects, arrays, strings, numbers, booleans, and null. The maximum size is 100 KB.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MemoryJsonData) -> dict:
    out: dict = {}
    out["content"] = value["content"]
    return out


def deserialize_json(data: dict) -> MemoryJsonData:
    out: MemoryJsonData = {}  # type: ignore[typeddict-item]
    if data.get("content") is not None:
        out["content"] = data["content"]
    else:
        out["content"] = None
    return out
