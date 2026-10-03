"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsIamGroupDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_iam_attached_managed_policy_list
    import capo_securityhub.types.aws_iam_group_policy_list
    import capo_securityhub.types.non_empty_string


class AwsIamGroupDetails(TypedDict, closed=True):
    attached_managed_policies: NotRequired[
        "capo_securityhub.types.aws_iam_attached_managed_policy_list.AwsIamAttachedManagedPolicyList"
    ]
    """<p>A list of the managed policies that are attached to the IAM group.</p>"""
    create_date: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Indicates when the IAM group was created.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>"""
    group_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The identifier of the IAM group.</p>"""
    group_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the IAM group.</p>"""
    group_policy_list: NotRequired[
        "capo_securityhub.types.aws_iam_group_policy_list.AwsIamGroupPolicyList"
    ]
    """<p>The list of inline policies that are embedded in the group.</p>"""
    path: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The path to the group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsIamGroupDetails) -> dict:
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
    if "group_id" in value:
        out["GroupId"] = value["group_id"]
    if "group_name" in value:
        out["GroupName"] = value["group_name"]
    if "group_policy_list" in value:
        import capo_securityhub.types.aws_iam_group_policy_list

        out["GroupPolicyList"] = (
            capo_securityhub.types.aws_iam_group_policy_list.serialize_json(
                value["group_policy_list"]
            )
        )
    if "path" in value:
        out["Path"] = value["path"]
    return out


def deserialize_json(data: dict) -> AwsIamGroupDetails:
    out: AwsIamGroupDetails = {}  # type: ignore[typeddict-item]
    if data.get("AttachedManagedPolicies") is not None:
        import capo_securityhub.types.aws_iam_attached_managed_policy_list

        out["attached_managed_policies"] = (
            capo_securityhub.types.aws_iam_attached_managed_policy_list.deserialize_json(
                data["AttachedManagedPolicies"]
            )
        )
    if data.get("CreateDate") is not None:
        out["create_date"] = data["CreateDate"]
    if data.get("GroupId") is not None:
        out["group_id"] = data["GroupId"]
    if data.get("GroupName") is not None:
        out["group_name"] = data["GroupName"]
    if data.get("GroupPolicyList") is not None:
        import capo_securityhub.types.aws_iam_group_policy_list

        out["group_policy_list"] = (
            capo_securityhub.types.aws_iam_group_policy_list.deserialize_json(
                data["GroupPolicyList"]
            )
        )
    if data.get("Path") is not None:
        out["path"] = data["Path"]
    return out
