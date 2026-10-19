"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#RegistryRecordCredentialProviderUnion``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_agent_registry_control.errors import DeserializationError, SerializationError
from capo_agent_registry_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_agent_registry_control.types.registry_record_iam_credential_provider
    import capo_agent_registry_control.types.registry_record_o_auth_credential_provider


class _RegistryRecordCredentialProviderUnion_oauthCredentialProvider(
    TypedDict, closed=True
):
    oauthCredentialProvider: "capo_agent_registry_control.types.registry_record_o_auth_credential_provider.RegistryRecordOAuthCredentialProvider"


class _RegistryRecordCredentialProviderUnion_iamCredentialProvider(
    TypedDict, closed=True
):
    iamCredentialProvider: "capo_agent_registry_control.types.registry_record_iam_credential_provider.RegistryRecordIamCredentialProvider"


RegistryRecordCredentialProviderUnion: TypeAlias = (
    _RegistryRecordCredentialProviderUnion_oauthCredentialProvider
    | _RegistryRecordCredentialProviderUnion_iamCredentialProvider
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: RegistryRecordCredentialProviderUnion) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"RegistryRecordCredentialProviderUnion: cannot serialize unknown variant {value.name!r}"
        )
    elif "oauthCredentialProvider" in value:
        import capo_agent_registry_control.types.registry_record_o_auth_credential_provider

        return {
            "oauthCredentialProvider": capo_agent_registry_control.types.registry_record_o_auth_credential_provider.serialize_json(
                value["oauthCredentialProvider"]
            )
        }
    elif "iamCredentialProvider" in value:
        import capo_agent_registry_control.types.registry_record_iam_credential_provider

        return {
            "iamCredentialProvider": capo_agent_registry_control.types.registry_record_iam_credential_provider.serialize_json(
                value["iamCredentialProvider"]
            )
        }
    else:
        raise SerializationError(
            "RegistryRecordCredentialProviderUnion: no variant present"
        )


def deserialize_json(data: dict) -> RegistryRecordCredentialProviderUnion:
    if data.get("oauthCredentialProvider") is not None:
        import capo_agent_registry_control.types.registry_record_o_auth_credential_provider

        return {
            "oauthCredentialProvider": capo_agent_registry_control.types.registry_record_o_auth_credential_provider.deserialize_json(
                data["oauthCredentialProvider"]
            )
        }
    elif data.get("iamCredentialProvider") is not None:
        import capo_agent_registry_control.types.registry_record_iam_credential_provider

        return {
            "iamCredentialProvider": capo_agent_registry_control.types.registry_record_iam_credential_provider.deserialize_json(
                data["iamCredentialProvider"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "RegistryRecordCredentialProviderUnion: no recognized variant key"
        )
