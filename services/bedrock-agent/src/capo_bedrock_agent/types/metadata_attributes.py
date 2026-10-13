"""Generated from Smithy shape ``com.amazonaws.bedrockagent#MetadataAttributes``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent.types.metadata_attribute

MetadataAttributes: TypeAlias = list[
    "capo_bedrock_agent.types.metadata_attribute.MetadataAttribute"
]


# --- restJson1 ser/de ---
def serialize_json(value: MetadataAttributes) -> list:
    import capo_bedrock_agent.types.metadata_attribute

    out: list = []
    for item in value:
        out.append(capo_bedrock_agent.types.metadata_attribute.serialize_json(item))
    return out


def deserialize_json(data: list) -> MetadataAttributes:
    import capo_bedrock_agent.types.metadata_attribute

    out: MetadataAttributes = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock_agent.types.metadata_attribute.deserialize_json(item))
    return out


def redact_sensitive(value: MetadataAttributes) -> list[Any]:
    import capo_bedrock_agent.types.metadata_attribute

    return [
        capo_bedrock_agent.types.metadata_attribute.redact_sensitive(item)
        for item in value
    ]
