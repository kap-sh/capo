"""Generated from Smithy shape ``com.amazonaws.finspacedata#PermissionGroup``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace_data.types.application_permission_list
    import capo_finspace_data.types.permission_group_description
    import capo_finspace_data.types.permission_group_id
    import capo_finspace_data.types.permission_group_membership_status
    import capo_finspace_data.types.permission_group_name
    import capo_finspace_data.types.timestamp_epoch


class PermissionGroup(TypedDict, closed=True):
    permission_group_id: NotRequired[
        "capo_finspace_data.types.permission_group_id.PermissionGroupId"
    ]
    """<p> The unique identifier for the permission group.</p>"""
    name: NotRequired[
        "capo_finspace_data.types.permission_group_name.PermissionGroupName"
    ]
    """<p>The name of the permission group.</p>"""
    description: NotRequired[
        "capo_finspace_data.types.permission_group_description.PermissionGroupDescription"
    ]
    """<p> A brief description for the permission group.</p>"""
    application_permissions: NotRequired[
        "capo_finspace_data.types.application_permission_list.ApplicationPermissionList"
    ]
    """<p>Indicates the permissions that are granted to a specific group for accessing the FinSpace application.</p> <important> <p>When assigning application permissions, be aware that the permission <code>ManageUsersAndGroups</code> allows users to grant themselves or others access to any functionality in their FinSpace environment's application. It should only be granted to trusted users.</p> </important> <ul> <li> <p> <code>CreateDataset</code> – Group members can create new datasets.</p> </li> <li> <p> <code>ManageClusters</code> – Group members can manage Apache Spark clusters from FinSpace notebooks.</p> </li> <li> <p> <code>ManageUsersAndGroups</code> – Group members can manage users and permission groups. This is a privileged permission that allows users to grant themselves or others access to any functionality in the application. It should only be granted to trusted users.</p> </li> <li> <p> <code>ManageAttributeSets</code> – Group members can manage attribute sets.</p> </li> <li> <p> <code>ViewAuditData</code> – Group members can view audit data.</p> </li> <li> <p> <code>AccessNotebooks</code> – Group members will have access to FinSpace notebooks.</p> </li> <li> <p> <code>GetTemporaryCredentials</code> – Group members can get temporary API credentials.</p> </li> </ul>"""
    create_time: "capo_finspace_data.types.timestamp_epoch.TimestampEpoch"
    """<p>The timestamp at which the group was created in FinSpace. The value is determined as epoch time in milliseconds. </p>"""
    last_modified_time: "capo_finspace_data.types.timestamp_epoch.TimestampEpoch"
    """<p>Describes the last time the permission group was updated. The value is determined as epoch time in milliseconds. </p>"""
    membership_status: NotRequired[
        "capo_finspace_data.types.permission_group_membership_status.PermissionGroupMembershipStatus"
    ]
    """<p>Indicates the status of the user within a permission group.</p> <ul> <li> <p> <code>ADDITION_IN_PROGRESS</code> – The user is currently being added to the permission group.</p> </li> <li> <p> <code>ADDITION_SUCCESS</code> – The user is successfully added to the permission group.</p> </li> <li> <p> <code>REMOVAL_IN_PROGRESS</code> – The user is currently being removed from the permission group.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: PermissionGroup) -> dict:
    out: dict = {}
    if "permission_group_id" in value:
        out["permissionGroupId"] = value["permission_group_id"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "application_permissions" in value:
        import capo_finspace_data.types.application_permission_list

        out["applicationPermissions"] = (
            capo_finspace_data.types.application_permission_list.serialize_json(
                value["application_permissions"]
            )
        )
    out["createTime"] = value.get("create_time", 0)
    out["lastModifiedTime"] = value.get("last_modified_time", 0)
    if "membership_status" in value:
        import capo_finspace_data.types.permission_group_membership_status

        out["membershipStatus"] = (
            capo_finspace_data.types.permission_group_membership_status.serialize_json(
                value["membership_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> PermissionGroup:
    out: PermissionGroup = {}  # type: ignore[typeddict-item]
    if data.get("permissionGroupId") is not None:
        out["permission_group_id"] = data["permissionGroupId"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("applicationPermissions") is not None:
        import capo_finspace_data.types.application_permission_list

        out["application_permissions"] = (
            capo_finspace_data.types.application_permission_list.deserialize_json(
                data["applicationPermissions"]
            )
        )
    if data.get("createTime") is not None:
        out["create_time"] = data["createTime"]
    else:
        out["create_time"] = 0
    if data.get("lastModifiedTime") is not None:
        out["last_modified_time"] = data["lastModifiedTime"]
    else:
        out["last_modified_time"] = 0
    if data.get("membershipStatus") is not None:
        import capo_finspace_data.types.permission_group_membership_status

        out["membership_status"] = (
            capo_finspace_data.types.permission_group_membership_status.deserialize_json(
                data["membershipStatus"]
            )
        )
    return out


def redact_sensitive(value: PermissionGroup) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
