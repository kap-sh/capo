"""Generated from Smithy shape ``com.amazonaws.quicksight#AuthenticationMetadata``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError, SerializationError
from capo_quicksight.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_quicksight.types.api_key_connection_metadata
    import capo_quicksight.types.authorization_code_grant_metadata
    import capo_quicksight.types.basic_auth_connection_metadata
    import capo_quicksight.types.client_credentials_grant_metadata
    import capo_quicksight.types.iam_connection_metadata
    import capo_quicksight.types.none_connection_metadata


class _AuthenticationMetadata_AuthorizationCodeGrantMetadata(TypedDict, closed=True):
    AuthorizationCodeGrantMetadata: "capo_quicksight.types.authorization_code_grant_metadata.AuthorizationCodeGrantMetadata"


class _AuthenticationMetadata_ClientCredentialsGrantMetadata(TypedDict, closed=True):
    ClientCredentialsGrantMetadata: "capo_quicksight.types.client_credentials_grant_metadata.ClientCredentialsGrantMetadata"


class _AuthenticationMetadata_BasicAuthConnectionMetadata(TypedDict, closed=True):
    BasicAuthConnectionMetadata: "capo_quicksight.types.basic_auth_connection_metadata.BasicAuthConnectionMetadata"


class _AuthenticationMetadata_ApiKeyConnectionMetadata(TypedDict, closed=True):
    ApiKeyConnectionMetadata: (
        "capo_quicksight.types.api_key_connection_metadata.APIKeyConnectionMetadata"
    )


class _AuthenticationMetadata_NoneConnectionMetadata(TypedDict, closed=True):
    NoneConnectionMetadata: (
        "capo_quicksight.types.none_connection_metadata.NoneConnectionMetadata"
    )


class _AuthenticationMetadata_IamConnectionMetadata(TypedDict, closed=True):
    IamConnectionMetadata: (
        "capo_quicksight.types.iam_connection_metadata.IAMConnectionMetadata"
    )


AuthenticationMetadata: TypeAlias = (
    _AuthenticationMetadata_AuthorizationCodeGrantMetadata
    | _AuthenticationMetadata_ClientCredentialsGrantMetadata
    | _AuthenticationMetadata_BasicAuthConnectionMetadata
    | _AuthenticationMetadata_ApiKeyConnectionMetadata
    | _AuthenticationMetadata_NoneConnectionMetadata
    | _AuthenticationMetadata_IamConnectionMetadata
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: AuthenticationMetadata) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"AuthenticationMetadata: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "AuthorizationCodeGrantMetadata" in value:
        import capo_quicksight.types.authorization_code_grant_metadata

        return {
            "AuthorizationCodeGrantMetadata": capo_quicksight.types.authorization_code_grant_metadata.serialize_json(
                value["AuthorizationCodeGrantMetadata"]
            )
        }
    elif "ClientCredentialsGrantMetadata" in value:
        import capo_quicksight.types.client_credentials_grant_metadata

        return {
            "ClientCredentialsGrantMetadata": capo_quicksight.types.client_credentials_grant_metadata.serialize_json(
                value["ClientCredentialsGrantMetadata"]
            )
        }
    elif "BasicAuthConnectionMetadata" in value:
        import capo_quicksight.types.basic_auth_connection_metadata

        return {
            "BasicAuthConnectionMetadata": capo_quicksight.types.basic_auth_connection_metadata.serialize_json(
                value["BasicAuthConnectionMetadata"]
            )
        }
    elif "ApiKeyConnectionMetadata" in value:
        import capo_quicksight.types.api_key_connection_metadata

        return {
            "ApiKeyConnectionMetadata": capo_quicksight.types.api_key_connection_metadata.serialize_json(
                value["ApiKeyConnectionMetadata"]
            )
        }
    elif "NoneConnectionMetadata" in value:
        import capo_quicksight.types.none_connection_metadata

        return {
            "NoneConnectionMetadata": capo_quicksight.types.none_connection_metadata.serialize_json(
                value["NoneConnectionMetadata"]
            )
        }
    elif "IamConnectionMetadata" in value:
        import capo_quicksight.types.iam_connection_metadata

        return {
            "IamConnectionMetadata": capo_quicksight.types.iam_connection_metadata.serialize_json(
                value["IamConnectionMetadata"]
            )
        }
    else:
        raise SerializationError("AuthenticationMetadata: no variant present")


def deserialize_json(data: dict) -> AuthenticationMetadata:
    if data.get("AuthorizationCodeGrantMetadata") is not None:
        import capo_quicksight.types.authorization_code_grant_metadata

        return {
            "AuthorizationCodeGrantMetadata": capo_quicksight.types.authorization_code_grant_metadata.deserialize_json(
                data["AuthorizationCodeGrantMetadata"]
            )
        }
    elif data.get("ClientCredentialsGrantMetadata") is not None:
        import capo_quicksight.types.client_credentials_grant_metadata

        return {
            "ClientCredentialsGrantMetadata": capo_quicksight.types.client_credentials_grant_metadata.deserialize_json(
                data["ClientCredentialsGrantMetadata"]
            )
        }
    elif data.get("BasicAuthConnectionMetadata") is not None:
        import capo_quicksight.types.basic_auth_connection_metadata

        return {
            "BasicAuthConnectionMetadata": capo_quicksight.types.basic_auth_connection_metadata.deserialize_json(
                data["BasicAuthConnectionMetadata"]
            )
        }
    elif data.get("ApiKeyConnectionMetadata") is not None:
        import capo_quicksight.types.api_key_connection_metadata

        return {
            "ApiKeyConnectionMetadata": capo_quicksight.types.api_key_connection_metadata.deserialize_json(
                data["ApiKeyConnectionMetadata"]
            )
        }
    elif data.get("NoneConnectionMetadata") is not None:
        import capo_quicksight.types.none_connection_metadata

        return {
            "NoneConnectionMetadata": capo_quicksight.types.none_connection_metadata.deserialize_json(
                data["NoneConnectionMetadata"]
            )
        }
    elif data.get("IamConnectionMetadata") is not None:
        import capo_quicksight.types.iam_connection_metadata

        return {
            "IamConnectionMetadata": capo_quicksight.types.iam_connection_metadata.deserialize_json(
                data["IamConnectionMetadata"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("AuthenticationMetadata: no recognized variant key")


def redact_sensitive(value: AuthenticationMetadata) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "AuthorizationCodeGrantMetadata" in value:
        import capo_quicksight.types.authorization_code_grant_metadata

        out["AuthorizationCodeGrantMetadata"] = (
            capo_quicksight.types.authorization_code_grant_metadata.redact_sensitive(
                value["AuthorizationCodeGrantMetadata"]
            )
        )
    if "ClientCredentialsGrantMetadata" in value:
        import capo_quicksight.types.client_credentials_grant_metadata

        out["ClientCredentialsGrantMetadata"] = (
            capo_quicksight.types.client_credentials_grant_metadata.redact_sensitive(
                value["ClientCredentialsGrantMetadata"]
            )
        )
    if "BasicAuthConnectionMetadata" in value:
        import capo_quicksight.types.basic_auth_connection_metadata

        out["BasicAuthConnectionMetadata"] = (
            capo_quicksight.types.basic_auth_connection_metadata.redact_sensitive(
                value["BasicAuthConnectionMetadata"]
            )
        )
    if "ApiKeyConnectionMetadata" in value:
        import capo_quicksight.types.api_key_connection_metadata

        out["ApiKeyConnectionMetadata"] = (
            capo_quicksight.types.api_key_connection_metadata.redact_sensitive(
                value["ApiKeyConnectionMetadata"]
            )
        )
    return out
