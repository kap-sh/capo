"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#MetadataSchemaEntry``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.extraction_config
    import capo_bedrock_agentcore_control.types.extraction_type
    import capo_bedrock_agentcore_control.types.metadata_key
    import capo_bedrock_agentcore_control.types.metadata_value_type


class MetadataSchemaEntry(TypedDict, closed=True):
    key: "capo_bedrock_agentcore_control.types.metadata_key.MetadataKey"
    """<p>The metadata field name. Must match an indexed key to be queryable via metadata filters.</p>"""
    type: NotRequired[
        "capo_bedrock_agentcore_control.types.metadata_value_type.MetadataValueType"
    ]
    """<p>The MetadataValueType.</p>"""
    extraction_type: NotRequired[
        "capo_bedrock_agentcore_control.types.extraction_type.ExtractionType"
    ]
    """<p>Specifies whether the metadata value is extracted by the LLM or passed through deterministically from the event.</p>"""
    extraction_config: NotRequired[
        "capo_bedrock_agentcore_control.types.extraction_config.ExtractionConfig"
    ]
    """<p>Configuration for extracting this metadata value from conversational content. Applicable only if extractionType is LLM inferred.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetadataSchemaEntry) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    if "type" in value:
        import capo_bedrock_agentcore_control.types.metadata_value_type

        out["type"] = (
            capo_bedrock_agentcore_control.types.metadata_value_type.serialize_json(
                value["type"]
            )
        )
    if "extraction_type" in value:
        import capo_bedrock_agentcore_control.types.extraction_type

        out["extractionType"] = (
            capo_bedrock_agentcore_control.types.extraction_type.serialize_json(
                value["extraction_type"]
            )
        )
    if "extraction_config" in value:
        import capo_bedrock_agentcore_control.types.extraction_config

        out["extractionConfig"] = (
            capo_bedrock_agentcore_control.types.extraction_config.serialize_json(
                value["extraction_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> MetadataSchemaEntry:
    out: MetadataSchemaEntry = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        raise DeserializationError("MetadataSchemaEntry.key required")
    if data.get("type") is not None:
        import capo_bedrock_agentcore_control.types.metadata_value_type

        out["type"] = (
            capo_bedrock_agentcore_control.types.metadata_value_type.deserialize_json(
                data["type"]
            )
        )
    if data.get("extractionType") is not None:
        import capo_bedrock_agentcore_control.types.extraction_type

        out["extraction_type"] = (
            capo_bedrock_agentcore_control.types.extraction_type.deserialize_json(
                data["extractionType"]
            )
        )
    if data.get("extractionConfig") is not None:
        import capo_bedrock_agentcore_control.types.extraction_config

        out["extraction_config"] = (
            capo_bedrock_agentcore_control.types.extraction_config.deserialize_json(
                data["extractionConfig"]
            )
        )
    return out


def redact_sensitive(value: MetadataSchemaEntry) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "extraction_config" in value:
        import capo_bedrock_agentcore_control.types.extraction_config

        out["extraction_config"] = (
            capo_bedrock_agentcore_control.types.extraction_config.redact_sensitive(
                value["extraction_config"]
            )
        )
    return out
