"""Generated from Smithy shape ``com.amazonaws.mediaconnect#MediaLiveTransitEncryption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.media_live_transit_encryption_key_configuration
    import capo_mediaconnect.types.media_live_transit_encryption_key_type


class MediaLiveTransitEncryption(TypedDict, closed=True):
    encryption_key_type: NotRequired[
        "capo_mediaconnect.types.media_live_transit_encryption_key_type.MediaLiveTransitEncryptionKeyType"
    ]
    """<p>The type of encryption key to use for MediaLive transit encryption.</p>"""
    encryption_key_configuration: "capo_mediaconnect.types.media_live_transit_encryption_key_configuration.MediaLiveTransitEncryptionKeyConfiguration"
    """<p>The configuration details for the MediaLive encryption key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MediaLiveTransitEncryption) -> dict:
    out: dict = {}
    if "encryption_key_type" in value:
        import capo_mediaconnect.types.media_live_transit_encryption_key_type

        out["encryptionKeyType"] = (
            capo_mediaconnect.types.media_live_transit_encryption_key_type.serialize_json(
                value["encryption_key_type"]
            )
        )
    import capo_mediaconnect.types.media_live_transit_encryption_key_configuration

    out["encryptionKeyConfiguration"] = (
        capo_mediaconnect.types.media_live_transit_encryption_key_configuration.serialize_json(
            value["encryption_key_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> MediaLiveTransitEncryption:
    out: MediaLiveTransitEncryption = {}  # type: ignore[typeddict-item]
    if data.get("encryptionKeyType") is not None:
        import capo_mediaconnect.types.media_live_transit_encryption_key_type

        out["encryption_key_type"] = (
            capo_mediaconnect.types.media_live_transit_encryption_key_type.deserialize_json(
                data["encryptionKeyType"]
            )
        )
    if data.get("encryptionKeyConfiguration") is not None:
        import capo_mediaconnect.types.media_live_transit_encryption_key_configuration

        out["encryption_key_configuration"] = (
            capo_mediaconnect.types.media_live_transit_encryption_key_configuration.deserialize_json(
                data["encryptionKeyConfiguration"]
            )
        )
    else:
        import capo_mediaconnect.types._unknown

        out["encryption_key_configuration"] = (
            capo_mediaconnect.types._unknown.UnknownUnionMember("")
        )
    return out
