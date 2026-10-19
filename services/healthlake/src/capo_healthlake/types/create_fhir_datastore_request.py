"""Generated from Smithy shape ``com.amazonaws.healthlake#CreateFHIRDatastoreRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_healthlake.types.analytics_configuration
    import capo_healthlake.types.backup_configuration
    import capo_healthlake.types.client_token_string
    import capo_healthlake.types.datastore_name
    import capo_healthlake.types.fhir_version
    import capo_healthlake.types.identity_provider_configuration
    import capo_healthlake.types.nlp_configuration
    import capo_healthlake.types.preload_data_config
    import capo_healthlake.types.profile_configuration
    import capo_healthlake.types.sse_configuration
    import capo_healthlake.types.tag_list


class CreateFHIRDatastoreRequest(TypedDict, closed=True):
    datastore_name: NotRequired["capo_healthlake.types.datastore_name.DatastoreName"]
    """<p>The data store name (user-generated).</p>"""
    datastore_type_version: "capo_healthlake.types.fhir_version.FHIRVersion"
    """<p>The FHIR release version supported by the data store. Current support is for version <code>R4</code>.</p>"""
    sse_configuration: NotRequired[
        "capo_healthlake.types.sse_configuration.SseConfiguration"
    ]
    """<p>The server-side encryption key configuration for a customer-provided encryption key specified for creating a data store. </p>"""
    preload_data_config: NotRequired[
        "capo_healthlake.types.preload_data_config.PreloadDataConfig"
    ]
    """<p>An optional parameter to preload (import) open source Synthea FHIR data upon creation of the data store.</p>"""
    client_token: NotRequired[
        "capo_healthlake.types.client_token_string.ClientTokenString"
    ]
    """<p>An optional user-provided token to ensure API idempotency.</p>"""
    tags: NotRequired["capo_healthlake.types.tag_list.TagList"]
    """<p>The resource tags applied to a data store when it is created.</p>"""
    identity_provider_configuration: NotRequired[
        "capo_healthlake.types.identity_provider_configuration.IdentityProviderConfiguration"
    ]
    """<p>The identity provider configuration to use for the data store.</p>"""
    analytics_configuration: NotRequired[
        "capo_healthlake.types.analytics_configuration.AnalyticsConfiguration"
    ]
    """<p>The analytics configuration for the data store.</p>"""
    nlp_configuration: NotRequired[
        "capo_healthlake.types.nlp_configuration.NlpConfiguration"
    ]
    """<p>The natural language processing (NLP) configuration for the data store.</p>"""
    profile_configuration: NotRequired[
        "capo_healthlake.types.profile_configuration.ProfileConfiguration"
    ]
    """<p>The profile configuration for the data store.</p>"""
    backup_configuration: NotRequired[
        "capo_healthlake.types.backup_configuration.BackupConfiguration"
    ]
    """The backup configuration for the data store."""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateFHIRDatastoreRequest) -> dict:
    out: dict = {}
    if "datastore_name" in value:
        out["DatastoreName"] = value["datastore_name"]
    import capo_healthlake.types.fhir_version

    out["DatastoreTypeVersion"] = (
        capo_healthlake.types.fhir_version.serialize_aws_json_1_0(
            value["datastore_type_version"]
        )
    )
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
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "tags" in value:
        import capo_healthlake.types.tag_list

        out["Tags"] = capo_healthlake.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    if "identity_provider_configuration" in value:
        import capo_healthlake.types.identity_provider_configuration

        out["IdentityProviderConfiguration"] = (
            capo_healthlake.types.identity_provider_configuration.serialize_aws_json_1_0(
                value["identity_provider_configuration"]
            )
        )
    if "analytics_configuration" in value:
        import capo_healthlake.types.analytics_configuration

        out["AnalyticsConfiguration"] = (
            capo_healthlake.types.analytics_configuration.serialize_aws_json_1_0(
                value["analytics_configuration"]
            )
        )
    if "nlp_configuration" in value:
        import capo_healthlake.types.nlp_configuration

        out["NlpConfiguration"] = (
            capo_healthlake.types.nlp_configuration.serialize_aws_json_1_0(
                value["nlp_configuration"]
            )
        )
    if "profile_configuration" in value:
        import capo_healthlake.types.profile_configuration

        out["ProfileConfiguration"] = (
            capo_healthlake.types.profile_configuration.serialize_aws_json_1_0(
                value["profile_configuration"]
            )
        )
    if "backup_configuration" in value:
        import capo_healthlake.types.backup_configuration

        out["BackupConfiguration"] = (
            capo_healthlake.types.backup_configuration.serialize_aws_json_1_0(
                value["backup_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateFHIRDatastoreRequest:
    out: CreateFHIRDatastoreRequest = {}  # type: ignore[typeddict-item]
    if data.get("DatastoreName") is not None:
        out["datastore_name"] = data["DatastoreName"]
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
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("Tags") is not None:
        import capo_healthlake.types.tag_list

        out["tags"] = capo_healthlake.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    if data.get("IdentityProviderConfiguration") is not None:
        import capo_healthlake.types.identity_provider_configuration

        out["identity_provider_configuration"] = (
            capo_healthlake.types.identity_provider_configuration.deserialize_aws_json_1_0(
                data["IdentityProviderConfiguration"]
            )
        )
    if data.get("AnalyticsConfiguration") is not None:
        import capo_healthlake.types.analytics_configuration

        out["analytics_configuration"] = (
            capo_healthlake.types.analytics_configuration.deserialize_aws_json_1_0(
                data["AnalyticsConfiguration"]
            )
        )
    if data.get("NlpConfiguration") is not None:
        import capo_healthlake.types.nlp_configuration

        out["nlp_configuration"] = (
            capo_healthlake.types.nlp_configuration.deserialize_aws_json_1_0(
                data["NlpConfiguration"]
            )
        )
    if data.get("ProfileConfiguration") is not None:
        import capo_healthlake.types.profile_configuration

        out["profile_configuration"] = (
            capo_healthlake.types.profile_configuration.deserialize_aws_json_1_0(
                data["ProfileConfiguration"]
            )
        )
    if data.get("BackupConfiguration") is not None:
        import capo_healthlake.types.backup_configuration

        out["backup_configuration"] = (
            capo_healthlake.types.backup_configuration.deserialize_aws_json_1_0(
                data["BackupConfiguration"]
            )
        )
    return out
