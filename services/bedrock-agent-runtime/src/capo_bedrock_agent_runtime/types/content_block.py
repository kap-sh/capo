"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ContentBlock``."""

from typing import TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError, SerializationError
from capo_bedrock_agent_runtime.types._unknown import UnknownUnionMember


class ContentBlockTextMember(TypedDict, closed=True):
    text: "str"


ContentBlock: TypeAlias = ContentBlockTextMember | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: ContentBlock) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ContentBlock: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "text" in value:
        return {"text": value["text"]}
    else:
        raise SerializationError("ContentBlock: no variant present")


def deserialize_json(data: dict) -> ContentBlock:
    if data.get("text") is not None:
        return {"text": data["text"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ContentBlock: no recognized variant key")
