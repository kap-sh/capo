"""Generated from Smithy shape ``com.amazonaws.mediaconnect#TlsEncryptionConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mediaconnect.errors import DeserializationError, SerializationError
from capo_mediaconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_mediaconnect.types.public_tls_encryption_configuration


class _TlsEncryptionConfiguration_Public(TypedDict, closed=True):
    Public: "capo_mediaconnect.types.public_tls_encryption_configuration.PublicTlsEncryptionConfiguration"


TlsEncryptionConfiguration: TypeAlias = (
    _TlsEncryptionConfiguration_Public | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: TlsEncryptionConfiguration) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"TlsEncryptionConfiguration: cannot serialize unknown variant {value.name!r}"
        )
    elif "Public" in value:
        import capo_mediaconnect.types.public_tls_encryption_configuration

        return {
            "public": capo_mediaconnect.types.public_tls_encryption_configuration.serialize_json(
                value["Public"]
            )
        }
    else:
        raise SerializationError("TlsEncryptionConfiguration: no variant present")


def deserialize_json(data: dict) -> TlsEncryptionConfiguration:
    if data.get("public") is not None:
        import capo_mediaconnect.types.public_tls_encryption_configuration

        return {
            "Public": capo_mediaconnect.types.public_tls_encryption_configuration.deserialize_json(
                data["public"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "TlsEncryptionConfiguration: no recognized variant key"
        )
