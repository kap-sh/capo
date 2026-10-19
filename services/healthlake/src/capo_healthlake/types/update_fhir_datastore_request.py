"""Generated from Smithy shape ``com.amazonaws.healthlake#UpdateFHIRDatastoreRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_healthlake.types.analytics_configuration
    import capo_healthlake.types.backup_configuration
    import capo_healthlake.types.datastore_id
    import capo_healthlake.types.datastore_name
    import capo_healthlake.types.identity_provider_configuration
    import capo_healthlake.types.nlp_configuration
    import capo_healthlake.types.profile_configuration


class UpdateFHIRDatastoreRequest(TypedDict, closed=True):
    datastore_id: "capo_healthlake.types.datastore_id.DatastoreId"
    """<p>The data store identifier.</p>"""
    datastore_name: NotRequired["capo_healthlake.types.datastore_name.DatastoreName"]
    """<p>The data store name.</p>"""
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
    identity_provider_configuration: NotRequired[
        "capo_healthlake.types.identity_provider_configuration.IdentityProviderConfiguration"
    ]
    """<p>The identity provider configuration for the data store.</p>"""
    backup_configuration: NotRequired[
        "capo_healthlake.types.backup_configuration.BackupConfiguration"
    ]
    """The backup configuration for the data store."""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateFHIRDatastoreRequest) -> dict:
    out: dict = {}
    out["DatastoreId"] = value["datastore_id"]
    if "datastore_name" in value:
        out["DatastoreName"] = value["datastore_name"]
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
    if "identity_provider_configuration" in value:
        import capo_healthlake.types.identity_provider_configuration

        out["IdentityProviderConfiguration"] = (
            capo_healthlake.types.identity_provider_configuration.serialize_aws_json_1_0(
                value["identity_provider_configuration"]
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


def deserialize_aws_json_1_0(data: dict) -> UpdateFHIRDatastoreRequest:
    out: UpdateFHIRDatastoreRequest = {}  # type: ignore[typeddict-item]
    if data.get("DatastoreId") is not None:
        out["datastore_id"] = data["DatastoreId"]
    else:
        out["datastore_id"] = ""
    if data.get("DatastoreName") is not None:
        out["datastore_name"] = data["DatastoreName"]
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
    if data.get("IdentityProviderConfiguration") is not None:
        import capo_healthlake.types.identity_provider_configuration

        out["identity_provider_configuration"] = (
            capo_healthlake.types.identity_provider_configuration.deserialize_aws_json_1_0(
                data["IdentityProviderConfiguration"]
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
