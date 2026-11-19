"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#GetUserPoolClientSessionConfigurationRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.client_id_type
    import capo_cognito_identity_provider.types.user_pool_id_type


class GetUserPoolClientSessionConfigurationRequest(TypedDict, closed=True):
    user_pool_id: (
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool that contains the app client.</p>"""
    client_id: "capo_cognito_identity_provider.types.client_id_type.ClientIdType"
    """<p>The ID of the app client where you want to retrieve the session configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetUserPoolClientSessionConfigurationRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    out["ClientId"] = value["client_id"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> GetUserPoolClientSessionConfigurationRequest:
    out: GetUserPoolClientSessionConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("UserPoolId") is not None:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        out["user_pool_id"] = ""
    if data.get("ClientId") is not None:
        out["client_id"] = data["ClientId"]
    else:
        out["client_id"] = ""
    return out


def redact_sensitive(
    value: GetUserPoolClientSessionConfigurationRequest,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "client_id" in value:
        out["client_id"] = "*** Sensitive Data Redacted ***"
    return out
