"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#FlowTraceNodeOutputContent``."""

from typing import TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError, SerializationError
from capo_bedrock_agent_runtime.types._unknown import UnknownUnionMember


class FlowTraceNodeOutputContentDocumentMember(TypedDict, closed=True):
    document: "object"


FlowTraceNodeOutputContent: TypeAlias = (
    FlowTraceNodeOutputContentDocumentMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: FlowTraceNodeOutputContent) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"FlowTraceNodeOutputContent: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "document" in value:
        return {"document": value["document"]}
    else:
        raise SerializationError("FlowTraceNodeOutputContent: no variant present")


def deserialize_json(data: dict) -> FlowTraceNodeOutputContent:
    if data.get("document") is not None:
        return {"document": data["document"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "FlowTraceNodeOutputContent: no recognized variant key"
        )
