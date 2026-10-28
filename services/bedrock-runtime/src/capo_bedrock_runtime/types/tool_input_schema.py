"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ToolInputSchema``."""

from typing import TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_runtime.errors import DeserializationError, SerializationError
from capo_bedrock_runtime.types._unknown import UnknownUnionMember


class ToolInputSchemaJsonMember(TypedDict, closed=True):
    json: "object"


ToolInputSchema: TypeAlias = ToolInputSchemaJsonMember | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: ToolInputSchema) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ToolInputSchema: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "json" in value:
        return {"json": value["json"]}
    else:
        raise SerializationError("ToolInputSchema: no variant present")


def deserialize_json(data: dict) -> ToolInputSchema:
    if data.get("json") is not None:
        return {"json": data["json"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ToolInputSchema: no recognized variant key")
