"""Generated from Smithy shape ``com.amazonaws.continuum#CreateIntegrationInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.integration_client_token
    import capo_continuum.types.integration_name
    import capo_continuum.types.provider_configuration


class CreateIntegrationInput(TypedDict, closed=True):
    client_token: NotRequired[
        "capo_continuum.types.integration_client_token.IntegrationClientToken"
    ]
    """An optional token identifying one create attempt within the caller's account, Region, and operation. SDKs generate a token when omitted. If a request reaches the service without a token, the service generates one for that request. Each request without a token starts a new attempt. To replay an attempt, supply the same token and identical input. Authorized users and roles in the same account can retry an attempt this way. Token records are retained for eight hours after success or terminal failure, including after deletion of a successfully created integration. Different input with the same token returns ValidationException."""
    name: "capo_continuum.types.integration_name.IntegrationName"
    """The name for the integration."""
    provider_configuration: (
        "capo_continuum.types.provider_configuration.ProviderConfiguration"
    )
    """The provider-specific configuration required to create the integration. Only one member may be specified."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateIntegrationInput) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["name"] = value["name"]
    import capo_continuum.types.provider_configuration

    out["providerConfiguration"] = (
        capo_continuum.types.provider_configuration.serialize_json(
            value["provider_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateIntegrationInput:
    out: CreateIntegrationInput = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("providerConfiguration") is not None:
        import capo_continuum.types.provider_configuration

        out["provider_configuration"] = (
            capo_continuum.types.provider_configuration.deserialize_json(
                data["providerConfiguration"]
            )
        )
    else:
        out["provider_configuration"] = {"$unknown": {"name": ""}}
    return out


def redact_sensitive(value: CreateIntegrationInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "provider_configuration" in value:
        import capo_continuum.types.provider_configuration

        out["provider_configuration"] = (
            capo_continuum.types.provider_configuration.redact_sensitive(
                value["provider_configuration"]
            )
        )
    return out
