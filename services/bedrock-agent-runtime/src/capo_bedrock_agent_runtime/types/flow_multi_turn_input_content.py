"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowMultiTurnInputContent``."""

from typing import TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError, SerializationError
from capo_bedrock_agent_runtime.types._unknown import UnknownUnionMember


class FlowMultiTurnInputContentDocumentMember(TypedDict, closed=True):
    document: "object"


FlowMultiTurnInputContent: TypeAlias = (
    FlowMultiTurnInputContentDocumentMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: FlowMultiTurnInputContent) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"FlowMultiTurnInputContent: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "document" in value:
        return {"document": value["document"]}
    else:
        raise SerializationError("FlowMultiTurnInputContent: no variant present")


def deserialize_json(data: dict) -> FlowMultiTurnInputContent:
    if data.get("document") is not None:
        return {"document": data["document"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "FlowMultiTurnInputContent: no recognized variant key"
        )
