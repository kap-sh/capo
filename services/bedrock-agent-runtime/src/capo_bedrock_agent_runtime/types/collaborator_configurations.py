"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#CollaboratorConfigurations``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.collaborator_configuration

CollaboratorConfigurations: TypeAlias = list[
    "capo_bedrock_agent_runtime.types.collaborator_configuration.CollaboratorConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: CollaboratorConfigurations) -> list:
    import capo_bedrock_agent_runtime.types.collaborator_configuration

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent_runtime.types.collaborator_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CollaboratorConfigurations:
    import capo_bedrock_agent_runtime.types.collaborator_configuration

    out: CollaboratorConfigurations = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent_runtime.types.collaborator_configuration.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: CollaboratorConfigurations) -> list[Any]:
    import capo_bedrock_agent_runtime.types.collaborator_configuration

    return [
        capo_bedrock_agent_runtime.types.collaborator_configuration.redact_sensitive(
            item
        )
        for item in value
    ]
