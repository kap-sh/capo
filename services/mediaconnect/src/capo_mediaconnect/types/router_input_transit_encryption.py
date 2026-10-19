"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterInputTransitEncryption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.router_input_transit_encryption_key_configuration
    import capo_mediaconnect.types.router_input_transit_encryption_key_type


class RouterInputTransitEncryption(TypedDict, closed=True):
    encryption_key_type: NotRequired[
        "capo_mediaconnect.types.router_input_transit_encryption_key_type.RouterInputTransitEncryptionKeyType"
    ]
    """<p>Specifies the type of encryption key to use for transit encryption.</p>"""
    encryption_key_configuration: "capo_mediaconnect.types.router_input_transit_encryption_key_configuration.RouterInputTransitEncryptionKeyConfiguration"
    """<p>Contains the configuration details for the encryption key used in transit encryption, including the key source and associated parameters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouterInputTransitEncryption) -> dict:
    out: dict = {}
    if "encryption_key_type" in value:
        import capo_mediaconnect.types.router_input_transit_encryption_key_type

        out["encryptionKeyType"] = (
            capo_mediaconnect.types.router_input_transit_encryption_key_type.serialize_json(
                value["encryption_key_type"]
            )
        )
    import capo_mediaconnect.types.router_input_transit_encryption_key_configuration

    out["encryptionKeyConfiguration"] = (
        capo_mediaconnect.types.router_input_transit_encryption_key_configuration.serialize_json(
            value["encryption_key_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> RouterInputTransitEncryption:
    out: RouterInputTransitEncryption = {}  # type: ignore[typeddict-item]
    if data.get("encryptionKeyType") is not None:
        import capo_mediaconnect.types.router_input_transit_encryption_key_type

        out["encryption_key_type"] = (
            capo_mediaconnect.types.router_input_transit_encryption_key_type.deserialize_json(
                data["encryptionKeyType"]
            )
        )
    if data.get("encryptionKeyConfiguration") is not None:
        import capo_mediaconnect.types.router_input_transit_encryption_key_configuration

        out["encryption_key_configuration"] = (
            capo_mediaconnect.types.router_input_transit_encryption_key_configuration.deserialize_json(
                data["encryptionKeyConfiguration"]
            )
        )
    else:
        import capo_mediaconnect.types._unknown

        out["encryption_key_configuration"] = (
            capo_mediaconnect.types._unknown.UnknownUnionMember("")
        )
    return out
