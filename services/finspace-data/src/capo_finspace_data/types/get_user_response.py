"""Generated from Smithy shape ``com.amazonaws.finspacedata#GetUserResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace_data.types.api_access
    import capo_finspace_data.types.email
    import capo_finspace_data.types.first_name
    import capo_finspace_data.types.last_name
    import capo_finspace_data.types.role_arn
    import capo_finspace_data.types.timestamp_epoch
    import capo_finspace_data.types.user_id
    import capo_finspace_data.types.user_status
    import capo_finspace_data.types.user_type


class GetUserResponse(TypedDict, closed=True):
    user_id: NotRequired["capo_finspace_data.types.user_id.UserId"]
    """<p>The unique identifier for the user that is retrieved.</p>"""
    status: NotRequired["capo_finspace_data.types.user_status.UserStatus"]
    """<p>The current status of the user. </p> <ul> <li> <p> <code>CREATING</code> – The creation is in progress.</p> </li> <li> <p> <code>ENABLED</code> – The user is created and is currently active.</p> </li> <li> <p> <code>DISABLED</code> – The user is currently inactive.</p> </li> </ul>"""
    first_name: NotRequired["capo_finspace_data.types.first_name.FirstName"]
    """<p>The first name of the user.</p>"""
    last_name: NotRequired["capo_finspace_data.types.last_name.LastName"]
    """<p>The last name of the user.</p>"""
    email_address: NotRequired["capo_finspace_data.types.email.Email"]
    """<p>The email address that is associated with the user.</p>"""
    type: NotRequired["capo_finspace_data.types.user_type.UserType"]
    """<p>Indicates the type of user. </p> <ul> <li> <p> <code>SUPER_USER</code> – A user with permission to all the functionality and data in FinSpace.</p> </li> </ul> <ul> <li> <p> <code>APP_USER</code> – A user with specific permissions in FinSpace. The users are assigned permissions by adding them to a permission group.</p> </li> </ul>"""
    api_access: NotRequired["capo_finspace_data.types.api_access.ApiAccess"]
    """<p>Indicates whether the user can use the <code>GetProgrammaticAccessCredentials</code> API to obtain credentials that can then be used to access other FinSpace Data API operations. </p> <ul> <li> <p> <code>ENABLED</code> – The user has permissions to use the APIs.</p> </li> <li> <p> <code>DISABLED</code> – The user does not have permissions to use any APIs.</p> </li> </ul>"""
    api_access_principal_arn: NotRequired["capo_finspace_data.types.role_arn.RoleArn"]
    """<p>The ARN identifier of an AWS user or role that is allowed to call the <code>GetProgrammaticAccessCredentials</code> API to obtain a credentials token for a specific FinSpace user. This must be an IAM role within your FinSpace account.</p>"""
    create_time: "capo_finspace_data.types.timestamp_epoch.TimestampEpoch"
    """<p>The timestamp at which the user was created in FinSpace. The value is determined as epoch time in milliseconds. </p>"""
    last_enabled_time: "capo_finspace_data.types.timestamp_epoch.TimestampEpoch"
    """<p>Describes the last time the user was activated. The value is determined as epoch time in milliseconds.</p>"""
    last_disabled_time: "capo_finspace_data.types.timestamp_epoch.TimestampEpoch"
    """<p>Describes the last time the user was deactivated. The value is determined as epoch time in milliseconds.</p>"""
    last_modified_time: "capo_finspace_data.types.timestamp_epoch.TimestampEpoch"
    """<p>Describes the last time the user details were updated. The value is determined as epoch time in milliseconds.</p>"""
    last_login_time: "capo_finspace_data.types.timestamp_epoch.TimestampEpoch"
    """<p>Describes the last time that the user logged into their account. The value is determined as epoch time in milliseconds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetUserResponse) -> dict:
    out: dict = {}
    if "user_id" in value:
        out["userId"] = value["user_id"]
    if "status" in value:
        import capo_finspace_data.types.user_status

        out["status"] = capo_finspace_data.types.user_status.serialize_json(
            value["status"]
        )
    if "first_name" in value:
        out["firstName"] = value["first_name"]
    if "last_name" in value:
        out["lastName"] = value["last_name"]
    if "email_address" in value:
        out["emailAddress"] = value["email_address"]
    if "type" in value:
        import capo_finspace_data.types.user_type

        out["type"] = capo_finspace_data.types.user_type.serialize_json(value["type"])
    if "api_access" in value:
        import capo_finspace_data.types.api_access

        out["apiAccess"] = capo_finspace_data.types.api_access.serialize_json(
            value["api_access"]
        )
    if "api_access_principal_arn" in value:
        out["apiAccessPrincipalArn"] = value["api_access_principal_arn"]
    out["createTime"] = value.get("create_time", 0)
    out["lastEnabledTime"] = value.get("last_enabled_time", 0)
    out["lastDisabledTime"] = value.get("last_disabled_time", 0)
    out["lastModifiedTime"] = value.get("last_modified_time", 0)
    out["lastLoginTime"] = value.get("last_login_time", 0)
    return out


def deserialize_json(data: dict) -> GetUserResponse:
    out: GetUserResponse = {}  # type: ignore[typeddict-item]
    if data.get("userId") is not None:
        out["user_id"] = data["userId"]
    if data.get("status") is not None:
        import capo_finspace_data.types.user_status

        out["status"] = capo_finspace_data.types.user_status.deserialize_json(
            data["status"]
        )
    if data.get("firstName") is not None:
        out["first_name"] = data["firstName"]
    if data.get("lastName") is not None:
        out["last_name"] = data["lastName"]
    if data.get("emailAddress") is not None:
        out["email_address"] = data["emailAddress"]
    if data.get("type") is not None:
        import capo_finspace_data.types.user_type

        out["type"] = capo_finspace_data.types.user_type.deserialize_json(data["type"])
    if data.get("apiAccess") is not None:
        import capo_finspace_data.types.api_access

        out["api_access"] = capo_finspace_data.types.api_access.deserialize_json(
            data["apiAccess"]
        )
    if data.get("apiAccessPrincipalArn") is not None:
        out["api_access_principal_arn"] = data["apiAccessPrincipalArn"]
    if data.get("createTime") is not None:
        out["create_time"] = data["createTime"]
    else:
        out["create_time"] = 0
    if data.get("lastEnabledTime") is not None:
        out["last_enabled_time"] = data["lastEnabledTime"]
    else:
        out["last_enabled_time"] = 0
    if data.get("lastDisabledTime") is not None:
        out["last_disabled_time"] = data["lastDisabledTime"]
    else:
        out["last_disabled_time"] = 0
    if data.get("lastModifiedTime") is not None:
        out["last_modified_time"] = data["lastModifiedTime"]
    else:
        out["last_modified_time"] = 0
    if data.get("lastLoginTime") is not None:
        out["last_login_time"] = data["lastLoginTime"]
    else:
        out["last_login_time"] = 0
    return out


def redact_sensitive(value: GetUserResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "first_name" in value:
        out["first_name"] = "*** Sensitive Data Redacted ***"
    if "last_name" in value:
        out["last_name"] = "*** Sensitive Data Redacted ***"
    if "email_address" in value:
        out["email_address"] = "*** Sensitive Data Redacted ***"
    return out
