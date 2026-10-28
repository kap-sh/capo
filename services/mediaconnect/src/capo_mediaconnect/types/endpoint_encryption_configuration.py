"""Generated from Smithy shape ``com.amazonaws.mediaconnect#EndpointEncryptionConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mediaconnect.errors import DeserializationError, SerializationError
from capo_mediaconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_mediaconnect.types.automatic_endpoint_encryption_configuration
    import capo_mediaconnect.types.secrets_manager_endpoint_encryption_configuration


class EndpointEncryptionConfigurationSecretsManagerMember(TypedDict, closed=True):
    SecretsManager: "capo_mediaconnect.types.secrets_manager_endpoint_encryption_configuration.SecretsManagerEndpointEncryptionConfiguration"


class EndpointEncryptionConfigurationAutomaticMember(TypedDict, closed=True):
    Automatic: "capo_mediaconnect.types.automatic_endpoint_encryption_configuration.AutomaticEndpointEncryptionConfiguration"


EndpointEncryptionConfiguration: TypeAlias = (
    EndpointEncryptionConfigurationSecretsManagerMember
    | EndpointEncryptionConfigurationAutomaticMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: EndpointEncryptionConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"EndpointEncryptionConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "SecretsManager" in value:
        import capo_mediaconnect.types.secrets_manager_endpoint_encryption_configuration

        return {
            "secretsManager": capo_mediaconnect.types.secrets_manager_endpoint_encryption_configuration.serialize_json(
                value["SecretsManager"]
            )
        }
    elif "Automatic" in value:
        import capo_mediaconnect.types.automatic_endpoint_encryption_configuration

        return {
            "automatic": capo_mediaconnect.types.automatic_endpoint_encryption_configuration.serialize_json(
                value["Automatic"]
            )
        }
    else:
        raise SerializationError("EndpointEncryptionConfiguration: no variant present")


def deserialize_json(data: dict) -> EndpointEncryptionConfiguration:
    if data.get("secretsManager") is not None:
        import capo_mediaconnect.types.secrets_manager_endpoint_encryption_configuration

        return {
            "SecretsManager": capo_mediaconnect.types.secrets_manager_endpoint_encryption_configuration.deserialize_json(
                data["secretsManager"]
            )
        }
    elif data.get("automatic") is not None:
        import capo_mediaconnect.types.automatic_endpoint_encryption_configuration

        return {
            "Automatic": capo_mediaconnect.types.automatic_endpoint_encryption_configuration.deserialize_json(
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
            "EndpointEncryptionConfiguration: no recognized variant key"
        )
