"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#DeleteUserPoolClientSecretRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.client_id_type
    import capo_cognito_identity_provider.types.client_secret_id_type
    import capo_cognito_identity_provider.types.user_pool_id_type


class DeleteUserPoolClientSecretRequest(TypedDict, closed=True):
    user_pool_id: (
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool that contains the app client.</p>"""
    client_id: "capo_cognito_identity_provider.types.client_id_type.ClientIdType"
    """<p>The ID of the app client from which you want to delete the secret.</p>"""
    client_secret_id: (
        "capo_cognito_identity_provider.types.client_secret_id_type.ClientSecretIdType"
    )
    """<p>The unique identifier of the client secret you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteUserPoolClientSecretRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    out["ClientId"] = value["client_id"]
    out["ClientSecretId"] = value["client_secret_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteUserPoolClientSecretRequest:
    out: DeleteUserPoolClientSecretRequest = {}  # type: ignore[typeddict-item]
    if data.get("UserPoolId") is not None:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        raise DeserializationError(
            "DeleteUserPoolClientSecretRequest.user_pool_id required"
        )
    if data.get("ClientId") is not None:
        out["client_id"] = data["ClientId"]
    else:
        raise DeserializationError(
            "DeleteUserPoolClientSecretRequest.client_id required"
        )
    if data.get("ClientSecretId") is not None:
        out["client_secret_id"] = data["ClientSecretId"]
    else:
        raise DeserializationError(
            "DeleteUserPoolClientSecretRequest.client_secret_id required"
        )
    return out


def redact_sensitive(value: DeleteUserPoolClientSecretRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "client_id" in value:
        out["client_id"] = "*** Sensitive Data Redacted ***"
    return out
