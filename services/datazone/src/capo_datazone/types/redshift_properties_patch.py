"""Generated from Smithy shape ``com.amazonaws.datazone#RedshiftPropertiesPatch``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.redshift_credentials
    import capo_datazone.types.redshift_lineage_sync_configuration_input
    import capo_datazone.types.redshift_storage_properties


class RedshiftPropertiesPatch(TypedDict, closed=True):
    storage: NotRequired[
        "capo_datazone.types.redshift_storage_properties.RedshiftStorageProperties"
    ]
    """<p>The storage in the Amazon Redshift properties patch.</p>"""
    database_name: NotRequired["str"]
    """<p>The name in the Amazon Redshift properties patch.</p>"""
    host: NotRequired["str"]
    """<p>The host in the Amazon Redshift properties patch.</p>"""
    port: NotRequired["int"]
    """<p>The port in the Amazon Redshift properties patch.</p>"""
    credentials: NotRequired[
        "capo_datazone.types.redshift_credentials.RedshiftCredentials"
    ]
    """<p>The credentials in the Amazon Redshift properties patch.</p>"""
    lineage_sync: NotRequired[
        "capo_datazone.types.redshift_lineage_sync_configuration_input.RedshiftLineageSyncConfigurationInput"
    ]
    """<p>The lineage sync in the Amazon Redshift properties patch.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RedshiftPropertiesPatch) -> dict:
    out: dict = {}
    if "storage" in value:
        import capo_datazone.types.redshift_storage_properties

        out["storage"] = capo_datazone.types.redshift_storage_properties.serialize_json(
            value["storage"]
        )
    if "database_name" in value:
        out["databaseName"] = value["database_name"]
    if "host" in value:
        out["host"] = value["host"]
    if "port" in value:
        out["port"] = value["port"]
    if "credentials" in value:
        import capo_datazone.types.redshift_credentials

        out["credentials"] = capo_datazone.types.redshift_credentials.serialize_json(
            value["credentials"]
        )
    if "lineage_sync" in value:
        import capo_datazone.types.redshift_lineage_sync_configuration_input

        out["lineageSync"] = (
            capo_datazone.types.redshift_lineage_sync_configuration_input.serialize_json(
                value["lineage_sync"]
            )
        )
    return out


def deserialize_json(data: dict) -> RedshiftPropertiesPatch:
    out: RedshiftPropertiesPatch = {}  # type: ignore[typeddict-item]
    if data.get("storage") is not None:
        import capo_datazone.types.redshift_storage_properties

        out["storage"] = (
            capo_datazone.types.redshift_storage_properties.deserialize_json(
                data["storage"]
            )
        )
    if data.get("databaseName") is not None:
        out["database_name"] = data["databaseName"]
    if data.get("host") is not None:
        out["host"] = data["host"]
    if data.get("port") is not None:
        out["port"] = data["port"]
    if data.get("credentials") is not None:
        import capo_datazone.types.redshift_credentials

        out["credentials"] = capo_datazone.types.redshift_credentials.deserialize_json(
            data["credentials"]
        )
    if data.get("lineageSync") is not None:
        import capo_datazone.types.redshift_lineage_sync_configuration_input

        out["lineage_sync"] = (
            capo_datazone.types.redshift_lineage_sync_configuration_input.deserialize_json(
                data["lineageSync"]
            )
        )
    return out


def redact_sensitive(value: RedshiftPropertiesPatch) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "credentials" in value:
        out["credentials"] = "*** Sensitive Data Redacted ***"
    return out
