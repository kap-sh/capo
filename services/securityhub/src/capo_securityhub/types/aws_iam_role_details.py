"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsIamRoleDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_iam_attached_managed_policy_list
    import capo_securityhub.types.aws_iam_instance_profile_list
    import capo_securityhub.types.aws_iam_permissions_boundary
    import capo_securityhub.types.aws_iam_role_assume_role_policy_document
    import capo_securityhub.types.aws_iam_role_policy_list
    import capo_securityhub.types.integer
    import capo_securityhub.types.non_empty_string


class AwsIamRoleDetails(TypedDict, closed=True):
    assume_role_policy_document: NotRequired[
        "capo_securityhub.types.aws_iam_role_assume_role_policy_document.AwsIamRoleAssumeRolePolicyDocument"
    ]
    """<p>The trust policy that grants permission to assume the role.</p>"""
    attached_managed_policies: NotRequired[
        "capo_securityhub.types.aws_iam_attached_managed_policy_list.AwsIamAttachedManagedPolicyList"
    ]
    """<p>The list of the managed policies that are attached to the role.</p>"""
    create_date: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Indicates when the role was created.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>"""
    instance_profile_list: NotRequired[
        "capo_securityhub.types.aws_iam_instance_profile_list.AwsIamInstanceProfileList"
    ]
    """<p>The list of instance profiles that contain this role.</p>"""
    permissions_boundary: NotRequired[
        "capo_securityhub.types.aws_iam_permissions_boundary.AwsIamPermissionsBoundary"
    ]
    role_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The stable and unique string identifying the role.</p>"""
    role_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The friendly name that identifies the role.</p>"""
    role_policy_list: NotRequired[
        "capo_securityhub.types.aws_iam_role_policy_list.AwsIamRolePolicyList"
    ]
    """<p>The list of inline policies that are embedded in the role.</p>"""
    max_session_duration: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The maximum session duration (in seconds) that you want to set for the specified role.</p>"""
    path: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The path to the role.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsIamRoleDetails) -> dict:
    out: dict = {}
    if "assume_role_policy_document" in value:
        out["AssumeRolePolicyDocument"] = value["assume_role_policy_document"]
    if "attached_managed_policies" in value:
        import capo_securityhub.types.aws_iam_attached_managed_policy_list

        out["AttachedManagedPolicies"] = (
            capo_securityhub.types.aws_iam_attached_managed_policy_list.serialize_json(
                value["attached_managed_policies"]
            )
        )
    if "create_date" in value:
        out["CreateDate"] = value["create_date"]
    if "instance_profile_list" in value:
        import capo_securityhub.types.aws_iam_instance_profile_list

        out["InstanceProfileList"] = (
            capo_securityhub.types.aws_iam_instance_profile_list.serialize_json(
                value["instance_profile_list"]
            )
        )
    if "permissions_boundary" in value:
        import capo_securityhub.types.aws_iam_permissions_boundary

        out["PermissionsBoundary"] = (
            capo_securityhub.types.aws_iam_permissions_boundary.serialize_json(
                value["permissions_boundary"]
            )
        )
    if "role_id" in value:
        out["RoleId"] = value["role_id"]
    if "role_name" in value:
        out["RoleName"] = value["role_name"]
    if "role_policy_list" in value:
        import capo_securityhub.types.aws_iam_role_policy_list

        out["RolePolicyList"] = (
            capo_securityhub.types.aws_iam_role_policy_list.serialize_json(
                value["role_policy_list"]
            )
        )
    if "max_session_duration" in value:
        out["MaxSessionDuration"] = value["max_session_duration"]
    if "path" in value:
        out["Path"] = value["path"]
    return out


def deserialize_json(data: dict) -> AwsIamRoleDetails:
    out: AwsIamRoleDetails = {}  # type: ignore[typeddict-item]
    if data.get("AssumeRolePolicyDocument") is not None:
        out["assume_role_policy_document"] = data["AssumeRolePolicyDocument"]
    if data.get("AttachedManagedPolicies") is not None:
        import capo_securityhub.types.aws_iam_attached_managed_policy_list

        out["attached_managed_policies"] = (
            capo_securityhub.types.aws_iam_attached_managed_policy_list.deserialize_json(
                data["AttachedManagedPolicies"]
            )
        )
    if data.get("CreateDate") is not None:
        out["create_date"] = data["CreateDate"]
    if data.get("InstanceProfileList") is not None:
        import capo_securityhub.types.aws_iam_instance_profile_list

        out["instance_profile_list"] = (
            capo_securityhub.types.aws_iam_instance_profile_list.deserialize_json(
                data["InstanceProfileList"]
            )
        )
    if data.get("PermissionsBoundary") is not None:
        import capo_securityhub.types.aws_iam_permissions_boundary

        out["permissions_boundary"] = (
            capo_securityhub.types.aws_iam_permissions_boundary.deserialize_json(
                data["PermissionsBoundary"]
            )
        )
    if data.get("RoleId") is not None:
        out["role_id"] = data["RoleId"]
    if data.get("RoleName") is not None:
        out["role_name"] = data["RoleName"]
    if data.get("RolePolicyList") is not None:
        import capo_securityhub.types.aws_iam_role_policy_list

        out["role_policy_list"] = (
            capo_securityhub.types.aws_iam_role_policy_list.deserialize_json(
                data["RolePolicyList"]
            )
        )
    if data.get("MaxSessionDuration") is not None:
        out["max_session_duration"] = data["MaxSessionDuration"]
    if data.get("Path") is not None:
        out["path"] = data["Path"]
    return out
