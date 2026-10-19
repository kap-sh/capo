"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AdminGetUserAuthFactorsRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.user_pool_id_type
    import capo_cognito_identity_provider.types.username_type


class AdminGetUserAuthFactorsRequest(TypedDict, closed=True):
    user_pool_id: (
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool where you want to get information about the user's authentication factors.</p>"""
    username: "capo_cognito_identity_provider.types.username_type.UsernameType"
    """<p>The name of the user that you want to query or modify. The value of this parameter is typically your user's username, but it can be any of their alias attributes. If <code>username</code> isn't an alias attribute in your user pool, this value must be the <code>sub</code> of a local user or the username of a user from a third-party IdP.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdminGetUserAuthFactorsRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    out["Username"] = value["username"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AdminGetUserAuthFactorsRequest:
    out: AdminGetUserAuthFactorsRequest = {}  # type: ignore[typeddict-item]
    if data.get("UserPoolId") is not None:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        out["user_pool_id"] = ""
    if data.get("Username") is not None:
        out["username"] = data["Username"]
    else:
        out["username"] = ""
    return out


def redact_sensitive(value: AdminGetUserAuthFactorsRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "username" in value:
        out["username"] = "*** Sensitive Data Redacted ***"
    return out
