"""Generated from Smithy shape ``com.amazonaws.datazone#SnowflakePropertiesPatch``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.connectivity_properties_patch
    import capo_datazone.types.lineage_sync_input
    import capo_datazone.types.snowflake_role


class SnowflakePropertiesPatch(TypedDict, closed=True):
    connectivity_properties_patch: NotRequired[
        "capo_datazone.types.connectivity_properties_patch.ConnectivityPropertiesPatch"
    ]
    """<p>The connectivity properties patch of the Snowflake connection.</p>"""
    snowflake_role: NotRequired["capo_datazone.types.snowflake_role.SnowflakeRole"]
    """<p>The Snowflake role used to access Snowflake resources.</p>"""
    lineage_sync: NotRequired["capo_datazone.types.lineage_sync_input.LineageSyncInput"]
    """<p>The lineage sync configuration for the Snowflake connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SnowflakePropertiesPatch) -> dict:
    out: dict = {}
    if "connectivity_properties_patch" in value:
        import capo_datazone.types.connectivity_properties_patch

        out["connectivityPropertiesPatch"] = (
            capo_datazone.types.connectivity_properties_patch.serialize_json(
                value["connectivity_properties_patch"]
            )
        )
    if "snowflake_role" in value:
        out["snowflakeRole"] = value["snowflake_role"]
    if "lineage_sync" in value:
        import capo_datazone.types.lineage_sync_input

        out["lineageSync"] = capo_datazone.types.lineage_sync_input.serialize_json(
            value["lineage_sync"]
        )
    return out


def deserialize_json(data: dict) -> SnowflakePropertiesPatch:
    out: SnowflakePropertiesPatch = {}  # type: ignore[typeddict-item]
    if data.get("connectivityPropertiesPatch") is not None:
        import capo_datazone.types.connectivity_properties_patch

        out["connectivity_properties_patch"] = (
            capo_datazone.types.connectivity_properties_patch.deserialize_json(
                data["connectivityPropertiesPatch"]
            )
        )
    if data.get("snowflakeRole") is not None:
        out["snowflake_role"] = data["snowflakeRole"]
    if data.get("lineageSync") is not None:
        import capo_datazone.types.lineage_sync_input

        out["lineage_sync"] = capo_datazone.types.lineage_sync_input.deserialize_json(
            data["lineageSync"]
        )
    return out


def redact_sensitive(value: SnowflakePropertiesPatch) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "connectivity_properties_patch" in value:
        import capo_datazone.types.connectivity_properties_patch

        out["connectivity_properties_patch"] = (
            capo_datazone.types.connectivity_properties_patch.redact_sensitive(
                value["connectivity_properties_patch"]
            )
        )
    return out
