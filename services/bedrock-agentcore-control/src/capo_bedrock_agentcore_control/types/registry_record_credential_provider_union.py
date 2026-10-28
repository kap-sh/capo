"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#RegistryRecordCredentialProviderUnion``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.registry_record_iam_credential_provider
    import capo_bedrock_agentcore_control.types.registry_record_o_auth_credential_provider


class RegistryRecordCredentialProviderUnionOauthCredentialProviderMember(
    TypedDict, closed=True
):
    oauthCredentialProvider: "capo_bedrock_agentcore_control.types.registry_record_o_auth_credential_provider.RegistryRecordOAuthCredentialProvider"


class RegistryRecordCredentialProviderUnionIamCredentialProviderMember(
    TypedDict, closed=True
):
    iamCredentialProvider: "capo_bedrock_agentcore_control.types.registry_record_iam_credential_provider.RegistryRecordIamCredentialProvider"


RegistryRecordCredentialProviderUnion: TypeAlias = (
    RegistryRecordCredentialProviderUnionOauthCredentialProviderMember
    | RegistryRecordCredentialProviderUnionIamCredentialProviderMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: RegistryRecordCredentialProviderUnion) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"RegistryRecordCredentialProviderUnion: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "oauthCredentialProvider" in value:
        import capo_bedrock_agentcore_control.types.registry_record_o_auth_credential_provider

        return {
            "oauthCredentialProvider": capo_bedrock_agentcore_control.types.registry_record_o_auth_credential_provider.serialize_json(
                value["oauthCredentialProvider"]
            )
        }
    elif "iamCredentialProvider" in value:
        import capo_bedrock_agentcore_control.types.registry_record_iam_credential_provider

        return {
            "iamCredentialProvider": capo_bedrock_agentcore_control.types.registry_record_iam_credential_provider.serialize_json(
                value["iamCredentialProvider"]
            )
        }
    else:
        raise SerializationError(
            "RegistryRecordCredentialProviderUnion: no variant present"
        )


def deserialize_json(data: dict) -> RegistryRecordCredentialProviderUnion:
    if data.get("oauthCredentialProvider") is not None:
        import capo_bedrock_agentcore_control.types.registry_record_o_auth_credential_provider

        return {
            "oauthCredentialProvider": capo_bedrock_agentcore_control.types.registry_record_o_auth_credential_provider.deserialize_json(
                data["oauthCredentialProvider"]
            )
        }
    elif data.get("iamCredentialProvider") is not None:
        import capo_bedrock_agentcore_control.types.registry_record_iam_credential_provider

        return {
            "iamCredentialProvider": capo_bedrock_agentcore_control.types.registry_record_iam_credential_provider.deserialize_json(
                data["iamCredentialProvider"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "RegistryRecordCredentialProviderUnion: no recognized variant key"
        )
