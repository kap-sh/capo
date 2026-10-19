"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#Domain``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_cloudwatchomni.types.arn
    import capo_cloudwatchomni.types.domain_id
    import capo_cloudwatchomni.types.domain_status
    import capo_cloudwatchomni.types.identity_provider_configuration
    import capo_cloudwatchomni.types.identity_provider_list
    import capo_cloudwatchomni.types.string_list


class Domain(TypedDict, closed=True):
    domain_id: "capo_cloudwatchomni.types.domain_id.DomainId"
    """The unique ID of the domain."""
    domain_arn: "capo_cloudwatchomni.types.arn.Arn"
    """The Amazon Resource Name (ARN) of the domain."""
    name: NotRequired["str"]
    """A name that identifies the domain."""
    identity_providers: (
        "capo_cloudwatchomni.types.identity_provider_list.IdentityProviderList"
    )
    """The identity providers configured for the domain."""
    identity_provider_configuration: NotRequired[
        "capo_cloudwatchomni.types.identity_provider_configuration.IdentityProviderConfiguration"
    ]
    """Identity provider configuration for the domain."""
    domain_endpoint_url: "str"
    """The HTTPS endpoint URL for accessing the domain."""
    custom_endpoint_urls: NotRequired[
        "capo_cloudwatchomni.types.string_list.StringList"
    ]
    """Additional endpoint URLs derived from the domain name."""
    identity_center_application_arn: NotRequired["capo_cloudwatchomni.types.arn.Arn"]
    """The ARN of the Identity Center application. Absent for IAM-only domains."""
    region: "str"
    """The Region where this domain was created."""
    created_at: "datetime.datetime"
    """The timestamp when the domain was created."""
    updated_at: "datetime.datetime"
    """The timestamp when the domain was last updated."""
    status: "capo_cloudwatchomni.types.domain_status.DomainStatus"
    """Current status of the domain."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Domain) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    out["domainArn"] = value["domain_arn"]
    if "name" in value:
        out["name"] = value["name"]
    import capo_cloudwatchomni.types.identity_provider_list

    out["identityProviders"] = (
        capo_cloudwatchomni.types.identity_provider_list.serialize_cbor(
            value["identity_providers"]
        )
    )
    if "identity_provider_configuration" in value:
        import capo_cloudwatchomni.types.identity_provider_configuration

        out["identityProviderConfiguration"] = (
            capo_cloudwatchomni.types.identity_provider_configuration.serialize_cbor(
                value["identity_provider_configuration"]
            )
        )
    out["domainEndpointUrl"] = value["domain_endpoint_url"]
    if "custom_endpoint_urls" in value:
        import capo_cloudwatchomni.types.string_list

        out["customEndpointUrls"] = (
            capo_cloudwatchomni.types.string_list.serialize_cbor(
                value["custom_endpoint_urls"]
            )
        )
    if "identity_center_application_arn" in value:
        out["identityCenterApplicationArn"] = value["identity_center_application_arn"]
    out["region"] = value["region"]
    import capo_cloudwatchomni.types._prelude.timestamp

    out["createdAt"] = capo_cloudwatchomni.types._prelude.timestamp.serialize_cbor(
        value["created_at"]
    )
    import capo_cloudwatchomni.types._prelude.timestamp

    out["updatedAt"] = capo_cloudwatchomni.types._prelude.timestamp.serialize_cbor(
        value["updated_at"]
    )
    import capo_cloudwatchomni.types.domain_status

    out["status"] = capo_cloudwatchomni.types.domain_status.serialize_cbor(
        value["status"]
    )
    return out


def deserialize_cbor(data: dict) -> Domain:
    out: Domain = {}  # type: ignore[typeddict-item]
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    else:
        out["domain_id"] = ""
    if data.get("domainArn") is not None:
        out["domain_arn"] = data["domainArn"]
    else:
        out["domain_arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("identityProviders") is not None:
        import capo_cloudwatchomni.types.identity_provider_list

        out["identity_providers"] = (
            capo_cloudwatchomni.types.identity_provider_list.deserialize_cbor(
                data["identityProviders"]
            )
        )
    else:
        out["identity_providers"] = []
    if data.get("identityProviderConfiguration") is not None:
        import capo_cloudwatchomni.types.identity_provider_configuration

        out["identity_provider_configuration"] = (
            capo_cloudwatchomni.types.identity_provider_configuration.deserialize_cbor(
                data["identityProviderConfiguration"]
            )
        )
    if data.get("domainEndpointUrl") is not None:
        out["domain_endpoint_url"] = data["domainEndpointUrl"]
    else:
        out["domain_endpoint_url"] = ""
    if data.get("customEndpointUrls") is not None:
        import capo_cloudwatchomni.types.string_list

        out["custom_endpoint_urls"] = (
            capo_cloudwatchomni.types.string_list.deserialize_cbor(
                data["customEndpointUrls"]
            )
        )
    if data.get("identityCenterApplicationArn") is not None:
        out["identity_center_application_arn"] = data["identityCenterApplicationArn"]
    if data.get("region") is not None:
        out["region"] = data["region"]
    else:
        out["region"] = ""
    if data.get("createdAt") is not None:
        import capo_cloudwatchomni.types._prelude.timestamp

        out["created_at"] = (
            capo_cloudwatchomni.types._prelude.timestamp.deserialize_cbor(
                data["createdAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import capo_cloudwatchomni.types._prelude.timestamp

        out["updated_at"] = (
            capo_cloudwatchomni.types._prelude.timestamp.deserialize_cbor(
                data["updatedAt"]
            )
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("status") is not None:
        import capo_cloudwatchomni.types.domain_status

        out["status"] = capo_cloudwatchomni.types.domain_status.deserialize_cbor(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_cloudwatchomni.types.domain_status.DomainStatus", ""
        )
    return out
