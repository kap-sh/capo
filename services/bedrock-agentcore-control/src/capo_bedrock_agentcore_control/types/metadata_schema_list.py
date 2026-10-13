"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#MetadataSchemaList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.metadata_schema_entry

MetadataSchemaList: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.metadata_schema_entry.MetadataSchemaEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: MetadataSchemaList) -> list:
    import capo_bedrock_agentcore_control.types.metadata_schema_entry

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.metadata_schema_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> MetadataSchemaList:
    import capo_bedrock_agentcore_control.types.metadata_schema_entry

    out: MetadataSchemaList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.metadata_schema_entry.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: MetadataSchemaList) -> list[Any]:
    import capo_bedrock_agentcore_control.types.metadata_schema_entry

    return [
        capo_bedrock_agentcore_control.types.metadata_schema_entry.redact_sensitive(
            item
        )
        for item in value
    ]
