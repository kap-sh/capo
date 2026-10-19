"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AdminGetDeviceRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.device_key_type
    import capo_cognito_identity_provider.types.user_pool_id_type
    import capo_cognito_identity_provider.types.username_type


class AdminGetDeviceRequest(TypedDict, closed=True):
    device_key: "capo_cognito_identity_provider.types.device_key_type.DeviceKeyType"
    """<p>The key of the device that you want to delete.</p>"""
    user_pool_id: (
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool where the device owner is a user.</p>"""
    username: "capo_cognito_identity_provider.types.username_type.UsernameType"
    """<p>The name of the user that you want to query or modify. The value of this parameter is typically your user's username, but it can be any of their alias attributes. If <code>username</code> isn't an alias attribute in your user pool, this value must be the <code>sub</code> of a local user or the username of a user from a third-party IdP.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdminGetDeviceRequest) -> dict:
    out: dict = {}
    out["DeviceKey"] = value["device_key"]
    out["UserPoolId"] = value["user_pool_id"]
    out["Username"] = value["username"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AdminGetDeviceRequest:
    out: AdminGetDeviceRequest = {}  # type: ignore[typeddict-item]
    if data.get("DeviceKey") is not None:
        out["device_key"] = data["DeviceKey"]
    else:
        out["device_key"] = ""
    if data.get("UserPoolId") is not None:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        out["user_pool_id"] = ""
    if data.get("Username") is not None:
        out["username"] = data["Username"]
    else:
        out["username"] = ""
    return out


def redact_sensitive(value: AdminGetDeviceRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "username" in value:
        out["username"] = "*** Sensitive Data Redacted ***"
    return out
