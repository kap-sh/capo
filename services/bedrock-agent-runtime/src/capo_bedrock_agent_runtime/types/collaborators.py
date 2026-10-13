"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#Collaborators``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.collaborator

Collaborators: TypeAlias = list[
    "capo_bedrock_agent_runtime.types.collaborator.Collaborator"
]


# --- restJson1 ser/de ---
def serialize_json(value: Collaborators) -> list:
    import capo_bedrock_agent_runtime.types.collaborator

    out: list = []
    for item in value:
        out.append(capo_bedrock_agent_runtime.types.collaborator.serialize_json(item))
    return out


def deserialize_json(data: list) -> Collaborators:
    import capo_bedrock_agent_runtime.types.collaborator

    out: Collaborators = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock_agent_runtime.types.collaborator.deserialize_json(item))
    return out


def redact_sensitive(value: Collaborators) -> list[Any]:
    import capo_bedrock_agent_runtime.types.collaborator

    return [
        capo_bedrock_agent_runtime.types.collaborator.redact_sensitive(item)
        for item in value
    ]
