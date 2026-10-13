"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ExternalSources``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.external_source

ExternalSources: TypeAlias = list[
    "capo_bedrock_agent_runtime.types.external_source.ExternalSource"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExternalSources) -> list:
    import capo_bedrock_agent_runtime.types.external_source

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent_runtime.types.external_source.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ExternalSources:
    import capo_bedrock_agent_runtime.types.external_source

    out: ExternalSources = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent_runtime.types.external_source.deserialize_json(item)
        )
    return out


def redact_sensitive(value: ExternalSources) -> list[Any]:
    import capo_bedrock_agent_runtime.types.external_source

    return [
        capo_bedrock_agent_runtime.types.external_source.redact_sensitive(item)
        for item in value
    ]
