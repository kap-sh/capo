"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspaceCreationProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.arn
    import capo_workspaces.types.boolean_object
    import capo_workspaces.types.default_ou
    import capo_workspaces.types.security_group_id


class WorkspaceCreationProperties(TypedDict, closed=True):
    enable_internet_access: NotRequired[
        "capo_workspaces.types.boolean_object.BooleanObject"
    ]
    """<p>Indicates whether internet access is enabled for your WorkSpaces.</p>"""
    default_ou: NotRequired["capo_workspaces.types.default_ou.DefaultOu"]
    """<p>The default organizational unit (OU) for your WorkSpaces directories. This string must be the full Lightweight Directory Access Protocol (LDAP) distinguished name for the target domain and OU. It must be in the form <code>"OU=<i>value</i>,DC=<i>value</i>,DC=<i>value</i>"</code>, where <i>value</i> is any string of characters, and the number of domain components (DCs) is two or more. For example, <code>OU=WorkSpaces_machines,DC=machines,DC=example,DC=com</code>. </p> <important> <ul> <li> <p>To avoid errors, certain characters in the distinguished name must be escaped. For more information, see <a href="https://docs.microsoft.com/previous-versions/windows/desktop/ldap/distinguished-names"> Distinguished Names</a> in the Microsoft documentation.</p> </li> <li> <p>The API doesn't validate whether the OU exists.</p> </li> </ul> </important>"""
    custom_security_group_id: NotRequired[
        "capo_workspaces.types.security_group_id.SecurityGroupId"
    ]
    """<p>The identifier of your custom security group.</p>"""
    user_enabled_as_local_administrator: NotRequired[
        "capo_workspaces.types.boolean_object.BooleanObject"
    ]
    """<p>Indicates whether users are local administrators of their WorkSpaces.</p>"""
    enable_maintenance_mode: NotRequired[
        "capo_workspaces.types.boolean_object.BooleanObject"
    ]
    """<p>Indicates whether maintenance mode is enabled for your WorkSpaces. For more information, see <a href="https://docs.aws.amazon.com/workspaces/latest/adminguide/workspace-maintenance.html">WorkSpace Maintenance</a>. </p>"""
    instance_iam_role_arn: NotRequired["capo_workspaces.types.arn.ARN"]
    """<p>Indicates the IAM role ARN of the instance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkspaceCreationProperties) -> dict:
    out: dict = {}
    if "enable_internet_access" in value:
        out["EnableInternetAccess"] = value["enable_internet_access"]
    if "default_ou" in value:
        out["DefaultOu"] = value["default_ou"]
    if "custom_security_group_id" in value:
        out["CustomSecurityGroupId"] = value["custom_security_group_id"]
    if "user_enabled_as_local_administrator" in value:
        out["UserEnabledAsLocalAdministrator"] = value[
            "user_enabled_as_local_administrator"
        ]
    if "enable_maintenance_mode" in value:
        out["EnableMaintenanceMode"] = value["enable_maintenance_mode"]
    if "instance_iam_role_arn" in value:
        out["InstanceIamRoleArn"] = value["instance_iam_role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WorkspaceCreationProperties:
    out: WorkspaceCreationProperties = {}  # type: ignore[typeddict-item]
    if data.get("EnableInternetAccess") is not None:
        out["enable_internet_access"] = data["EnableInternetAccess"]
    if data.get("DefaultOu") is not None:
        out["default_ou"] = data["DefaultOu"]
    if data.get("CustomSecurityGroupId") is not None:
        out["custom_security_group_id"] = data["CustomSecurityGroupId"]
    if data.get("UserEnabledAsLocalAdministrator") is not None:
        out["user_enabled_as_local_administrator"] = data[
            "UserEnabledAsLocalAdministrator"
        ]
    if data.get("EnableMaintenanceMode") is not None:
        out["enable_maintenance_mode"] = data["EnableMaintenanceMode"]
    if data.get("InstanceIamRoleArn") is not None:
        out["instance_iam_role_arn"] = data["InstanceIamRoleArn"]
    return out
