"""Generated from Smithy shape ``com.amazonaws.continuum#StartIntegrationAuthorizationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.integration_authorization_provider_type
    import capo_continuum.types.integration_name


class StartIntegrationAuthorizationInput(TypedDict, closed=True):
    provider_type: "capo_continuum.types.integration_authorization_provider_type.IntegrationAuthorizationProviderType"
    """The provider to authorize. Only GITHUB is supported."""
    name: NotRequired["capo_continuum.types.integration_name.IntegrationName"]
    """The name the integration will be created with. When specified, the request fails with ConflictException if an integration with this name already exists in the account, before the caller leaves for the provider. The name is only checked: it is not reserved, stored, or authorized. CreateIntegration requires its own name, checks it again, and may use a different one."""


# --- restJson1 ser/de ---
def serialize_json(value: StartIntegrationAuthorizationInput) -> dict:
    out: dict = {}
    import capo_continuum.types.integration_authorization_provider_type

    out["providerType"] = (
        capo_continuum.types.integration_authorization_provider_type.serialize_json(
            value["provider_type"]
        )
    )
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> StartIntegrationAuthorizationInput:
    out: StartIntegrationAuthorizationInput = {}  # type: ignore[typeddict-item]
    if data.get("providerType") is not None:
        import capo_continuum.types.integration_authorization_provider_type

        out["provider_type"] = (
            capo_continuum.types.integration_authorization_provider_type.deserialize_json(
                data["providerType"]
            )
        )
    else:
        import typing

        out["provider_type"] = typing.cast(
            "capo_continuum.types.integration_authorization_provider_type.IntegrationAuthorizationProviderType",
            "",
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    return out
