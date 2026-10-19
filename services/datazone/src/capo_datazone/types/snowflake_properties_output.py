"""Generated from Smithy shape ``com.amazonaws.datazone#SnowflakePropertiesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.connection_status
    import capo_datazone.types.identity_mapping
    import capo_datazone.types.lineage_sync_output
    import capo_datazone.types.snowflake_role


class SnowflakePropertiesOutput(TypedDict, closed=True):
    snowflake_role: "capo_datazone.types.snowflake_role.SnowflakeRole"
    """<p>The Snowflake role used to access Snowflake resources.</p>"""
    identity_mapping: "capo_datazone.types.identity_mapping.IdentityMapping"
    """<p>The identity mapping configuration for the Snowflake connection.</p>"""
    lineage_sync: "capo_datazone.types.lineage_sync_output.LineageSyncOutput"
    """<p>The lineage sync configuration for the Snowflake connection.</p>"""
    status: "capo_datazone.types.connection_status.ConnectionStatus"
    """<p>The status of the Snowflake connection.</p>"""
    error_message: NotRequired["str"]
    """<p>An error message returned if the Snowflake connection failed to establish or validate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SnowflakePropertiesOutput) -> dict:
    out: dict = {}
    out["snowflakeRole"] = value["snowflake_role"]
    import capo_datazone.types.identity_mapping

    out["identityMapping"] = capo_datazone.types.identity_mapping.serialize_json(
        value["identity_mapping"]
    )
    import capo_datazone.types.lineage_sync_output

    out["lineageSync"] = capo_datazone.types.lineage_sync_output.serialize_json(
        value["lineage_sync"]
    )
    import capo_datazone.types.connection_status

    out["status"] = capo_datazone.types.connection_status.serialize_json(
        value["status"]
    )
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> SnowflakePropertiesOutput:
    out: SnowflakePropertiesOutput = {}  # type: ignore[typeddict-item]
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
        raise DeserializationError(
            "SnowflakePropertiesOutput.identity_mapping required"
        )
    if data.get("lineageSync") is not None:
        import capo_datazone.types.lineage_sync_output

        out["lineage_sync"] = capo_datazone.types.lineage_sync_output.deserialize_json(
            data["lineageSync"]
        )
    else:
        raise DeserializationError("SnowflakePropertiesOutput.lineage_sync required")
    if data.get("status") is not None:
        import capo_datazone.types.connection_status

        out["status"] = capo_datazone.types.connection_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_datazone.types.connection_status.ConnectionStatus", ""
        )
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    return out
