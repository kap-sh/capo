"""Generated from Smithy shape ``com.amazonaws.pipes#SelfManagedKafkaAccessConfigurationCredentials``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_pipes.errors import DeserializationError, SerializationError
from capo_pipes.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_pipes.types.secret_manager_arn


class _SelfManagedKafkaAccessConfigurationCredentials_BasicAuth(TypedDict, closed=True):
    BasicAuth: "capo_pipes.types.secret_manager_arn.SecretManagerArn"


class _SelfManagedKafkaAccessConfigurationCredentials_SaslScram512Auth(
    TypedDict, closed=True
):
    SaslScram512Auth: "capo_pipes.types.secret_manager_arn.SecretManagerArn"


class _SelfManagedKafkaAccessConfigurationCredentials_SaslScram256Auth(
    TypedDict, closed=True
):
    SaslScram256Auth: "capo_pipes.types.secret_manager_arn.SecretManagerArn"


class _SelfManagedKafkaAccessConfigurationCredentials_ClientCertificateTlsAuth(
    TypedDict, closed=True
):
    ClientCertificateTlsAuth: "capo_pipes.types.secret_manager_arn.SecretManagerArn"


SelfManagedKafkaAccessConfigurationCredentials: TypeAlias = (
    _SelfManagedKafkaAccessConfigurationCredentials_BasicAuth
    | _SelfManagedKafkaAccessConfigurationCredentials_SaslScram512Auth
    | _SelfManagedKafkaAccessConfigurationCredentials_SaslScram256Auth
    | _SelfManagedKafkaAccessConfigurationCredentials_ClientCertificateTlsAuth
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: SelfManagedKafkaAccessConfigurationCredentials) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"SelfManagedKafkaAccessConfigurationCredentials: cannot serialize unknown variant {value.name!r}"
        )
    elif "BasicAuth" in value:
        return {"BasicAuth": value["BasicAuth"]}
    elif "SaslScram512Auth" in value:
        return {"SaslScram512Auth": value["SaslScram512Auth"]}
    elif "SaslScram256Auth" in value:
        return {"SaslScram256Auth": value["SaslScram256Auth"]}
    elif "ClientCertificateTlsAuth" in value:
        return {"ClientCertificateTlsAuth": value["ClientCertificateTlsAuth"]}
    else:
        raise SerializationError(
            "SelfManagedKafkaAccessConfigurationCredentials: no variant present"
        )


def deserialize_json(data: dict) -> SelfManagedKafkaAccessConfigurationCredentials:
    if data.get("BasicAuth") is not None:
        return {"BasicAuth": data["BasicAuth"]}
    elif data.get("SaslScram512Auth") is not None:
        return {"SaslScram512Auth": data["SaslScram512Auth"]}
    elif data.get("SaslScram256Auth") is not None:
        return {"SaslScram256Auth": data["SaslScram256Auth"]}
    elif data.get("ClientCertificateTlsAuth") is not None:
        return {"ClientCertificateTlsAuth": data["ClientCertificateTlsAuth"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "SelfManagedKafkaAccessConfigurationCredentials: no recognized variant key"
        )
