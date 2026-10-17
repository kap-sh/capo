"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#CustomMetadataSchemaConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_agent_registry_control.types.custom_metadata_schema_definition
    import capo_agent_registry_control.types.record_type_schema_override_list


class CustomMetadataSchemaConfiguration(TypedDict, closed=True):
    default_schema: NotRequired[
        "capo_agent_registry_control.types.custom_metadata_schema_definition.CustomMetadataSchemaDefinition"
    ]
    """<p>A JSON Schema with the common attributes: fields that records of every record type can carry.</p>"""
    record_type_schema_overrides: NotRequired[
        "capo_agent_registry_control.types.record_type_schema_override_list.RecordTypeSchemaOverrideList"
    ]
    """<p>The fields for individual record types. Records of a record type can carry the common attributes defined in <code>defaultSchema</code> plus that record type's fields.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomMetadataSchemaConfiguration) -> dict:
    out: dict = {}
    if "default_schema" in value:
        out["defaultSchema"] = value["default_schema"]
    if "record_type_schema_overrides" in value:
        import capo_agent_registry_control.types.record_type_schema_override_list

        out["recordTypeSchemaOverrides"] = (
            capo_agent_registry_control.types.record_type_schema_override_list.serialize_json(
                value["record_type_schema_overrides"]
            )
        )
    return out


def deserialize_json(data: dict) -> CustomMetadataSchemaConfiguration:
    out: CustomMetadataSchemaConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("defaultSchema") is not None:
        out["default_schema"] = data["defaultSchema"]
    if data.get("recordTypeSchemaOverrides") is not None:
        import capo_agent_registry_control.types.record_type_schema_override_list

        out["record_type_schema_overrides"] = (
            capo_agent_registry_control.types.record_type_schema_override_list.deserialize_json(
                data["recordTypeSchemaOverrides"]
            )
        )
    return out
