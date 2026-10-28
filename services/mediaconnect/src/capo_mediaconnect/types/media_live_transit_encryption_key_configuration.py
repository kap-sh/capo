"""Generated from Smithy shape ``com.amazonaws.mediaconnect#MediaLiveTransitEncryptionKeyConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mediaconnect.errors import DeserializationError, SerializationError
from capo_mediaconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_mediaconnect.types.automatic_encryption_key_configuration
    import capo_mediaconnect.types.secrets_manager_encryption_key_configuration


class MediaLiveTransitEncryptionKeyConfigurationSecretsManagerMember(
    TypedDict, closed=True
):
    SecretsManager: "capo_mediaconnect.types.secrets_manager_encryption_key_configuration.SecretsManagerEncryptionKeyConfiguration"


class MediaLiveTransitEncryptionKeyConfigurationAutomaticMember(TypedDict, closed=True):
    Automatic: "capo_mediaconnect.types.automatic_encryption_key_configuration.AutomaticEncryptionKeyConfiguration"


MediaLiveTransitEncryptionKeyConfiguration: TypeAlias = (
    MediaLiveTransitEncryptionKeyConfigurationSecretsManagerMember
    | MediaLiveTransitEncryptionKeyConfigurationAutomaticMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: MediaLiveTransitEncryptionKeyConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"MediaLiveTransitEncryptionKeyConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "SecretsManager" in value:
        import capo_mediaconnect.types.secrets_manager_encryption_key_configuration

        return {
            "secretsManager": capo_mediaconnect.types.secrets_manager_encryption_key_configuration.serialize_json(
                value["SecretsManager"]
            )
        }
    elif "Automatic" in value:
        import capo_mediaconnect.types.automatic_encryption_key_configuration

        return {
            "automatic": capo_mediaconnect.types.automatic_encryption_key_configuration.serialize_json(
                value["Automatic"]
            )
        }
    else:
        raise SerializationError(
            "MediaLiveTransitEncryptionKeyConfiguration: no variant present"
        )


def deserialize_json(data: dict) -> MediaLiveTransitEncryptionKeyConfiguration:
    if data.get("secretsManager") is not None:
        import capo_mediaconnect.types.secrets_manager_encryption_key_configuration

        return {
            "SecretsManager": capo_mediaconnect.types.secrets_manager_encryption_key_configuration.deserialize_json(
                data["secretsManager"]
            )
        }
    elif data.get("automatic") is not None:
        import capo_mediaconnect.types.automatic_encryption_key_configuration

        return {
            "Automatic": capo_mediaconnect.types.automatic_encryption_key_configuration.deserialize_json(
                data["automatic"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "MediaLiveTransitEncryptionKeyConfiguration: no recognized variant key"
        )
