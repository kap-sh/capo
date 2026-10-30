"""Generated from Smithy shape ``com.amazonaws.continuum#UpdateIntegrationInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.integration_id
    import capo_continuum.types.update_provider_configuration


class UpdateIntegrationInput(TypedDict, closed=True):
    integration_id: "capo_continuum.types.integration_id.IntegrationId"
    """The unique identifier of the S3 integration to update."""
    provider_configuration: (
        "capo_continuum.types.update_provider_configuration.UpdateProviderConfiguration"
    )
    """The provider-specific changes to apply. The member must match the integration's provider type, and only S3 integrations can be updated."""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIntegrationInput) -> dict:
    out: dict = {}
    import capo_continuum.types.update_provider_configuration

    out["providerConfiguration"] = (
        capo_continuum.types.update_provider_configuration.serialize_json(
            value["provider_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateIntegrationInput:
    out: UpdateIntegrationInput = {}  # type: ignore[typeddict-item]
    if data.get("providerConfiguration") is not None:
        import capo_continuum.types.update_provider_configuration

        out["provider_configuration"] = (
            capo_continuum.types.update_provider_configuration.deserialize_json(
                data["providerConfiguration"]
            )
        )
    else:
        out["provider_configuration"] = {"$unknown": {"name": ""}}
    return out


def redact_sensitive(value: UpdateIntegrationInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "provider_configuration" in value:
        import capo_continuum.types.update_provider_configuration

        out["provider_configuration"] = (
            capo_continuum.types.update_provider_configuration.redact_sensitive(
                value["provider_configuration"]
            )
        )
    return out
