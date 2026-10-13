"""Generated from Smithy shape ``com.amazonaws.finspacedata#PermissionGroupByUser``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace_data.types.permission_group_id
    import capo_finspace_data.types.permission_group_membership_status
    import capo_finspace_data.types.permission_group_name


class PermissionGroupByUser(TypedDict, closed=True):
    permission_group_id: NotRequired[
        "capo_finspace_data.types.permission_group_id.PermissionGroupId"
    ]
    """<p>The unique identifier for the permission group.</p>"""
    name: NotRequired[
        "capo_finspace_data.types.permission_group_name.PermissionGroupName"
    ]
    """<p>The name of the permission group.</p>"""
    membership_status: NotRequired[
        "capo_finspace_data.types.permission_group_membership_status.PermissionGroupMembershipStatus"
    ]
    """<p>Indicates the status of the user within a permission group.</p> <ul> <li> <p> <code>ADDITION_IN_PROGRESS</code> – The user is currently being added to the permission group.</p> </li> <li> <p> <code>ADDITION_SUCCESS</code> – The user is successfully added to the permission group.</p> </li> <li> <p> <code>REMOVAL_IN_PROGRESS</code> – The user is currently being removed from the permission group.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: PermissionGroupByUser) -> dict:
    out: dict = {}
    if "permission_group_id" in value:
        out["permissionGroupId"] = value["permission_group_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "membership_status" in value:
        import capo_finspace_data.types.permission_group_membership_status

        out["membershipStatus"] = (
            capo_finspace_data.types.permission_group_membership_status.serialize_json(
                value["membership_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> PermissionGroupByUser:
    out: PermissionGroupByUser = {}  # type: ignore[typeddict-item]
    if data.get("permissionGroupId") is not None:
        out["permission_group_id"] = data["permissionGroupId"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("membershipStatus") is not None:
        import capo_finspace_data.types.permission_group_membership_status

        out["membership_status"] = (
            capo_finspace_data.types.permission_group_membership_status.deserialize_json(
                data["membershipStatus"]
            )
        )
    return out


def redact_sensitive(value: PermissionGroupByUser) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    return out
