"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterInputTransitEncryptionKeyConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mediaconnect.errors import DeserializationError, SerializationError
from capo_mediaconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_mediaconnect.types.automatic_encryption_key_configuration
    import capo_mediaconnect.types.secrets_manager_encryption_key_configuration


class RouterInputTransitEncryptionKeyConfigurationSecretsManagerMember(
    TypedDict, closed=True
):
    SecretsManager: "capo_mediaconnect.types.secrets_manager_encryption_key_configuration.SecretsManagerEncryptionKeyConfiguration"


class RouterInputTransitEncryptionKeyConfigurationAutomaticMember(
    TypedDict, closed=True
):
    Automatic: "capo_mediaconnect.types.automatic_encryption_key_configuration.AutomaticEncryptionKeyConfiguration"


RouterInputTransitEncryptionKeyConfiguration: TypeAlias = (
    RouterInputTransitEncryptionKeyConfigurationSecretsManagerMember
    | RouterInputTransitEncryptionKeyConfigurationAutomaticMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: RouterInputTransitEncryptionKeyConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"RouterInputTransitEncryptionKeyConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
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
            "RouterInputTransitEncryptionKeyConfiguration: no variant present"
        )


def deserialize_json(data: dict) -> RouterInputTransitEncryptionKeyConfiguration:
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
            "RouterInputTransitEncryptionKeyConfiguration: no recognized variant key"
        )
