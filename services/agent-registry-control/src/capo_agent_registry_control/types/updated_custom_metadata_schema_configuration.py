"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#UpdatedCustomMetadataSchemaConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_agent_registry_control.types.custom_metadata_schema_configuration


class UpdatedCustomMetadataSchemaConfiguration(TypedDict, closed=True):
    optional_value: NotRequired[
        "capo_agent_registry_control.types.custom_metadata_schema_configuration.CustomMetadataSchemaConfiguration"
    ]
    """<p>The value to set for this field. Omit the wrapper to leave the field unchanged.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatedCustomMetadataSchemaConfiguration) -> dict:
    out: dict = {}
    if "optional_value" in value:
        import capo_agent_registry_control.types.custom_metadata_schema_configuration

        out["optionalValue"] = (
            capo_agent_registry_control.types.custom_metadata_schema_configuration.serialize_json(
                value["optional_value"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatedCustomMetadataSchemaConfiguration:
    out: UpdatedCustomMetadataSchemaConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("optionalValue") is not None:
        import capo_agent_registry_control.types.custom_metadata_schema_configuration

        out["optional_value"] = (
            capo_agent_registry_control.types.custom_metadata_schema_configuration.deserialize_json(
                data["optionalValue"]
            )
        )
    return out


def redact_sensitive(value: UpdatedCustomMetadataSchemaConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "optional_value" in value:
        out["optional_value"] = "*** Sensitive Data Redacted ***"
    return out
