"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#RetrievedReferences``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.retrieved_reference

RetrievedReferences: TypeAlias = list[
    "capo_bedrock_agent_runtime.types.retrieved_reference.RetrievedReference"
]


# --- restJson1 ser/de ---
def serialize_json(value: RetrievedReferences) -> list:
    import capo_bedrock_agent_runtime.types.retrieved_reference

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent_runtime.types.retrieved_reference.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RetrievedReferences:
    import capo_bedrock_agent_runtime.types.retrieved_reference

    out: RetrievedReferences = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent_runtime.types.retrieved_reference.deserialize_json(item)
        )
    return out


def redact_sensitive(value: RetrievedReferences) -> list[Any]:
    import capo_bedrock_agent_runtime.types.retrieved_reference

    return [
        capo_bedrock_agent_runtime.types.retrieved_reference.redact_sensitive(item)
        for item in value
    ]
