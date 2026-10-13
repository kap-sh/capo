"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#GetUICustomizationRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.client_id_type
    import capo_cognito_identity_provider.types.user_pool_id_type


class GetUICustomizationRequest(TypedDict, closed=True):
    user_pool_id: (
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool that you want to query for branding settings.</p>"""
    client_id: NotRequired[
        "capo_cognito_identity_provider.types.client_id_type.ClientIdType"
    ]
    """<p>The ID of the app client that you want to query for branding settings.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetUICustomizationRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    if "client_id" in value:
        out["ClientId"] = value["client_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetUICustomizationRequest:
    out: GetUICustomizationRequest = {}  # type: ignore[typeddict-item]
    if data.get("UserPoolId") is not None:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        raise DeserializationError("GetUICustomizationRequest.user_pool_id required")
    if data.get("ClientId") is not None:
        out["client_id"] = data["ClientId"]
    return out


def redact_sensitive(value: GetUICustomizationRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "client_id" in value:
        out["client_id"] = "*** Sensitive Data Redacted ***"
    return out
