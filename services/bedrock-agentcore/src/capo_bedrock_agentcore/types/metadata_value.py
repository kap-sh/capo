"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#MetadataValue``."""

from typing import TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError
from capo_bedrock_agentcore.types._unknown import UnknownUnionMember


class _MetadataValue_stringValue(TypedDict, closed=True):
    stringValue: "str"


MetadataValue: TypeAlias = _MetadataValue_stringValue | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: MetadataValue) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"MetadataValue: cannot serialize unknown variant {value.name!r}"
        )
    elif "stringValue" in value:
        return {"stringValue": value["stringValue"]}
    else:
        raise SerializationError("MetadataValue: no variant present")


def deserialize_json(data: dict) -> MetadataValue:
    if data.get("stringValue") is not None:
        return {"stringValue": data["stringValue"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("MetadataValue: no recognized variant key")
