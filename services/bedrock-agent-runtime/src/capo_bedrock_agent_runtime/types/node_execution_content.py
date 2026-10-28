"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#NodeExecutionContent``."""

from typing import TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError, SerializationError
from capo_bedrock_agent_runtime.types._unknown import UnknownUnionMember


class NodeExecutionContentDocumentMember(TypedDict, closed=True):
    document: "object"


NodeExecutionContent: TypeAlias = (
    NodeExecutionContentDocumentMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: NodeExecutionContent) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"NodeExecutionContent: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "document" in value:
        return {"document": value["document"]}
    else:
        raise SerializationError("NodeExecutionContent: no variant present")


def deserialize_json(data: dict) -> NodeExecutionContent:
    if data.get("document") is not None:
        return {"document": data["document"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("NodeExecutionContent: no recognized variant key")
