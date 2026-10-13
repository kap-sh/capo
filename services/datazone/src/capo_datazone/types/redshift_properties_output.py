"""Generated from Smithy shape ``com.amazonaws.datazone#RedshiftPropertiesOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.connection_status
    import capo_datazone.types.redshift_credentials
    import capo_datazone.types.redshift_lineage_sync_configuration_output
    import capo_datazone.types.redshift_storage_properties


class RedshiftPropertiesOutput(TypedDict, closed=True):
    storage: NotRequired[
        "capo_datazone.types.redshift_storage_properties.RedshiftStorageProperties"
    ]
    """<p>The storage in the Amazon Redshift properties.</p>"""
    credentials: NotRequired[
        "capo_datazone.types.redshift_credentials.RedshiftCredentials"
    ]
    """<p>The Amazon Redshift credentials.</p>"""
    is_provisioned_secret: NotRequired["bool"]
    """<p>Specifies whether Amaon Redshift properties has a provisioned secret.</p>"""
    jdbc_iam_url: NotRequired["str"]
    """<p>The jdbcIam URL of the Amazon Redshift properties.</p>"""
    jdbc_url: NotRequired["str"]
    """<p>The jdbcURL of the Amazon Redshift properties. </p>"""
    redshift_temp_dir: NotRequired["str"]
    """<p>The redshiftTempDir of the Amazon Redshift properties.</p>"""
    lineage_sync: NotRequired[
        "capo_datazone.types.redshift_lineage_sync_configuration_output.RedshiftLineageSyncConfigurationOutput"
    ]
    """<p>The lineage syn of the Amazon Redshift properties.</p>"""
    status: NotRequired["capo_datazone.types.connection_status.ConnectionStatus"]
    """<p>The status in the Amazon Redshift properties.</p>"""
    database_name: NotRequired["str"]
    """<p>The Amazon Redshift database name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RedshiftPropertiesOutput) -> dict:
    out: dict = {}
    if "storage" in value:
        import capo_datazone.types.redshift_storage_properties

        out["storage"] = capo_datazone.types.redshift_storage_properties.serialize_json(
            value["storage"]
        )
    if "credentials" in value:
        import capo_datazone.types.redshift_credentials

        out["credentials"] = capo_datazone.types.redshift_credentials.serialize_json(
            value["credentials"]
        )
    if "is_provisioned_secret" in value:
        out["isProvisionedSecret"] = value["is_provisioned_secret"]
    if "jdbc_iam_url" in value:
        out["jdbcIamUrl"] = value["jdbc_iam_url"]
    if "jdbc_url" in value:
        out["jdbcUrl"] = value["jdbc_url"]
    if "redshift_temp_dir" in value:
        out["redshiftTempDir"] = value["redshift_temp_dir"]
    if "lineage_sync" in value:
        import capo_datazone.types.redshift_lineage_sync_configuration_output

        out["lineageSync"] = (
            capo_datazone.types.redshift_lineage_sync_configuration_output.serialize_json(
                value["lineage_sync"]
            )
        )
    if "status" in value:
        import capo_datazone.types.connection_status

        out["status"] = capo_datazone.types.connection_status.serialize_json(
            value["status"]
        )
    if "database_name" in value:
        out["databaseName"] = value["database_name"]
    return out


def deserialize_json(data: dict) -> RedshiftPropertiesOutput:
    out: RedshiftPropertiesOutput = {}  # type: ignore[typeddict-item]
    if data.get("storage") is not None:
        import capo_datazone.types.redshift_storage_properties

        out["storage"] = (
            capo_datazone.types.redshift_storage_properties.deserialize_json(
                data["storage"]
            )
        )
    if data.get("credentials") is not None:
        import capo_datazone.types.redshift_credentials

        out["credentials"] = capo_datazone.types.redshift_credentials.deserialize_json(
            data["credentials"]
        )
    if data.get("isProvisionedSecret") is not None:
        out["is_provisioned_secret"] = data["isProvisionedSecret"]
    if data.get("jdbcIamUrl") is not None:
        out["jdbc_iam_url"] = data["jdbcIamUrl"]
    if data.get("jdbcUrl") is not None:
        out["jdbc_url"] = data["jdbcUrl"]
    if data.get("redshiftTempDir") is not None:
        out["redshift_temp_dir"] = data["redshiftTempDir"]
    if data.get("lineageSync") is not None:
        import capo_datazone.types.redshift_lineage_sync_configuration_output

        out["lineage_sync"] = (
            capo_datazone.types.redshift_lineage_sync_configuration_output.deserialize_json(
                data["lineageSync"]
            )
        )
    if data.get("status") is not None:
        import capo_datazone.types.connection_status

        out["status"] = capo_datazone.types.connection_status.deserialize_json(
            data["status"]
        )
    if data.get("databaseName") is not None:
        out["database_name"] = data["databaseName"]
    return out


def redact_sensitive(value: RedshiftPropertiesOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "credentials" in value:
        out["credentials"] = "*** Sensitive Data Redacted ***"
    return out
