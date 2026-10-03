"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsIamUserDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_iam_attached_managed_policy_list
    import capo_securityhub.types.aws_iam_permissions_boundary
    import capo_securityhub.types.aws_iam_user_policy_list
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.string_list


class AwsIamUserDetails(TypedDict, closed=True):
    attached_managed_policies: NotRequired[
        "capo_securityhub.types.aws_iam_attached_managed_policy_list.AwsIamAttachedManagedPolicyList"
    ]
    """<p>A list of the managed policies that are attached to the user.</p>"""
    create_date: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Indicates when the user was created.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>"""
    group_list: NotRequired["capo_securityhub.types.string_list.StringList"]
    """<p>A list of IAM groups that the user belongs to.</p>"""
    path: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The path to the user.</p>"""
    permissions_boundary: NotRequired[
        "capo_securityhub.types.aws_iam_permissions_boundary.AwsIamPermissionsBoundary"
    ]
    """<p>The permissions boundary for the user.</p>"""
    user_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The unique identifier for the user.</p>"""
    user_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the user.</p>"""
    user_policy_list: NotRequired[
        "capo_securityhub.types.aws_iam_user_policy_list.AwsIamUserPolicyList"
    ]
    """<p>The list of inline policies that are embedded in the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsIamUserDetails) -> dict:
    out: dict = {}
    if "attached_managed_policies" in value:
        import capo_securityhub.types.aws_iam_attached_managed_policy_list

        out["AttachedManagedPolicies"] = (
            capo_securityhub.types.aws_iam_attached_managed_policy_list.serialize_json(
                value["attached_managed_policies"]
            )
        )
    if "create_date" in value:
        out["CreateDate"] = value["create_date"]
    if "group_list" in value:
        import capo_securityhub.types.string_list

        out["GroupList"] = capo_securityhub.types.string_list.serialize_json(
            value["group_list"]
        )
    if "path" in value:
        out["Path"] = value["path"]
    if "permissions_boundary" in value:
        import capo_securityhub.types.aws_iam_permissions_boundary

        out["PermissionsBoundary"] = (
            capo_securityhub.types.aws_iam_permissions_boundary.serialize_json(
                value["permissions_boundary"]
            )
        )
    if "user_id" in value:
        out["UserId"] = value["user_id"]
    if "user_name" in value:
        out["UserName"] = value["user_name"]
    if "user_policy_list" in value:
        import capo_securityhub.types.aws_iam_user_policy_list

        out["UserPolicyList"] = (
            capo_securityhub.types.aws_iam_user_policy_list.serialize_json(
                value["user_policy_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsIamUserDetails:
    out: AwsIamUserDetails = {}  # type: ignore[typeddict-item]
    if data.get("AttachedManagedPolicies") is not None:
        import capo_securityhub.types.aws_iam_attached_managed_policy_list

        out["attached_managed_policies"] = (
            capo_securityhub.types.aws_iam_attached_managed_policy_list.deserialize_json(
                data["AttachedManagedPolicies"]
            )
        )
    if data.get("CreateDate") is not None:
        out["create_date"] = data["CreateDate"]
    if data.get("GroupList") is not None:
        import capo_securityhub.types.string_list

        out["group_list"] = capo_securityhub.types.string_list.deserialize_json(
            data["GroupList"]
        )
    if data.get("Path") is not None:
        out["path"] = data["Path"]
    if data.get("PermissionsBoundary") is not None:
        import capo_securityhub.types.aws_iam_permissions_boundary

        out["permissions_boundary"] = (
            capo_securityhub.types.aws_iam_permissions_boundary.deserialize_json(
                data["PermissionsBoundary"]
            )
        )
    if data.get("UserId") is not None:
        out["user_id"] = data["UserId"]
    if data.get("UserName") is not None:
        out["user_name"] = data["UserName"]
    if data.get("UserPolicyList") is not None:
        import capo_securityhub.types.aws_iam_user_policy_list

        out["user_policy_list"] = (
            capo_securityhub.types.aws_iam_user_policy_list.deserialize_json(
                data["UserPolicyList"]
            )
        )
    return out
