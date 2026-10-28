"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#IntegrationCredential``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_cloudwatchomni.errors import DeserializationError, SerializationError
from capo_cloudwatchomni.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.api_key_credential
    import capo_cloudwatchomni.types.o_auth_client_credential
    import capo_cloudwatchomni.types.o_auth_code_credential


class IntegrationCredentialOauthCodeCredentialMember(TypedDict, closed=True):
    oauthCodeCredential: (
        "capo_cloudwatchomni.types.o_auth_code_credential.OAuthCodeCredential"
    )


class IntegrationCredentialOauthClientCredentialMember(TypedDict, closed=True):
    oauthClientCredential: (
        "capo_cloudwatchomni.types.o_auth_client_credential.OAuthClientCredential"
    )


class IntegrationCredentialApiKeyCredentialMember(TypedDict, closed=True):
    apiKeyCredential: "capo_cloudwatchomni.types.api_key_credential.ApiKeyCredential"


IntegrationCredential: TypeAlias = (
    IntegrationCredentialOauthCodeCredentialMember
    | IntegrationCredentialOauthClientCredentialMember
    | IntegrationCredentialApiKeyCredentialMember
    | UnknownUnionMember
)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IntegrationCredential) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"IntegrationCredential: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "oauthCodeCredential" in value:
        import capo_cloudwatchomni.types.o_auth_code_credential

        return {
            "oauthCodeCredential": capo_cloudwatchomni.types.o_auth_code_credential.serialize_cbor(
                value["oauthCodeCredential"]
            )
        }
    elif "oauthClientCredential" in value:
        import capo_cloudwatchomni.types.o_auth_client_credential

        return {
            "oauthClientCredential": capo_cloudwatchomni.types.o_auth_client_credential.serialize_cbor(
                value["oauthClientCredential"]
            )
        }
    elif "apiKeyCredential" in value:
        import capo_cloudwatchomni.types.api_key_credential

        return {
            "apiKeyCredential": capo_cloudwatchomni.types.api_key_credential.serialize_cbor(
                value["apiKeyCredential"]
            )
        }
    else:
        raise SerializationError("IntegrationCredential: no variant present")


def deserialize_cbor(data: dict) -> IntegrationCredential:
    if data.get("oauthCodeCredential") is not None:
        import capo_cloudwatchomni.types.o_auth_code_credential

        return {
            "oauthCodeCredential": capo_cloudwatchomni.types.o_auth_code_credential.deserialize_cbor(
                data["oauthCodeCredential"]
            )
        }
    elif data.get("oauthClientCredential") is not None:
        import capo_cloudwatchomni.types.o_auth_client_credential

        return {
            "oauthClientCredential": capo_cloudwatchomni.types.o_auth_client_credential.deserialize_cbor(
                data["oauthClientCredential"]
            )
        }
    elif data.get("apiKeyCredential") is not None:
        import capo_cloudwatchomni.types.api_key_credential

        return {
            "apiKeyCredential": capo_cloudwatchomni.types.api_key_credential.deserialize_cbor(
                data["apiKeyCredential"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("IntegrationCredential: no recognized variant key")


def redact_sensitive(value: IntegrationCredential) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "oauthCodeCredential" in value:
        out["oauthCodeCredential"] = "*** Sensitive Data Redacted ***"
    if "oauthClientCredential" in value:
        out["oauthClientCredential"] = "*** Sensitive Data Redacted ***"
    if "apiKeyCredential" in value:
        out["apiKeyCredential"] = "*** Sensitive Data Redacted ***"
    return out
