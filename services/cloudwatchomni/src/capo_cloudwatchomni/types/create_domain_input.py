"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#CreateDomainInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.client_token
    import capo_cloudwatchomni.types.identity_provider_configuration
    import capo_cloudwatchomni.types.identity_provider_list
    import capo_cloudwatchomni.types.tag_map


class CreateDomainInput(TypedDict, closed=True):
    name: "str"
    """A name that identifies the domain. Must be 3-63 characters: lowercase letters, numbers, and hyphens. It must begin and end with a letter or number and cannot contain consecutive hyphens."""
    identity_providers: (
        "capo_cloudwatchomni.types.identity_provider_list.IdentityProviderList"
    )
    """The identity providers to configure for the domain."""
    identity_provider_configuration: NotRequired[
        "capo_cloudwatchomni.types.identity_provider_configuration.IdentityProviderConfiguration"
    ]
    """Identity provider configuration for the domain."""
    tags: NotRequired["capo_cloudwatchomni.types.tag_map.TagMap"]
    """The tags to associate with the domain."""
    client_token: NotRequired["capo_cloudwatchomni.types.client_token.ClientToken"]
    """Idempotency token for safe retries. Repeated requests with the same token return the original result instead of creating a duplicate."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateDomainInput) -> dict:
    out: dict = {}
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
    if "tags" in value:
        import capo_cloudwatchomni.types.tag_map

        out["tags"] = capo_cloudwatchomni.types.tag_map.serialize_cbor(value["tags"])
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_cbor(data: dict) -> CreateDomainInput:
    out: CreateDomainInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
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
    if data.get("tags") is not None:
        import capo_cloudwatchomni.types.tag_map

        out["tags"] = capo_cloudwatchomni.types.tag_map.deserialize_cbor(data["tags"])
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
