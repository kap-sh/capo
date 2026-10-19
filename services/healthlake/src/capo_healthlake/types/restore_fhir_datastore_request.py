"""Generated from Smithy shape ``com.amazonaws.healthlake#RestoreFHIRDatastoreRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_healthlake.types.analytics_configuration
    import capo_healthlake.types.client_token_string
    import capo_healthlake.types.datastore_id
    import capo_healthlake.types.datastore_name
    import capo_healthlake.types.identity_provider_configuration
    import capo_healthlake.types.nlp_configuration
    import capo_healthlake.types.profile_configuration
    import capo_healthlake.types.restore_configuration
    import capo_healthlake.types.sse_configuration
    import capo_healthlake.types.tag_list


class RestoreFHIRDatastoreRequest(TypedDict, closed=True):
    source_datastore_id: "capo_healthlake.types.datastore_id.DatastoreId"
    """The identifier of the source data store to restore from."""
    restore_configuration: (
        "capo_healthlake.types.restore_configuration.RestoreConfiguration"
    )
    """The restore configuration specifying the type and parameters for the restore."""
    datastore_name: NotRequired["capo_healthlake.types.datastore_name.DatastoreName"]
    """The name for the restored data store."""
    sse_configuration: NotRequired[
        "capo_healthlake.types.sse_configuration.SseConfiguration"
    ]
    """The server-side encryption key configuration for the restored data store."""
    client_token: NotRequired[
        "capo_healthlake.types.client_token_string.ClientTokenString"
    ]
    """An optional user-provided token to ensure API idempotency of the restore."""
    tags: NotRequired["capo_healthlake.types.tag_list.TagList"]
    """The resource tags applied to the restored data store."""
    identity_provider_configuration: NotRequired[
        "capo_healthlake.types.identity_provider_configuration.IdentityProviderConfiguration"
    ]
    """The identity provider configuration for the restored data store."""
    analytics_configuration: NotRequired[
        "capo_healthlake.types.analytics_configuration.AnalyticsConfiguration"
    ]
    """The analytics configuration for the restored data store."""
    nlp_configuration: NotRequired[
        "capo_healthlake.types.nlp_configuration.NlpConfiguration"
    ]
    """The NLP configuration for the restored data store."""
    profile_configuration: NotRequired[
        "capo_healthlake.types.profile_configuration.ProfileConfiguration"
    ]
    """The profile configuration for the restored data store."""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RestoreFHIRDatastoreRequest) -> dict:
    out: dict = {}
    out["SourceDatastoreId"] = value["source_datastore_id"]
    import capo_healthlake.types.restore_configuration

    out["RestoreConfiguration"] = (
        capo_healthlake.types.restore_configuration.serialize_aws_json_1_0(
            value["restore_configuration"]
        )
    )
    if "datastore_name" in value:
        out["DatastoreName"] = value["datastore_name"]
    if "sse_configuration" in value:
        import capo_healthlake.types.sse_configuration

        out["SseConfiguration"] = (
            capo_healthlake.types.sse_configuration.serialize_aws_json_1_0(
                value["sse_configuration"]
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
    return out


def deserialize_aws_json_1_0(data: dict) -> RestoreFHIRDatastoreRequest:
    out: RestoreFHIRDatastoreRequest = {}  # type: ignore[typeddict-item]
    if data.get("SourceDatastoreId") is not None:
        out["source_datastore_id"] = data["SourceDatastoreId"]
    else:
        out["source_datastore_id"] = ""
    if data.get("RestoreConfiguration") is not None:
        import capo_healthlake.types.restore_configuration

        out["restore_configuration"] = (
            capo_healthlake.types.restore_configuration.deserialize_aws_json_1_0(
                data["RestoreConfiguration"]
            )
        )
    else:
        import capo_healthlake.types._unknown

        out["restore_configuration"] = (
            capo_healthlake.types._unknown.UnknownUnionMember("")
        )
    if data.get("DatastoreName") is not None:
        out["datastore_name"] = data["DatastoreName"]
    if data.get("SseConfiguration") is not None:
        import capo_healthlake.types.sse_configuration

        out["sse_configuration"] = (
            capo_healthlake.types.sse_configuration.deserialize_aws_json_1_0(
                data["SseConfiguration"]
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
    return out
