"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UserPoolClientDescription``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.client_id_type
    import capo_cognito_identity_provider.types.client_name_type
    import capo_cognito_identity_provider.types.user_pool_id_type


class UserPoolClientDescription(TypedDict, closed=True):
    client_id: NotRequired[
        "capo_cognito_identity_provider.types.client_id_type.ClientIdType"
    ]
    """<p>The app client ID.</p>"""
    user_pool_id: NotRequired[
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    ]
    """<p>The ID of the user pool that's associated with the app client.</p>"""
    client_name: NotRequired[
        "capo_cognito_identity_provider.types.client_name_type.ClientNameType"
    ]
    """<p>The app client name.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserPoolClientDescription) -> dict:
    out: dict = {}
    if "client_id" in value:
        out["ClientId"] = value["client_id"]
    if "user_pool_id" in value:
        out["UserPoolId"] = value["user_pool_id"]
    if "client_name" in value:
        out["ClientName"] = value["client_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UserPoolClientDescription:
    out: UserPoolClientDescription = {}  # type: ignore[typeddict-item]
    if data.get("ClientId") is not None:
        out["client_id"] = data["ClientId"]
    if data.get("UserPoolId") is not None:
        out["user_pool_id"] = data["UserPoolId"]
    if data.get("ClientName") is not None:
        out["client_name"] = data["ClientName"]
    return out


def redact_sensitive(value: UserPoolClientDescription) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "client_id" in value:
        out["client_id"] = "*** Sensitive Data Redacted ***"
    return out
