"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#RecordTypeSchemaOverride``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_agent_registry_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_agent_registry_control.types.custom_metadata_schema_definition
    import capo_agent_registry_control.types.record_type


class RecordTypeSchemaOverride(TypedDict, closed=True):
    record_type: "capo_agent_registry_control.types.record_type.RecordType"
    """<p>The record type that this schema override applies to.</p>"""
    schema: "capo_agent_registry_control.types.custom_metadata_schema_definition.CustomMetadataSchemaDefinition"
    """<p>The JSON Schema for the specified record type. Must follow the same structural rules as the default schema.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecordTypeSchemaOverride) -> dict:
    out: dict = {}
    import capo_agent_registry_control.types.record_type

    out["recordType"] = capo_agent_registry_control.types.record_type.serialize_json(
        value["record_type"]
    )
    out["schema"] = value["schema"]
    return out


def deserialize_json(data: dict) -> RecordTypeSchemaOverride:
    out: RecordTypeSchemaOverride = {}  # type: ignore[typeddict-item]
    if data.get("recordType") is not None:
        import capo_agent_registry_control.types.record_type

        out["record_type"] = (
            capo_agent_registry_control.types.record_type.deserialize_json(
                data["recordType"]
            )
        )
    else:
        raise DeserializationError("RecordTypeSchemaOverride.record_type required")
    if data.get("schema") is not None:
        out["schema"] = data["schema"]
    else:
        raise DeserializationError("RecordTypeSchemaOverride.schema required")
    return out
