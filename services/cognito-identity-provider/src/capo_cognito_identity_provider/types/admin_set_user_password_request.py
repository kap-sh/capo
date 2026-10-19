"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AdminSetUserPasswordRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.boolean_type
    import capo_cognito_identity_provider.types.password_type
    import capo_cognito_identity_provider.types.user_pool_id_type
    import capo_cognito_identity_provider.types.username_type


class AdminSetUserPasswordRequest(TypedDict, closed=True):
    user_pool_id: (
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool where you want to set the user's password.</p>"""
    username: "capo_cognito_identity_provider.types.username_type.UsernameType"
    """<p>The name of the user that you want to query or modify. The value of this parameter is typically your user's username, but it can be any of their alias attributes. If <code>username</code> isn't an alias attribute in your user pool, this value must be the <code>sub</code> of a local user or the username of a user from a third-party IdP.</p>"""
    password: "capo_cognito_identity_provider.types.password_type.PasswordType"
    """<p>The new temporary or permanent password that you want to set for the user. You can't remove the password for a user who already has a password so that they can only sign in with passwordless methods. In this scenario, you must create a new user without a password.</p>"""
    permanent: NotRequired[
        "capo_cognito_identity_provider.types.boolean_type.BooleanType"
    ]
    """<p>Set to <code>true</code> to set a password that the user can immediately sign in with. Set to <code>false</code> to set a temporary password that the user must change on their next sign-in.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdminSetUserPasswordRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    out["Username"] = value["username"]
    out["Password"] = value["password"]
    if "permanent" in value:
        out["Permanent"] = value["permanent"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AdminSetUserPasswordRequest:
    out: AdminSetUserPasswordRequest = {}  # type: ignore[typeddict-item]
    if data.get("UserPoolId") is not None:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        raise DeserializationError("AdminSetUserPasswordRequest.user_pool_id required")
    if data.get("Username") is not None:
        out["username"] = data["Username"]
    else:
        raise DeserializationError("AdminSetUserPasswordRequest.username required")
    if data.get("Password") is not None:
        out["password"] = data["Password"]
    else:
        raise DeserializationError("AdminSetUserPasswordRequest.password required")
    if data.get("Permanent") is not None:
        out["permanent"] = data["Permanent"]
    return out


def redact_sensitive(value: AdminSetUserPasswordRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "username" in value:
        out["username"] = "*** Sensitive Data Redacted ***"
    if "password" in value:
        out["password"] = "*** Sensitive Data Redacted ***"
    return out
