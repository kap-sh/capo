"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#MetadataAttributeSchemaList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.metadata_attribute_schema

MetadataAttributeSchemaList: TypeAlias = list[
    "capo_bedrock_agent_runtime.types.metadata_attribute_schema.MetadataAttributeSchema"
]


# --- restJson1 ser/de ---
def serialize_json(value: MetadataAttributeSchemaList) -> list:
    import capo_bedrock_agent_runtime.types.metadata_attribute_schema

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agent_runtime.types.metadata_attribute_schema.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> MetadataAttributeSchemaList:
    import capo_bedrock_agent_runtime.types.metadata_attribute_schema

    out: MetadataAttributeSchemaList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agent_runtime.types.metadata_attribute_schema.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: MetadataAttributeSchemaList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
