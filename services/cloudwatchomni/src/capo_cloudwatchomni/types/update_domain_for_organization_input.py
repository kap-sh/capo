"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#UpdateDomainForOrganizationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.domain_id
    import capo_cloudwatchomni.types.identity_provider_configuration
    import capo_cloudwatchomni.types.identity_provider_list


class UpdateDomainForOrganizationInput(TypedDict, closed=True):
    domain_id: "capo_cloudwatchomni.types.domain_id.DomainId"
    """The ID of the organization domain to update."""
    name: NotRequired["str"]
    """A new name for the organization domain. Omit to leave unchanged. Must be 3-63 characters: lowercase letters, numbers, and hyphens. It must begin and end with a letter or number and cannot contain consecutive hyphens."""
    identity_providers: NotRequired[
        "capo_cloudwatchomni.types.identity_provider_list.IdentityProviderList"
    ]
    """The identity providers to configure for the domain. Omit to leave unchanged."""
    identity_provider_configuration: NotRequired[
        "capo_cloudwatchomni.types.identity_provider_configuration.IdentityProviderConfiguration"
    ]
    """Identity provider configuration for the domain. Omit to leave unchanged."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateDomainForOrganizationInput) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "identity_providers" in value:
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
    return out


def deserialize_cbor(data: dict) -> UpdateDomainForOrganizationInput:
    out: UpdateDomainForOrganizationInput = {}  # type: ignore[typeddict-item]
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    else:
        out["domain_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("identityProviders") is not None:
        import capo_cloudwatchomni.types.identity_provider_list

        out["identity_providers"] = (
            capo_cloudwatchomni.types.identity_provider_list.deserialize_cbor(
                data["identityProviders"]
            )
        )
    if data.get("identityProviderConfiguration") is not None:
        import capo_cloudwatchomni.types.identity_provider_configuration

        out["identity_provider_configuration"] = (
            capo_cloudwatchomni.types.identity_provider_configuration.deserialize_cbor(
                data["identityProviderConfiguration"]
            )
        )
    return out
