"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#Content``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.natural_language


class ContentRawTextMember(TypedDict, closed=True):
    rawText: "capo_bedrock_agentcore_control.types.natural_language.NaturalLanguage"


Content: TypeAlias = ContentRawTextMember | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: Content) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"Content: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "rawText" in value:
        return {"rawText": value["rawText"]}
    else:
        raise SerializationError("Content: no variant present")


def deserialize_json(data: dict) -> Content:
    if data.get("rawText") is not None:
        return {"rawText": data["rawText"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("Content: no recognized variant key")
