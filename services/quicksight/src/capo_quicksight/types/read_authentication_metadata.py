"""Generated from Smithy shape ``com.amazonaws.quicksight#ReadAuthenticationMetadata``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_quicksight.types.read_api_key_connection_metadata
    import capo_quicksight.types.read_authorization_code_grant_metadata
    import capo_quicksight.types.read_basic_auth_connection_metadata
    import capo_quicksight.types.read_client_credentials_grant_metadata
    import capo_quicksight.types.read_iam_connection_metadata
    import capo_quicksight.types.read_none_connection_metadata


class _ReadAuthenticationMetadata_AuthorizationCodeGrantMetadata(
    TypedDict, closed=True
):
    AuthorizationCodeGrantMetadata: "capo_quicksight.types.read_authorization_code_grant_metadata.ReadAuthorizationCodeGrantMetadata"


class _ReadAuthenticationMetadata_ClientCredentialsGrantMetadata(
    TypedDict, closed=True
):
    ClientCredentialsGrantMetadata: "capo_quicksight.types.read_client_credentials_grant_metadata.ReadClientCredentialsGrantMetadata"


class _ReadAuthenticationMetadata_BasicAuthConnectionMetadata(TypedDict, closed=True):
    BasicAuthConnectionMetadata: "capo_quicksight.types.read_basic_auth_connection_metadata.ReadBasicAuthConnectionMetadata"


class _ReadAuthenticationMetadata_ApiKeyConnectionMetadata(TypedDict, closed=True):
    ApiKeyConnectionMetadata: "capo_quicksight.types.read_api_key_connection_metadata.ReadAPIKeyConnectionMetadata"


class _ReadAuthenticationMetadata_NoneConnectionMetadata(TypedDict, closed=True):
    NoneConnectionMetadata: (
        "capo_quicksight.types.read_none_connection_metadata.ReadNoneConnectionMetadata"
    )


class _ReadAuthenticationMetadata_IamConnectionMetadata(TypedDict, closed=True):
    IamConnectionMetadata: (
        "capo_quicksight.types.read_iam_connection_metadata.ReadIamConnectionMetadata"
    )


ReadAuthenticationMetadata: TypeAlias = (
    _ReadAuthenticationMetadata_AuthorizationCodeGrantMetadata
    | _ReadAuthenticationMetadata_ClientCredentialsGrantMetadata
    | _ReadAuthenticationMetadata_BasicAuthConnectionMetadata
    | _ReadAuthenticationMetadata_ApiKeyConnectionMetadata
    | _ReadAuthenticationMetadata_NoneConnectionMetadata
    | _ReadAuthenticationMetadata_IamConnectionMetadata
)


# --- restJson1 ser/de ---
def serialize_json(value: ReadAuthenticationMetadata) -> dict:
    if "AuthorizationCodeGrantMetadata" in value:
        import capo_quicksight.types.read_authorization_code_grant_metadata

        return {
            "AuthorizationCodeGrantMetadata": capo_quicksight.types.read_authorization_code_grant_metadata.serialize_json(
                value["AuthorizationCodeGrantMetadata"]
            )
        }
    elif "ClientCredentialsGrantMetadata" in value:
        import capo_quicksight.types.read_client_credentials_grant_metadata

        return {
            "ClientCredentialsGrantMetadata": capo_quicksight.types.read_client_credentials_grant_metadata.serialize_json(
                value["ClientCredentialsGrantMetadata"]
            )
        }
    elif "BasicAuthConnectionMetadata" in value:
        import capo_quicksight.types.read_basic_auth_connection_metadata

        return {
            "BasicAuthConnectionMetadata": capo_quicksight.types.read_basic_auth_connection_metadata.serialize_json(
                value["BasicAuthConnectionMetadata"]
            )
        }
    elif "ApiKeyConnectionMetadata" in value:
        import capo_quicksight.types.read_api_key_connection_metadata

        return {
            "ApiKeyConnectionMetadata": capo_quicksight.types.read_api_key_connection_metadata.serialize_json(
                value["ApiKeyConnectionMetadata"]
            )
        }
    elif "NoneConnectionMetadata" in value:
        import capo_quicksight.types.read_none_connection_metadata

        return {
            "NoneConnectionMetadata": capo_quicksight.types.read_none_connection_metadata.serialize_json(
                value["NoneConnectionMetadata"]
            )
        }
    elif "IamConnectionMetadata" in value:
        import capo_quicksight.types.read_iam_connection_metadata

        return {
            "IamConnectionMetadata": capo_quicksight.types.read_iam_connection_metadata.serialize_json(
                value["IamConnectionMetadata"]
            )
        }
    else:
        raise SerializationError("ReadAuthenticationMetadata: no variant present")


def deserialize_json(data: dict) -> ReadAuthenticationMetadata:
    if data.get("AuthorizationCodeGrantMetadata") is not None:
        import capo_quicksight.types.read_authorization_code_grant_metadata

        return {
            "AuthorizationCodeGrantMetadata": capo_quicksight.types.read_authorization_code_grant_metadata.deserialize_json(
                data["AuthorizationCodeGrantMetadata"]
            )
        }
    elif data.get("ClientCredentialsGrantMetadata") is not None:
        import capo_quicksight.types.read_client_credentials_grant_metadata

        return {
            "ClientCredentialsGrantMetadata": capo_quicksight.types.read_client_credentials_grant_metadata.deserialize_json(
                data["ClientCredentialsGrantMetadata"]
            )
        }
    elif data.get("BasicAuthConnectionMetadata") is not None:
        import capo_quicksight.types.read_basic_auth_connection_metadata

        return {
            "BasicAuthConnectionMetadata": capo_quicksight.types.read_basic_auth_connection_metadata.deserialize_json(
                data["BasicAuthConnectionMetadata"]
            )
        }
    elif data.get("ApiKeyConnectionMetadata") is not None:
        import capo_quicksight.types.read_api_key_connection_metadata

        return {
            "ApiKeyConnectionMetadata": capo_quicksight.types.read_api_key_connection_metadata.deserialize_json(
                data["ApiKeyConnectionMetadata"]
            )
        }
    elif data.get("NoneConnectionMetadata") is not None:
        import capo_quicksight.types.read_none_connection_metadata

        return {
            "NoneConnectionMetadata": capo_quicksight.types.read_none_connection_metadata.deserialize_json(
                data["NoneConnectionMetadata"]
            )
        }
    elif data.get("IamConnectionMetadata") is not None:
        import capo_quicksight.types.read_iam_connection_metadata

        return {
            "IamConnectionMetadata": capo_quicksight.types.read_iam_connection_metadata.deserialize_json(
                data["IamConnectionMetadata"]
            )
        }
    else:
        raise DeserializationError(
            "ReadAuthenticationMetadata: no recognized variant key"
        )


def redact_sensitive(value: ReadAuthenticationMetadata) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "BasicAuthConnectionMetadata" in value:
        import capo_quicksight.types.read_basic_auth_connection_metadata

        out["BasicAuthConnectionMetadata"] = (
            capo_quicksight.types.read_basic_auth_connection_metadata.redact_sensitive(
                value["BasicAuthConnectionMetadata"]
            )
        )
    if "ApiKeyConnectionMetadata" in value:
        import capo_quicksight.types.read_api_key_connection_metadata

        out["ApiKeyConnectionMetadata"] = (
            capo_quicksight.types.read_api_key_connection_metadata.redact_sensitive(
                value["ApiKeyConnectionMetadata"]
            )
        )
    return out
