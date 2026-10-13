"""Generated from Smithy shape ``com.amazonaws.appfabric#Credential``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_appfabric.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_appfabric.types.api_key_credential
    import capo_appfabric.types.oauth2_credential


class _Credential_oauth2Credential(TypedDict, closed=True):
    oauth2Credential: "capo_appfabric.types.oauth2_credential.Oauth2Credential"


class _Credential_apiKeyCredential(TypedDict, closed=True):
    apiKeyCredential: "capo_appfabric.types.api_key_credential.ApiKeyCredential"


Credential: TypeAlias = _Credential_oauth2Credential | _Credential_apiKeyCredential


# --- restJson1 ser/de ---
def serialize_json(value: Credential) -> dict:
    if "oauth2Credential" in value:
        import capo_appfabric.types.oauth2_credential

        return {
            "oauth2Credential": capo_appfabric.types.oauth2_credential.serialize_json(
                value["oauth2Credential"]
            )
        }
    elif "apiKeyCredential" in value:
        import capo_appfabric.types.api_key_credential

        return {
            "apiKeyCredential": capo_appfabric.types.api_key_credential.serialize_json(
                value["apiKeyCredential"]
            )
        }
    else:
        raise SerializationError("Credential: no variant present")


def deserialize_json(data: dict) -> Credential:
    if data.get("oauth2Credential") is not None:
        import capo_appfabric.types.oauth2_credential

        return {
            "oauth2Credential": capo_appfabric.types.oauth2_credential.deserialize_json(
                data["oauth2Credential"]
            )
        }
    elif data.get("apiKeyCredential") is not None:
        import capo_appfabric.types.api_key_credential

        return {
            "apiKeyCredential": capo_appfabric.types.api_key_credential.deserialize_json(
                data["apiKeyCredential"]
            )
        }
    else:
        raise DeserializationError("Credential: no recognized variant key")


def redact_sensitive(value: Credential) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "oauth2Credential" in value:
        import capo_appfabric.types.oauth2_credential

        out["oauth2Credential"] = (
            capo_appfabric.types.oauth2_credential.redact_sensitive(
                value["oauth2Credential"]
            )
        )
    if "apiKeyCredential" in value:
        import capo_appfabric.types.api_key_credential

        out["apiKeyCredential"] = (
            capo_appfabric.types.api_key_credential.redact_sensitive(
                value["apiKeyCredential"]
            )
        )
    return out
