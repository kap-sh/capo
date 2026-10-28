"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CredentialProvider``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.gateway_api_key_credential_provider
    import capo_bedrock_agentcore_control.types.iam_credential_provider
    import capo_bedrock_agentcore_control.types.o_auth_credential_provider


class CredentialProviderOauthCredentialProviderMember(TypedDict, closed=True):
    oauthCredentialProvider: "capo_bedrock_agentcore_control.types.o_auth_credential_provider.OAuthCredentialProvider"


class CredentialProviderApiKeyCredentialProviderMember(TypedDict, closed=True):
    apiKeyCredentialProvider: "capo_bedrock_agentcore_control.types.gateway_api_key_credential_provider.GatewayApiKeyCredentialProvider"


class CredentialProviderIamCredentialProviderMember(TypedDict, closed=True):
    iamCredentialProvider: "capo_bedrock_agentcore_control.types.iam_credential_provider.IamCredentialProvider"


CredentialProvider: TypeAlias = (
    CredentialProviderOauthCredentialProviderMember
    | CredentialProviderApiKeyCredentialProviderMember
    | CredentialProviderIamCredentialProviderMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: CredentialProvider) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"CredentialProvider: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "oauthCredentialProvider" in value:
        import capo_bedrock_agentcore_control.types.o_auth_credential_provider

        return {
            "oauthCredentialProvider": capo_bedrock_agentcore_control.types.o_auth_credential_provider.serialize_json(
                value["oauthCredentialProvider"]
            )
        }
    elif "apiKeyCredentialProvider" in value:
        import capo_bedrock_agentcore_control.types.gateway_api_key_credential_provider

        return {
            "apiKeyCredentialProvider": capo_bedrock_agentcore_control.types.gateway_api_key_credential_provider.serialize_json(
                value["apiKeyCredentialProvider"]
            )
        }
    elif "iamCredentialProvider" in value:
        import capo_bedrock_agentcore_control.types.iam_credential_provider

        return {
            "iamCredentialProvider": capo_bedrock_agentcore_control.types.iam_credential_provider.serialize_json(
                value["iamCredentialProvider"]
            )
        }
    else:
        raise SerializationError("CredentialProvider: no variant present")


def deserialize_json(data: dict) -> CredentialProvider:
    if data.get("oauthCredentialProvider") is not None:
        import capo_bedrock_agentcore_control.types.o_auth_credential_provider

        return {
            "oauthCredentialProvider": capo_bedrock_agentcore_control.types.o_auth_credential_provider.deserialize_json(
                data["oauthCredentialProvider"]
            )
        }
    elif data.get("apiKeyCredentialProvider") is not None:
        import capo_bedrock_agentcore_control.types.gateway_api_key_credential_provider

        return {
            "apiKeyCredentialProvider": capo_bedrock_agentcore_control.types.gateway_api_key_credential_provider.deserialize_json(
                data["apiKeyCredentialProvider"]
            )
        }
    elif data.get("iamCredentialProvider") is not None:
        import capo_bedrock_agentcore_control.types.iam_credential_provider

        return {
            "iamCredentialProvider": capo_bedrock_agentcore_control.types.iam_credential_provider.deserialize_json(
                data["iamCredentialProvider"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("CredentialProvider: no recognized variant key")


def redact_sensitive(value: CredentialProvider) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "oauthCredentialProvider" in value:
        import capo_bedrock_agentcore_control.types.o_auth_credential_provider

        out["oauthCredentialProvider"] = (
            capo_bedrock_agentcore_control.types.o_auth_credential_provider.redact_sensitive(
                value["oauthCredentialProvider"]
            )
        )
    return out
