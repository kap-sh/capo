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
    """<p>The default JSON Schema that applies to record types without a specific override. Supported property types are <code>string</code>, <code>string</code> with an <code>enum</code> constraint, <code>string</code> with a <code>uri</code> format, and <code>boolean</code>.</p>"""
    record_type_schema_overrides: NotRequired[
        "capo_agent_registry_control.types.record_type_schema_override_list.RecordTypeSchemaOverrideList"
    ]
    """<p>A list of per-record-type schema overrides. When a record's type matches an override, that override's schema is used instead of the default schema for validation. If you don't specify an override for a record type, the default schema applies. If no default schema exists, custom metadata on records of that type is rejected.</p>"""


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
