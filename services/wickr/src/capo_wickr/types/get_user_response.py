"""Generated from Smithy shape ``com.amazonaws.wickr#GetUserResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wickr.types.generic_string
    import capo_wickr.types.security_group_id_list
    import capo_wickr.types.sensitive_string
    import capo_wickr.types.user_id


class GetUserResponse(TypedDict, closed=True):
    user_id: "capo_wickr.types.user_id.UserId"
    """<p>The unique identifier of the user.</p>"""
    first_name: NotRequired["capo_wickr.types.sensitive_string.SensitiveString"]
    """<p>The first name of the user.</p>"""
    last_name: NotRequired["capo_wickr.types.sensitive_string.SensitiveString"]
    """<p>The last name of the user.</p>"""
    username: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The email address or username of the user.</p>"""
    is_admin: NotRequired["bool"]
    """<p>Indicates whether the user has administrator privileges in the network.</p>"""
    suspended: NotRequired["bool"]
    """<p>Indicates whether the user is currently suspended.</p>"""
    status: NotRequired["int"]
    """<p>The current status of the user (1 for pending, 2 for active).</p>"""
    last_activity: NotRequired["int"]
    """<p>The timestamp of the user's last activity in the network, specified in epoch seconds.</p>"""
    last_login: NotRequired["int"]
    """<p>The timestamp of the user's last login to the network, specified in epoch seconds.</p>"""
    security_group_ids: NotRequired[
        "capo_wickr.types.security_group_id_list.SecurityGroupIdList"
    ]
    """<p>A list of security group IDs to which the user belongs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetUserResponse) -> dict:
    out: dict = {}
    out["userId"] = value["user_id"]
    if "first_name" in value:
        out["firstName"] = value["first_name"]
    if "last_name" in value:
        out["lastName"] = value["last_name"]
    if "username" in value:
        out["username"] = value["username"]
    if "is_admin" in value:
        out["isAdmin"] = value["is_admin"]
    if "suspended" in value:
        out["suspended"] = value["suspended"]
    if "status" in value:
        out["status"] = value["status"]
    if "last_activity" in value:
        out["lastActivity"] = value["last_activity"]
    if "last_login" in value:
        out["lastLogin"] = value["last_login"]
    if "security_group_ids" in value:
        import capo_wickr.types.security_group_id_list

        out["securityGroupIds"] = (
            capo_wickr.types.security_group_id_list.serialize_json(
                value["security_group_ids"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetUserResponse:
    out: GetUserResponse = {}  # type: ignore[typeddict-item]
    if data.get("userId") is not None:
        out["user_id"] = data["userId"]
    else:
        out["user_id"] = ""
    if data.get("firstName") is not None:
        out["first_name"] = data["firstName"]
    if data.get("lastName") is not None:
        out["last_name"] = data["lastName"]
    if data.get("username") is not None:
        out["username"] = data["username"]
    if data.get("isAdmin") is not None:
        out["is_admin"] = data["isAdmin"]
    if data.get("suspended") is not None:
        out["suspended"] = data["suspended"]
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("lastActivity") is not None:
        out["last_activity"] = data["lastActivity"]
    if data.get("lastLogin") is not None:
        out["last_login"] = data["lastLogin"]
    if data.get("securityGroupIds") is not None:
        import capo_wickr.types.security_group_id_list

        out["security_group_ids"] = (
            capo_wickr.types.security_group_id_list.deserialize_json(
                data["securityGroupIds"]
            )
        )
    return out


def redact_sensitive(value: GetUserResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "first_name" in value:
        out["first_name"] = "*** Sensitive Data Redacted ***"
    if "last_name" in value:
        out["last_name"] = "*** Sensitive Data Redacted ***"
    return out
