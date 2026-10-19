"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#CredentialsProvider``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_license_manager_user_subscriptions.errors import (
    DeserializationError,
    SerializationError,
)
from capo_license_manager_user_subscriptions.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_license_manager_user_subscriptions.types.secrets_manager_credentials_provider


class _CredentialsProvider_SecretsManagerCredentialsProvider(TypedDict, closed=True):
    SecretsManagerCredentialsProvider: "capo_license_manager_user_subscriptions.types.secrets_manager_credentials_provider.SecretsManagerCredentialsProvider"


CredentialsProvider: TypeAlias = (
    _CredentialsProvider_SecretsManagerCredentialsProvider | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: CredentialsProvider) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"CredentialsProvider: cannot serialize unknown variant {value.name!r}"
        )
    elif "SecretsManagerCredentialsProvider" in value:
        import capo_license_manager_user_subscriptions.types.secrets_manager_credentials_provider

        return {
            "SecretsManagerCredentialsProvider": capo_license_manager_user_subscriptions.types.secrets_manager_credentials_provider.serialize_json(
                value["SecretsManagerCredentialsProvider"]
            )
        }
    else:
        raise SerializationError("CredentialsProvider: no variant present")


def deserialize_json(data: dict) -> CredentialsProvider:
    if data.get("SecretsManagerCredentialsProvider") is not None:
        import capo_license_manager_user_subscriptions.types.secrets_manager_credentials_provider

        return {
            "SecretsManagerCredentialsProvider": capo_license_manager_user_subscriptions.types.secrets_manager_credentials_provider.deserialize_json(
                data["SecretsManagerCredentialsProvider"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("CredentialsProvider: no recognized variant key")
