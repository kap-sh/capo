"""Generated from Smithy shape ``com.amazonaws.bedrockagent#MetadataConfigurations``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent.types.metadata_configuration

MetadataConfigurations: TypeAlias = list[
    "capo_bedrock_agent.types.metadata_configuration.MetadataConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: MetadataConfigurations) -> list:
    import capo_bedrock_agent.types.metadata_configuration

    out: list = []
    for item in value:
        out.append(capo_bedrock_agent.types.metadata_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> MetadataConfigurations:
    import capo_bedrock_agent.types.metadata_configuration

    out: MetadataConfigurations = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent.types.metadata_configuration.deserialize_json(item)
        )
    return out


def redact_sensitive(value: MetadataConfigurations) -> list[Any]:
    import capo_bedrock_agent.types.metadata_configuration

    return [
        capo_bedrock_agent.types.metadata_configuration.redact_sensitive(item)
        for item in value
    ]
