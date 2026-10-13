"""Generated from Smithy shape ``com.amazonaws.finspacedata#UpdatePermissionGroupRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace_data.types.application_permission_list
    import capo_finspace_data.types.client_token
    import capo_finspace_data.types.permission_group_description
    import capo_finspace_data.types.permission_group_id
    import capo_finspace_data.types.permission_group_name


class UpdatePermissionGroupRequest(TypedDict, closed=True):
    permission_group_id: (
        "capo_finspace_data.types.permission_group_id.PermissionGroupId"
    )
    """<p>The unique identifier for the permission group to update.</p>"""
    name: NotRequired[
        "capo_finspace_data.types.permission_group_name.PermissionGroupName"
    ]
    """<p>The name of the permission group.</p>"""
    description: NotRequired[
        "capo_finspace_data.types.permission_group_description.PermissionGroupDescription"
    ]
    """<p>A brief description for the permission group.</p>"""
    application_permissions: NotRequired[
        "capo_finspace_data.types.application_permission_list.ApplicationPermissionList"
    ]
    """<p>The permissions that are granted to a specific group for accessing the FinSpace application.</p> <important> <p>When assigning application permissions, be aware that the permission <code>ManageUsersAndGroups</code> allows users to grant themselves or others access to any functionality in their FinSpace environment's application. It should only be granted to trusted users.</p> </important> <ul> <li> <p> <code>CreateDataset</code> – Group members can create new datasets.</p> </li> <li> <p> <code>ManageClusters</code> – Group members can manage Apache Spark clusters from FinSpace notebooks.</p> </li> <li> <p> <code>ManageUsersAndGroups</code> – Group members can manage users and permission groups. This is a privileged permission that allows users to grant themselves or others access to any functionality in the application. It should only be granted to trusted users.</p> </li> <li> <p> <code>ManageAttributeSets</code> – Group members can manage attribute sets.</p> </li> <li> <p> <code>ViewAuditData</code> – Group members can view audit data.</p> </li> <li> <p> <code>AccessNotebooks</code> – Group members will have access to FinSpace notebooks.</p> </li> <li> <p> <code>GetTemporaryCredentials</code> – Group members can get temporary API credentials.</p> </li> </ul>"""
    client_token: NotRequired["capo_finspace_data.types.client_token.ClientToken"]
    """<p>A token that ensures idempotency. This token expires in 10 minutes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePermissionGroupRequest) -> dict:
    out: dict = {}
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
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdatePermissionGroupRequest:
    out: UpdatePermissionGroupRequest = {}  # type: ignore[typeddict-item]
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
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out


def redact_sensitive(value: UpdatePermissionGroupRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
