"""Generated from Smithy shape ``com.amazonaws.mediaconnect#TlsEncryption``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.tls_encryption_configuration
    import capo_mediaconnect.types.tls_encryption_type


class TlsEncryption(TypedDict, closed=True):
    encryption_type: NotRequired[
        "capo_mediaconnect.types.tls_encryption_type.TlsEncryptionType"
    ]
    """<p>The type of TLS encryption to use for the connection.</p>"""
    encryption_configuration: "capo_mediaconnect.types.tls_encryption_configuration.TlsEncryptionConfiguration"
    """<p>The configuration settings for the specified TLS encryption type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TlsEncryption) -> dict:
    out: dict = {}
    if "encryption_type" in value:
        import capo_mediaconnect.types.tls_encryption_type

        out["encryptionType"] = (
            capo_mediaconnect.types.tls_encryption_type.serialize_json(
                value["encryption_type"]
            )
        )
    import capo_mediaconnect.types.tls_encryption_configuration

    out["encryptionConfiguration"] = (
        capo_mediaconnect.types.tls_encryption_configuration.serialize_json(
            value["encryption_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> TlsEncryption:
    out: TlsEncryption = {}  # type: ignore[typeddict-item]
    if data.get("encryptionType") is not None:
        import capo_mediaconnect.types.tls_encryption_type

        out["encryption_type"] = (
            capo_mediaconnect.types.tls_encryption_type.deserialize_json(
                data["encryptionType"]
            )
        )
    if data.get("encryptionConfiguration") is not None:
        import capo_mediaconnect.types.tls_encryption_configuration

        out["encryption_configuration"] = (
            capo_mediaconnect.types.tls_encryption_configuration.deserialize_json(
                data["encryptionConfiguration"]
            )
        )
    else:
        import capo_mediaconnect.types._unknown

        out["encryption_configuration"] = (
            capo_mediaconnect.types._unknown.UnknownUnionMember("")
        )
    return out
