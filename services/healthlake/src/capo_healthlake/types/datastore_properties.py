"""Generated from Smithy shape ``com.amazonaws.healthlake#DatastoreProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_healthlake.types.analytics_configuration
    import capo_healthlake.types.datastore_arn
    import capo_healthlake.types.datastore_backup_status
    import capo_healthlake.types.datastore_id
    import capo_healthlake.types.datastore_name
    import capo_healthlake.types.datastore_status
    import capo_healthlake.types.error_cause
    import capo_healthlake.types.fhir_version
    import capo_healthlake.types.health_lake_string
    import capo_healthlake.types.health_lake_timestamp
    import capo_healthlake.types.identity_provider_configuration
    import capo_healthlake.types.nlp_configuration
    import capo_healthlake.types.preload_data_config
    import capo_healthlake.types.profile_configuration
    import capo_healthlake.types.sse_configuration


class DatastoreProperties(TypedDict, closed=True):
    datastore_id: "capo_healthlake.types.datastore_id.DatastoreId"
    """<p>The data store identifier.</p>"""
    datastore_arn: "capo_healthlake.types.datastore_arn.DatastoreArn"
    """<p>The Amazon Resource Name (ARN) used in the creation of the data store.</p>"""
    datastore_name: NotRequired["capo_healthlake.types.datastore_name.DatastoreName"]
    """<p>The data store name.</p>"""
    datastore_status: "capo_healthlake.types.datastore_status.DatastoreStatus"
    """<p>The data store status.</p>"""
    created_at: NotRequired[
        "capo_healthlake.types.health_lake_timestamp.HealthLakeTimestamp"
    ]
    """<p>The time the data store was created. </p>"""
    datastore_type_version: "capo_healthlake.types.fhir_version.FHIRVersion"
    """<p>The FHIR release version supported by the data store. Current support is for version <code>R4</code>.</p>"""
    datastore_endpoint: "capo_healthlake.types.health_lake_string.HealthLakeString"
    """<p>The Amazon Web Services endpoint for the data store.</p>"""
    sse_configuration: NotRequired[
        "capo_healthlake.types.sse_configuration.SseConfiguration"
    ]
    """<p> The server-side encryption key configuration for a customer provided encryption key.</p>"""
    preload_data_config: NotRequired[
        "capo_healthlake.types.preload_data_config.PreloadDataConfig"
    ]
    """<p>The preloaded Synthea data configuration for the data store.</p>"""
    identity_provider_configuration: NotRequired[
        "capo_healthlake.types.identity_provider_configuration.IdentityProviderConfiguration"
    ]
    """<p>The identity provider selected during data store creation.</p>"""
    error_cause: NotRequired["capo_healthlake.types.error_cause.ErrorCause"]
    """<p>The error cause for the current data store operation.</p>"""
    nlp_configuration: NotRequired[
        "capo_healthlake.types.nlp_configuration.NlpConfiguration"
    ]
    """<p>The natural language processing (NLP) configuration for the data store.</p>"""
    analytics_configuration: NotRequired[
        "capo_healthlake.types.analytics_configuration.AnalyticsConfiguration"
    ]
    """<p>The analytics configuration for the data store.</p>"""
    profile_configuration: NotRequired[
        "capo_healthlake.types.profile_configuration.ProfileConfiguration"
    ]
    """<p>The profile configuration for the data store.</p>"""
    backup_status_info: NotRequired[
        "capo_healthlake.types.datastore_backup_status.DatastoreBackupStatus"
    ]
    """The backup status information for the data store."""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DatastoreProperties) -> dict:
    out: dict = {}
    out["DatastoreId"] = value["datastore_id"]
    out["DatastoreArn"] = value["datastore_arn"]
    if "datastore_name" in value:
        out["DatastoreName"] = value["datastore_name"]
    import capo_healthlake.types.datastore_status

    out["DatastoreStatus"] = (
        capo_healthlake.types.datastore_status.serialize_aws_json_1_0(
            value["datastore_status"]
        )
    )
    if "created_at" in value:
        import capo_healthlake.types.health_lake_timestamp

        out["CreatedAt"] = (
            capo_healthlake.types.health_lake_timestamp.serialize_aws_json_1_0(
                value["created_at"]
            )
        )
    import capo_healthlake.types.fhir_version

    out["DatastoreTypeVersion"] = (
        capo_healthlake.types.fhir_version.serialize_aws_json_1_0(
            value["datastore_type_version"]
        )
    )
    out["DatastoreEndpoint"] = value["datastore_endpoint"]
    if "sse_configuration" in value:
        import capo_healthlake.types.sse_configuration

        out["SseConfiguration"] = (
            capo_healthlake.types.sse_configuration.serialize_aws_json_1_0(
                value["sse_configuration"]
            )
        )
    if "preload_data_config" in value:
        import capo_healthlake.types.preload_data_config

        out["PreloadDataConfig"] = (
            capo_healthlake.types.preload_data_config.serialize_aws_json_1_0(
                value["preload_data_config"]
            )
        )
    if "identity_provider_configuration" in value:
        import capo_healthlake.types.identity_provider_configuration

        out["IdentityProviderConfiguration"] = (
            capo_healthlake.types.identity_provider_configuration.serialize_aws_json_1_0(
                value["identity_provider_configuration"]
            )
        )
    if "error_cause" in value:
        import capo_healthlake.types.error_cause

        out["ErrorCause"] = capo_healthlake.types.error_cause.serialize_aws_json_1_0(
            value["error_cause"]
        )
    if "nlp_configuration" in value:
        import capo_healthlake.types.nlp_configuration

        out["NlpConfiguration"] = (
            capo_healthlake.types.nlp_configuration.serialize_aws_json_1_0(
                value["nlp_configuration"]
            )
        )
    if "analytics_configuration" in value:
        import capo_healthlake.types.analytics_configuration

        out["AnalyticsConfiguration"] = (
            capo_healthlake.types.analytics_configuration.serialize_aws_json_1_0(
                value["analytics_configuration"]
            )
        )
    if "profile_configuration" in value:
        import capo_healthlake.types.profile_configuration

        out["ProfileConfiguration"] = (
            capo_healthlake.types.profile_configuration.serialize_aws_json_1_0(
                value["profile_configuration"]
            )
        )
    if "backup_status_info" in value:
        import capo_healthlake.types.datastore_backup_status

        out["BackupStatusInfo"] = (
            capo_healthlake.types.datastore_backup_status.serialize_aws_json_1_0(
                value["backup_status_info"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DatastoreProperties:
    out: DatastoreProperties = {}  # type: ignore[typeddict-item]
    if data.get("DatastoreId") is not None:
        out["datastore_id"] = data["DatastoreId"]
    else:
        out["datastore_id"] = ""
    if data.get("DatastoreArn") is not None:
        out["datastore_arn"] = data["DatastoreArn"]
    else:
        out["datastore_arn"] = ""
    if data.get("DatastoreName") is not None:
        out["datastore_name"] = data["DatastoreName"]
    if data.get("DatastoreStatus") is not None:
        import capo_healthlake.types.datastore_status

        out["datastore_status"] = (
            capo_healthlake.types.datastore_status.deserialize_aws_json_1_0(
                data["DatastoreStatus"]
            )
        )
    else:
        import typing

        out["datastore_status"] = typing.cast(
            "capo_healthlake.types.datastore_status.DatastoreStatus", ""
        )
    if data.get("CreatedAt") is not None:
        import capo_healthlake.types.health_lake_timestamp

        out["created_at"] = (
            capo_healthlake.types.health_lake_timestamp.deserialize_aws_json_1_0(
                data["CreatedAt"]
            )
        )
    if data.get("DatastoreTypeVersion") is not None:
        import capo_healthlake.types.fhir_version

        out["datastore_type_version"] = (
            capo_healthlake.types.fhir_version.deserialize_aws_json_1_0(
                data["DatastoreTypeVersion"]
            )
        )
    else:
        import typing

        out["datastore_type_version"] = typing.cast(
            "capo_healthlake.types.fhir_version.FHIRVersion", ""
        )
    if data.get("DatastoreEndpoint") is not None:
        out["datastore_endpoint"] = data["DatastoreEndpoint"]
    else:
        out["datastore_endpoint"] = ""
    if data.get("SseConfiguration") is not None:
        import capo_healthlake.types.sse_configuration

        out["sse_configuration"] = (
            capo_healthlake.types.sse_configuration.deserialize_aws_json_1_0(
                data["SseConfiguration"]
            )
        )
    if data.get("PreloadDataConfig") is not None:
        import capo_healthlake.types.preload_data_config

        out["preload_data_config"] = (
            capo_healthlake.types.preload_data_config.deserialize_aws_json_1_0(
                data["PreloadDataConfig"]
            )
        )
    if data.get("IdentityProviderConfiguration") is not None:
        import capo_healthlake.types.identity_provider_configuration

        out["identity_provider_configuration"] = (
            capo_healthlake.types.identity_provider_configuration.deserialize_aws_json_1_0(
                data["IdentityProviderConfiguration"]
            )
        )
    if data.get("ErrorCause") is not None:
        import capo_healthlake.types.error_cause

        out["error_cause"] = capo_healthlake.types.error_cause.deserialize_aws_json_1_0(
            data["ErrorCause"]
        )
    if data.get("NlpConfiguration") is not None:
        import capo_healthlake.types.nlp_configuration

        out["nlp_configuration"] = (
            capo_healthlake.types.nlp_configuration.deserialize_aws_json_1_0(
                data["NlpConfiguration"]
            )
        )
    if data.get("AnalyticsConfiguration") is not None:
        import capo_healthlake.types.analytics_configuration

        out["analytics_configuration"] = (
            capo_healthlake.types.analytics_configuration.deserialize_aws_json_1_0(
                data["AnalyticsConfiguration"]
            )
        )
    if data.get("ProfileConfiguration") is not None:
        import capo_healthlake.types.profile_configuration

        out["profile_configuration"] = (
            capo_healthlake.types.profile_configuration.deserialize_aws_json_1_0(
                data["ProfileConfiguration"]
            )
        )
    if data.get("BackupStatusInfo") is not None:
        import capo_healthlake.types.datastore_backup_status

        out["backup_status_info"] = (
            capo_healthlake.types.datastore_backup_status.deserialize_aws_json_1_0(
                data["BackupStatusInfo"]
            )
        )
    return out
