"""Generated from Smithy shape ``com.amazonaws.finspacedata#UserByPermissionGroup``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace_data.types.api_access
    import capo_finspace_data.types.email
    import capo_finspace_data.types.first_name
    import capo_finspace_data.types.last_name
    import capo_finspace_data.types.permission_group_membership_status
    import capo_finspace_data.types.role_arn
    import capo_finspace_data.types.user_id
    import capo_finspace_data.types.user_status
    import capo_finspace_data.types.user_type


class UserByPermissionGroup(TypedDict, closed=True):
    user_id: NotRequired["capo_finspace_data.types.user_id.UserId"]
    """<p>The unique identifier for the user.</p>"""
    status: NotRequired["capo_finspace_data.types.user_status.UserStatus"]
    """<p>The current status of the user. </p> <ul> <li> <p> <code>CREATING</code> – The user creation is in progress.</p> </li> <li> <p> <code>ENABLED</code> – The user is created and is currently active.</p> </li> <li> <p> <code>DISABLED</code> – The user is currently inactive.</p> </li> </ul>"""
    first_name: NotRequired["capo_finspace_data.types.first_name.FirstName"]
    """<p>The first name of the user.</p>"""
    last_name: NotRequired["capo_finspace_data.types.last_name.LastName"]
    """<p>The last name of the user.</p>"""
    email_address: NotRequired["capo_finspace_data.types.email.Email"]
    """<p>The email address of the user. The email address serves as a unique identifier for each user and cannot be changed after it's created.</p>"""
    type: NotRequired["capo_finspace_data.types.user_type.UserType"]
    """<p> Indicates the type of user.</p> <ul> <li> <p> <code>SUPER_USER</code> – A user with permission to all the functionality and data in FinSpace.</p> </li> <li> <p> <code>APP_USER</code> – A user with specific permissions in FinSpace. The users are assigned permissions by adding them to a permission group.</p> </li> </ul>"""
    api_access: NotRequired["capo_finspace_data.types.api_access.ApiAccess"]
    """<p>Indicates whether the user can access FinSpace API operations.</p> <ul> <li> <p> <code>ENABLED</code> – The user has permissions to use the API operations.</p> </li> <li> <p> <code>DISABLED</code> – The user does not have permissions to use any API operations.</p> </li> </ul>"""
    api_access_principal_arn: NotRequired["capo_finspace_data.types.role_arn.RoleArn"]
    """<p>The IAM ARN identifier that is attached to FinSpace API calls.</p>"""
    membership_status: NotRequired[
        "capo_finspace_data.types.permission_group_membership_status.PermissionGroupMembershipStatus"
    ]
    """<p>Indicates the status of the user within a permission group.</p> <ul> <li> <p> <code>ADDITION_IN_PROGRESS</code> – The user is currently being added to the permission group.</p> </li> <li> <p> <code>ADDITION_SUCCESS</code> – The user is successfully added to the permission group.</p> </li> <li> <p> <code>REMOVAL_IN_PROGRESS</code> – The user is currently being removed from the permission group.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserByPermissionGroup) -> dict:
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
    if "membership_status" in value:
        import capo_finspace_data.types.permission_group_membership_status

        out["membershipStatus"] = (
            capo_finspace_data.types.permission_group_membership_status.serialize_json(
                value["membership_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> UserByPermissionGroup:
    out: UserByPermissionGroup = {}  # type: ignore[typeddict-item]
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
    if data.get("membershipStatus") is not None:
        import capo_finspace_data.types.permission_group_membership_status

        out["membership_status"] = (
            capo_finspace_data.types.permission_group_membership_status.deserialize_json(
                data["membershipStatus"]
            )
        )
    return out


def redact_sensitive(value: UserByPermissionGroup) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "first_name" in value:
        out["first_name"] = "*** Sensitive Data Redacted ***"
    if "last_name" in value:
        out["last_name"] = "*** Sensitive Data Redacted ***"
    if "email_address" in value:
        out["email_address"] = "*** Sensitive Data Redacted ***"
    return out
