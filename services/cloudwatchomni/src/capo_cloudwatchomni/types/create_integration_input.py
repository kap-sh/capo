"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#CreateIntegrationInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatchomni.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.integration_credential
    import capo_cloudwatchomni.types.integration_type
    import capo_cloudwatchomni.types.string_map
    import capo_cloudwatchomni.types.tag_map


class CreateIntegrationInput(TypedDict, closed=True):
    integration_type: "capo_cloudwatchomni.types.integration_type.IntegrationType"
    """The type of third-party provider to integrate with."""
    name: "str"
    """The name for the new integration; unique within the account."""
    credential: NotRequired[
        "capo_cloudwatchomni.types.integration_credential.IntegrationCredential"
    ]
    """The credential used to authenticate with the third-party provider."""
    integration_attributes: NotRequired[
        "capo_cloudwatchomni.types.string_map.StringMap"
    ]
    """Provider-specific attributes to associate with the integration."""
    role_arn: NotRequired["str"]
    """The Amazon Resource Name of the IAM role assumed to access the integration."""
    tags: NotRequired["capo_cloudwatchomni.types.tag_map.TagMap"]
    """Tags to apply to the integration at creation time (Tagris tag-on-create)."""
    client_token: NotRequired["str"]
    """Idempotency token for safe retries. Retrying with the same token returns the original integration instead of creating a duplicate."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateIntegrationInput) -> dict:
    out: dict = {}
    import capo_cloudwatchomni.types.integration_type

    out["integrationType"] = capo_cloudwatchomni.types.integration_type.serialize_cbor(
        value["integration_type"]
    )
    out["name"] = value["name"]
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
    if "tags" in value:
        import capo_cloudwatchomni.types.tag_map

        out["tags"] = capo_cloudwatchomni.types.tag_map.serialize_cbor(value["tags"])
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_cbor(data: dict) -> CreateIntegrationInput:
    out: CreateIntegrationInput = {}  # type: ignore[typeddict-item]
    if data.get("integrationType") is not None:
        import capo_cloudwatchomni.types.integration_type

        out["integration_type"] = (
            capo_cloudwatchomni.types.integration_type.deserialize_cbor(
                data["integrationType"]
            )
        )
    else:
        raise DeserializationError("CreateIntegrationInput.integration_type required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateIntegrationInput.name required")
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
    if data.get("tags") is not None:
        import capo_cloudwatchomni.types.tag_map

        out["tags"] = capo_cloudwatchomni.types.tag_map.deserialize_cbor(data["tags"])
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out


def redact_sensitive(value: CreateIntegrationInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "credential" in value:
        import capo_cloudwatchomni.types.integration_credential

        out["credential"] = (
            capo_cloudwatchomni.types.integration_credential.redact_sensitive(
                value["credential"]
            )
        )
    return out
