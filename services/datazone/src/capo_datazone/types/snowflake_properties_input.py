"""Generated from Smithy shape ``com.amazonaws.datazone#SnowflakePropertiesInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.connectivity_properties
    import capo_datazone.types.identity_mapping
    import capo_datazone.types.lineage_sync_input
    import capo_datazone.types.snowflake_role


class SnowflakePropertiesInput(TypedDict, closed=True):
    connectivity_properties: NotRequired[
        "capo_datazone.types.connectivity_properties.ConnectivityProperties"
    ]
    """<p>The connectivity properties of the Snowflake connection.</p>"""
    snowflake_role: "capo_datazone.types.snowflake_role.SnowflakeRole"
    """<p>The Snowflake role used to access Snowflake resources.</p>"""
    identity_mapping: "capo_datazone.types.identity_mapping.IdentityMapping"
    """<p>The identity mapping configuration for the Snowflake connection.</p>"""
    lineage_sync: NotRequired["capo_datazone.types.lineage_sync_input.LineageSyncInput"]
    """<p>The lineage sync configuration for the Snowflake connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SnowflakePropertiesInput) -> dict:
    out: dict = {}
    if "connectivity_properties" in value:
        import capo_datazone.types.connectivity_properties

        out["connectivityProperties"] = (
            capo_datazone.types.connectivity_properties.serialize_json(
                value["connectivity_properties"]
            )
        )
    out["snowflakeRole"] = value["snowflake_role"]
    import capo_datazone.types.identity_mapping

    out["identityMapping"] = capo_datazone.types.identity_mapping.serialize_json(
        value["identity_mapping"]
    )
    if "lineage_sync" in value:
        import capo_datazone.types.lineage_sync_input

        out["lineageSync"] = capo_datazone.types.lineage_sync_input.serialize_json(
            value["lineage_sync"]
        )
    return out


def deserialize_json(data: dict) -> SnowflakePropertiesInput:
    out: SnowflakePropertiesInput = {}  # type: ignore[typeddict-item]
    if data.get("connectivityProperties") is not None:
        import capo_datazone.types.connectivity_properties

        out["connectivity_properties"] = (
            capo_datazone.types.connectivity_properties.deserialize_json(
                data["connectivityProperties"]
            )
        )
    if data.get("snowflakeRole") is not None:
        out["snowflake_role"] = data["snowflakeRole"]
    else:
        out["snowflake_role"] = ""
    if data.get("identityMapping") is not None:
        import capo_datazone.types.identity_mapping

        out["identity_mapping"] = capo_datazone.types.identity_mapping.deserialize_json(
            data["identityMapping"]
        )
    else:
        raise DeserializationError("SnowflakePropertiesInput.identity_mapping required")
    if data.get("lineageSync") is not None:
        import capo_datazone.types.lineage_sync_input

        out["lineage_sync"] = capo_datazone.types.lineage_sync_input.deserialize_json(
            data["lineageSync"]
        )
    return out


def redact_sensitive(value: SnowflakePropertiesInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "connectivity_properties" in value:
        import capo_datazone.types.connectivity_properties

        out["connectivity_properties"] = (
            capo_datazone.types.connectivity_properties.redact_sensitive(
                value["connectivity_properties"]
            )
        )
    return out
