"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#UpdateIntegrationInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatchomni.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.integration_credential
    import capo_cloudwatchomni.types.integration_identifier
    import capo_cloudwatchomni.types.string_map


class UpdateIntegrationInput(TypedDict, closed=True):
    identifier: "capo_cloudwatchomni.types.integration_identifier.IntegrationIdentifier"
    """Identifies the integration to update — exactly one of integrationId, integrationArn, or integrationName."""
    credential: NotRequired[
        "capo_cloudwatchomni.types.integration_credential.IntegrationCredential"
    ]
    """The replacement credential used to authenticate with the provider."""
    integration_attributes: NotRequired[
        "capo_cloudwatchomni.types.string_map.StringMap"
    ]
    """The provider-specific attributes to associate with the integration."""
    role_arn: NotRequired["str"]
    """The Amazon Resource Name of the IAM role assumed to access the integration."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateIntegrationInput) -> dict:
    out: dict = {}
    import capo_cloudwatchomni.types.integration_identifier

    out["identifier"] = capo_cloudwatchomni.types.integration_identifier.serialize_cbor(
        value["identifier"]
    )
    if "credential" in value:
        import capo_cloudwatchomni.types.integration_credential

        out["credential"] = (
            capo_cloudwatchomni.types.integration_credential.serialize_cbor(
                value["credential"]
            )
        )
    if "integration_attributes" in value:
        import capo_cloudwatchomni.types.string_map

        out["integrationAttributes"] = (
            capo_cloudwatchomni.types.string_map.serialize_cbor(
                value["integration_attributes"]
            )
        )
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    return out


def deserialize_cbor(data: dict) -> UpdateIntegrationInput:
    out: UpdateIntegrationInput = {}  # type: ignore[typeddict-item]
    if data.get("identifier") is not None:
        import capo_cloudwatchomni.types.integration_identifier

        out["identifier"] = (
            capo_cloudwatchomni.types.integration_identifier.deserialize_cbor(
                data["identifier"]
            )
        )
    else:
        raise DeserializationError("UpdateIntegrationInput.identifier required")
    if data.get("credential") is not None:
        import capo_cloudwatchomni.types.integration_credential

        out["credential"] = (
            capo_cloudwatchomni.types.integration_credential.deserialize_cbor(
                data["credential"]
            )
        )
    if data.get("integrationAttributes") is not None:
        import capo_cloudwatchomni.types.string_map

        out["integration_attributes"] = (
            capo_cloudwatchomni.types.string_map.deserialize_cbor(
                data["integrationAttributes"]
            )
        )
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    return out


def redact_sensitive(value: UpdateIntegrationInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "credential" in value:
        import capo_cloudwatchomni.types.integration_credential

        out["credential"] = (
            capo_cloudwatchomni.types.integration_credential.redact_sensitive(
                value["credential"]
            )
        )
    return out
