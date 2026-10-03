"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsIamPolicyDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_iam_policy_version_list
    import capo_securityhub.types.boolean
    import capo_securityhub.types.integer
    import capo_securityhub.types.non_empty_string


class AwsIamPolicyDetails(TypedDict, closed=True):
    attachment_count: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The number of users, groups, and roles that the policy is attached to.</p>"""
    create_date: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>When the policy was created.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>"""
    default_version_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The identifier of the default version of the policy.</p>"""
    description: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>A description of the policy.</p>"""
    is_attachable: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Whether the policy can be attached to a user, group, or role.</p>"""
    path: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The path to the policy.</p>"""
    permissions_boundary_usage_count: NotRequired[
        "capo_securityhub.types.integer.Integer"
    ]
    """<p>The number of users and roles that use the policy to set the permissions boundary.</p>"""
    policy_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The unique identifier of the policy.</p>"""
    policy_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the policy.</p>"""
    policy_version_list: NotRequired[
        "capo_securityhub.types.aws_iam_policy_version_list.AwsIamPolicyVersionList"
    ]
    """<p>List of versions of the policy.</p>"""
    update_date: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>When the policy was most recently updated.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsIamPolicyDetails) -> dict:
    out: dict = {}
    if "attachment_count" in value:
        out["AttachmentCount"] = value["attachment_count"]
    if "create_date" in value:
        out["CreateDate"] = value["create_date"]
    if "default_version_id" in value:
        out["DefaultVersionId"] = value["default_version_id"]
    if "description" in value:
        out["Description"] = value["description"]
    if "is_attachable" in value:
        out["IsAttachable"] = value["is_attachable"]
    if "path" in value:
        out["Path"] = value["path"]
    if "permissions_boundary_usage_count" in value:
        out["PermissionsBoundaryUsageCount"] = value["permissions_boundary_usage_count"]
    if "policy_id" in value:
        out["PolicyId"] = value["policy_id"]
    if "policy_name" in value:
        out["PolicyName"] = value["policy_name"]
    if "policy_version_list" in value:
        import capo_securityhub.types.aws_iam_policy_version_list

        out["PolicyVersionList"] = (
            capo_securityhub.types.aws_iam_policy_version_list.serialize_json(
                value["policy_version_list"]
            )
        )
    if "update_date" in value:
        out["UpdateDate"] = value["update_date"]
    return out


def deserialize_json(data: dict) -> AwsIamPolicyDetails:
    out: AwsIamPolicyDetails = {}  # type: ignore[typeddict-item]
    if data.get("AttachmentCount") is not None:
        out["attachment_count"] = data["AttachmentCount"]
    if data.get("CreateDate") is not None:
        out["create_date"] = data["CreateDate"]
    if data.get("DefaultVersionId") is not None:
        out["default_version_id"] = data["DefaultVersionId"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("IsAttachable") is not None:
        out["is_attachable"] = data["IsAttachable"]
    if data.get("Path") is not None:
        out["path"] = data["Path"]
    if data.get("PermissionsBoundaryUsageCount") is not None:
        out["permissions_boundary_usage_count"] = data["PermissionsBoundaryUsageCount"]
    if data.get("PolicyId") is not None:
        out["policy_id"] = data["PolicyId"]
    if data.get("PolicyName") is not None:
        out["policy_name"] = data["PolicyName"]
    if data.get("PolicyVersionList") is not None:
        import capo_securityhub.types.aws_iam_policy_version_list

        out["policy_version_list"] = (
            capo_securityhub.types.aws_iam_policy_version_list.deserialize_json(
                data["PolicyVersionList"]
            )
        )
    if data.get("UpdateDate") is not None:
        out["update_date"] = data["UpdateDate"]
    return out
