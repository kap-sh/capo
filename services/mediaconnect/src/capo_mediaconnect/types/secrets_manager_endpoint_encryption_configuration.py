"""Generated from Smithy shape ``com.amazonaws.mediaconnect#SecretsManagerEndpointEncryptionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mediaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mediaconnect.types.endpoint_encryption_secret_configuration
    import capo_mediaconnect.types.endpoint_encryption_secret_type


class SecretsManagerEndpointEncryptionConfiguration(TypedDict, closed=True):
    encryption_secret_type: NotRequired[
        "capo_mediaconnect.types.endpoint_encryption_secret_type.EndpointEncryptionSecretType"
    ]
    """<p>The type of secret used to encrypt the connection. Valid values include the following:</p> <ul> <li> <p> <code>AES_128_KEY</code> – A 128-bit AES encryption key.</p> </li> <li> <p> <code>AES_192_KEY</code> – A 192-bit AES encryption key.</p> </li> <li> <p> <code>AES_256_KEY</code> – A 256-bit AES encryption key.</p> </li> <li> <p> <code>SRT_PASSPHRASE</code> – An SRT passphrase.</p> </li> </ul>"""
    encryption_secret: "capo_mediaconnect.types.endpoint_encryption_secret_configuration.EndpointEncryptionSecretConfiguration"
    """<p>The Secrets Manager secret that holds the key or passphrase used to encrypt the connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SecretsManagerEndpointEncryptionConfiguration) -> dict:
    out: dict = {}
    if "encryption_secret_type" in value:
        import capo_mediaconnect.types.endpoint_encryption_secret_type

        out["encryptionSecretType"] = (
            capo_mediaconnect.types.endpoint_encryption_secret_type.serialize_json(
                value["encryption_secret_type"]
            )
        )
    import capo_mediaconnect.types.endpoint_encryption_secret_configuration

    out["encryptionSecret"] = (
        capo_mediaconnect.types.endpoint_encryption_secret_configuration.serialize_json(
            value["encryption_secret"]
        )
    )
    return out


def deserialize_json(data: dict) -> SecretsManagerEndpointEncryptionConfiguration:
    out: SecretsManagerEndpointEncryptionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("encryptionSecretType") is not None:
        import capo_mediaconnect.types.endpoint_encryption_secret_type

        out["encryption_secret_type"] = (
            capo_mediaconnect.types.endpoint_encryption_secret_type.deserialize_json(
                data["encryptionSecretType"]
            )
        )
    if data.get("encryptionSecret") is not None:
        import capo_mediaconnect.types.endpoint_encryption_secret_configuration

        out["encryption_secret"] = (
            capo_mediaconnect.types.endpoint_encryption_secret_configuration.deserialize_json(
                data["encryptionSecret"]
            )
        )
    else:
        raise DeserializationError(
            "SecretsManagerEndpointEncryptionConfiguration.encryption_secret required"
        )
    return out
