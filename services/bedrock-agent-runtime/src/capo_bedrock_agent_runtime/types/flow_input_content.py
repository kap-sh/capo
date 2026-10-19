"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowInputContent``."""

from typing import TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError, SerializationError
from capo_bedrock_agent_runtime.types._unknown import UnknownUnionMember


class _FlowInputContent_document(TypedDict, closed=True):
    document: "object"


FlowInputContent: TypeAlias = _FlowInputContent_document | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: FlowInputContent) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"FlowInputContent: cannot serialize unknown variant {value.name!r}"
        )
    elif "document" in value:
        return {"document": value["document"]}
    else:
        raise SerializationError("FlowInputContent: no variant present")


def deserialize_json(data: dict) -> FlowInputContent:
    if data.get("document") is not None:
        return {"document": data["document"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("FlowInputContent: no recognized variant key")
