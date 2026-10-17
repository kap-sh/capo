"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#UpdateSpaceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatchomni.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.encryption_configuration
    import capo_cloudwatchomni.types.space_id


class UpdateSpaceInput(TypedDict, closed=True):
    space_id: "capo_cloudwatchomni.types.space_id.SpaceId"
    """The unique ID of the space to update."""
    name: NotRequired["str"]
    """A new name for the space. Omit to leave unchanged. Must be 3-64 characters: lowercase letters, numbers, and hyphens. It must begin and end with a letter or number and cannot contain consecutive hyphens."""
    encryption_configuration: NotRequired[
        "capo_cloudwatchomni.types.encryption_configuration.EncryptionConfiguration"
    ]
    """How to encrypt the space's data at rest. Omit to leave encryption unchanged. Pass `encryptionStrategy` AWS_OWNED to stop using a customer managed key and revert to service owned encryption."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateSpaceInput) -> dict:
    out: dict = {}
    out["spaceId"] = value["space_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "encryption_configuration" in value:
        import capo_cloudwatchomni.types.encryption_configuration

        out["encryptionConfiguration"] = (
            capo_cloudwatchomni.types.encryption_configuration.serialize_cbor(
                value["encryption_configuration"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> UpdateSpaceInput:
    out: UpdateSpaceInput = {}  # type: ignore[typeddict-item]
    if data.get("spaceId") is not None:
        out["space_id"] = data["spaceId"]
    else:
        raise DeserializationError("UpdateSpaceInput.space_id required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("encryptionConfiguration") is not None:
        import capo_cloudwatchomni.types.encryption_configuration

        out["encryption_configuration"] = (
            capo_cloudwatchomni.types.encryption_configuration.deserialize_cbor(
                data["encryptionConfiguration"]
            )
        )
    return out
